"""OpenAI-only try-on. Credentials and image data never reach logs or disk."""
import base64
import io
import os
from pathlib import Path
import httpx
from PIL import Image

ROOT = Path(__file__).resolve().parent

class AIError(Exception):
    def __init__(self, status, code, message):
        self.status, self.code, self.message = status, code, message


def api_key():
    key = os.getenv("OPENAI_API_KEY", "").strip()
    if key:
        return key
    # Read only at runtime; never expose the value through status/errors.
    try:
        for line in (ROOT.parents[1] / "docs" / "env" / ".env").read_text(encoding="utf-8-sig").splitlines():
            name, separator, value = line.partition("=")
            if separator and name.strip() == "OPENAI_API_KEY":
                return value.strip().strip("\"'")
    except OSError:
        pass
    return ""


def status():
    ready = bool(api_key())
    return dict(engine="openai", available=ready, notice=(
        "OpenAI: ảnh gửi tới OpenAI khi bạn đồng ý và bấm thử áo. Ứng dụng không lưu ảnh; chính sách lưu của nhà cung cấp áp dụng."
        if ready else "Chưa cấu hình OpenAI. Điền OPENAI_API_KEY trong docs/env/.env trên máy của bạn."
    ))


def png_bytes(image):
    stream = io.BytesIO()
    image.save(stream, format="PNG")
    return stream.getvalue()


def png_uri(image):
    return "data:image/png;base64," + base64.b64encode(png_bytes(image)).decode("ascii")


def hosted_tryon(person, garment, consent, client=None):
    if consent is not True:
        raise AIError(403, "EXTERNAL_CONSENT", "Cần đồng ý gửi ảnh tới OpenAI trước khi tạo.")
    key = api_key()
    if not key:
        raise AIError(503, "AI_UNAVAILABLE", "Chưa cấu hình OpenAI API key trên máy chủ.")
    owned = client is None
    client = client or httpx.Client(timeout=180, follow_redirects=False)
    try:
        response = client.post("https://api.openai.com/v1/images/edits",
            headers={"Authorization": "Bearer " + key},
            data={"model": "gpt-image-1", "size": "1024x1536", "quality": "medium",
                  "input_fidelity": "high", "n": "1", "prompt":
                  "Edit the first image: replace only the person's current top with the polo in the second image. "
                  "Preserve the person's face, identity, body, pose, hands, background and lighting. "
                  "Match the polo colour, collar, fabric and print placement, lettering and logo from the garment reference. "
                  "Fit fabric naturally to the torso with realistic folds. Keep all other clothing unchanged. "
                  "Return one photorealistic clothed portrait; do not add text or change the person."},
            files=[("image[]", ("person.png", png_bytes(person), "image/png")),
                   ("image[]", ("polo.png", png_bytes(garment), "image/png"))])
        if response.status_code == 429:
            raise AIError(429, "AI_RATE_LIMIT", "OpenAI đang giới hạn yêu cầu hoặc hết hạn mức. Kiểm tra tài khoản API.")
        if response.status_code in (401, 403):
            raise AIError(503, "AI_AUTH", "Kiểm tra API key và quyền sử dụng mô hình ảnh của OpenAI.")
        response.raise_for_status()
        encoded = response.json()["data"][0]["b64_json"]
        raw = base64.b64decode(encoded, validate=True)
        with Image.open(io.BytesIO(raw)) as image:
            image.load()
            return png_uri(image)
    except AIError:
        raise
    except httpx.TimeoutException:
        raise AIError(504, "AI_TIMEOUT", "OpenAI phản hồi quá lâu. Thử lại sau.") from None
    except Exception:
        raise AIError(502, "AI_PROVIDER_FAILED", "Không tạo được ảnh với OpenAI. Thiết kế vẫn giữ trong phiên.") from None
    finally:
        if owned:
            client.close()


def generate(person, garment, consent=False):
    return hosted_tryon(person, garment, consent), "openai"
