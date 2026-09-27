"""Loopback-only demo. Never writes uploaded images or logs request bodies."""
import base64
import io
import json
import os
import re
import threading
from pathlib import Path
from urllib.parse import urlparse

import numpy as np
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageOps, UnidentifiedImageError
from scipy import ndimage
from starlette.concurrency import run_in_threadpool

import ai

ROOT = Path(__file__).resolve().parent
os.environ.setdefault("U2NET_HOME", str(ROOT / ".models" / "rembg"))
Image.MAX_IMAGE_PIXELS = 16_000_000
BODY_LIMIT = 29 * 1024 * 1024
FILE_LIMIT = 10 * 1024 * 1024
IMAGE_PATTERN = re.compile(r"^data:image/(png|jpeg|webp);base64,([A-Za-z0-9+/=]+)$")
AI_LOCK = threading.Lock()
BG_LOCK = threading.Lock()
REMBG_SESSION = None
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


def fail(status, code, message):
    raise ai.AIError(status, code, message)


@app.exception_handler(ai.AIError)
async def safe_error(request, exc):
    return JSONResponse({"error": {"code": exc.code, "message": exc.message}}, status_code=exc.status,
                        headers={"Cache-Control": "no-store"})


@app.middleware("http")
async def privacy_boundary(request, call_next):
    host = urlparse("http://" + request.headers.get("host", "")).hostname
    if host not in ("127.0.0.1", "localhost", "testserver"):
        return JSONResponse({"error": {"code": "HOST_REJECTED", "message": "Chỉ truy cập demo cục bộ."}},
                            status_code=403, headers={"Cache-Control": "no-store"})
    origin = request.headers.get("origin")
    if request.method != "GET" and origin and origin != str(request.base_url).rstrip("/"):
        return JSONResponse({"error": {"code": "ORIGIN_REJECTED", "message": "Nguồn yêu cầu không hợp lệ."}},
                            status_code=403, headers={"Cache-Control": "no-store"})
    if request.method != "GET" and request.headers.get("sec-fetch-site") == "cross-site":
        return JSONResponse({"error": {"code": "ORIGIN_REJECTED", "message": "Nguồn yêu cầu không hợp lệ."}},
                            status_code=403, headers={"Cache-Control": "no-store"})
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "no-referrer"
    return response


async def read_payload(request):
    if request.headers.get("content-type", "").split(";")[0] != "application/json":
        fail(400, "INVALID_JSON", "Yêu cầu phải có định dạng JSON.")
    raw = bytearray()
    async for part in request.stream():
        if len(raw) + len(part) > BODY_LIMIT:
            fail(413, "BODY_TOO_LARGE", "Ảnh vượt giới hạn xử lý.")
        raw.extend(part)
    try:
        payload = json.loads(raw)
        if not isinstance(payload, dict):
            raise ValueError()
        return payload
    except (ValueError, UnicodeDecodeError):
        fail(400, "INVALID_JSON", "Dữ liệu yêu cầu không hợp lệ.")


def decode_image(value):
    if not isinstance(value, str):
        fail(400, "INVALID_IMAGE", "Chọn ảnh PNG, JPEG hoặc WebP hợp lệ.")
    if len(value) > FILE_LIMIT * 4 // 3 + 100:
        fail(413, "IMAGE_TOO_LARGE", "Mỗi ảnh tối đa 10 MiB.")
    match = IMAGE_PATTERN.fullmatch(value)
    if not match:
        fail(400, "INVALID_IMAGE", "Chọn ảnh PNG, JPEG hoặc WebP hợp lệ.")
    try:
        raw = base64.b64decode(match[2], validate=True)
        if len(raw) > FILE_LIMIT:
            fail(413, "IMAGE_TOO_LARGE", "Mỗi ảnh tối đa 10 MiB.")
        with Image.open(io.BytesIO(raw)) as source:
            if source.format != {"png": "PNG", "jpeg": "JPEG", "webp": "WEBP"}[match[1]]:
                fail(400, "MIME_MISMATCH", "Nội dung ảnh không khớp định dạng.")
            if source.width * source.height > 16_000_000:
                fail(413, "PIXEL_LIMIT", "Ảnh quá lớn. Chọn ảnh dưới 16 triệu pixel.")
            source.load()
            return ImageOps.exif_transpose(source).convert("RGBA")
    except ai.AIError:
        raise
    except Image.DecompressionBombError:
        fail(413, "PIXEL_LIMIT", "Ảnh quá lớn. Chọn ảnh dưới 16 triệu pixel.")
    except (UnidentifiedImageError, ValueError, OSError):
        fail(400, "INVALID_IMAGE", "Không đọc được ảnh. Hãy chọn một ảnh khác.")


def remove_solid(image, tolerance=35):
    pixels = np.array(image.convert("RGBA"))
    rgb = pixels[..., :3].astype(np.float32)
    samples = rgb[[0, 0, -1, -1], [0, -1, 0, -1]]
    colour = np.median(samples, axis=0)
    candidates = np.linalg.norm(rgb - colour, axis=-1) <= tolerance
    labels, _ = ndimage.label(candidates)
    border = np.unique(np.concatenate((labels[0], labels[-1], labels[:, 0], labels[:, -1])))
    border = border[border != 0]
    pixels[np.isin(labels, border), 3] = 0
    return Image.fromarray(pixels)


def process_background(payload):
    mode = payload.get("mode", "subject")
    tolerance = payload.get("tolerance", 35)
    if mode not in ("subject", "solid") or type(tolerance) is not int or not 5 <= tolerance <= 100:
        fail(400, "INVALID_OPTIONS", "Tuỳ chọn xóa nền không hợp lệ.")
    image = decode_image(payload.get("image"))
    if mode == "solid":
        return {"image": ai.png_uri(remove_solid(image, tolerance))}
    if not BG_LOCK.acquire(blocking=False):
        fail(429, "BACKGROUND_BUSY", "Một ảnh khác đang được xử lý. Thử lại sau.")
    try:
        global REMBG_SESSION
        from rembg import new_session, remove
        if REMBG_SESSION is None:
            REMBG_SESSION = new_session("u2netp")
        result = remove(image, session=REMBG_SESSION)
        return {"image": ai.png_uri(result)}
    except ai.AIError:
        raise
    except Exception:
        fail(503, "BACKGROUND_UNAVAILABLE", "Không tải được mô hình xóa nền. Có thể dùng chế độ nền đơn sắc.")
    finally:
        BG_LOCK.release()


def process_tryon(payload):
    revision = payload.get("designRevision")
    if type(revision) is not int or revision < 0 or type(payload.get("externalConsent", False)) is not bool:
        fail(400, "INVALID_REVISION", "Dữ liệu thiết kế không hợp lệ.")
    person = decode_image(payload.get("personImage"))
    garment = decode_image(payload.get("garmentImage"))
    if not AI_LOCK.acquire(blocking=False):
        fail(429, "AI_BUSY", "AI đang xử lý một ảnh. Vui lòng thử lại sau.")
    try:
        result, engine = ai.generate(person, garment, payload.get("externalConsent", False))
        return {"image": result, "designRevision": revision, "engine": engine}
    finally:
        AI_LOCK.release()


@app.get("/api/status")
def engine_status():
    return {"backgroundRemoval": True, "tryOn": ai.status()}


@app.post("/api/remove-background")
async def remove_background(request: Request):
    return await run_in_threadpool(process_background, await read_payload(request))


@app.post("/api/try-on")
async def try_on(request: Request):
    return await run_in_threadpool(process_tryon, await read_payload(request))


app.mount("/", StaticFiles(directory=ROOT / "web", html=True), name="web")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=int(os.getenv("PORT", "8765")), access_log=False)
