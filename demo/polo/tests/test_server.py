"""Contract tests use synthetic images; fake AI transport is not real inference."""
import base64
import io
import os
import sys
import unittest
from types import SimpleNamespace
from pathlib import Path
from unittest.mock import patch

import httpx
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import ai
import server
from fastapi.testclient import TestClient


def fixture():
    image = Image.new("RGBA", (80, 80), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((15, 15, 65, 65), fill="navy")
    draw.rectangle((30, 30, 50, 50), fill="white")
    return image


class DemoContracts(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(server.app)
        self.image = ai.png_uri(fixture())

    def test_no_store_on_static_and_status(self):
        for path in ("/", "/api/status"):
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.headers["cache-control"], "no-store")

    def test_real_solid_removal_preserves_disconnected_white_detail(self):
        response = self.client.post("/api/remove-background", json={"image": self.image, "mode": "solid"})
        self.assertEqual(response.status_code, 200)
        result = server.decode_image(response.json()["image"])
        self.assertEqual(result.getpixel((0, 0))[3], 0)
        self.assertEqual(result.getpixel((20, 20))[3], 255)
        self.assertEqual(result.getpixel((40, 40))[3], 255)
        self.assertEqual(response.headers["cache-control"], "no-store")

    def test_original_is_not_mutated(self):
        image = fixture()
        before = image.tobytes()
        server.remove_solid(image)
        self.assertEqual(image.tobytes(), before)

    def test_corrupt_and_svg_rejected(self):
        for value in ("data:image/png;base64,YWJj", "data:image/svg+xml;base64,YWJj", None):
            response = self.client.post("/api/remove-background", json={"image": value, "mode": "solid"})
            self.assertEqual(response.status_code, 400)

    def test_actual_mime_mismatch(self):
        response = self.client.post("/api/remove-background", json={"image": self.image.replace("image/png", "image/jpeg"), "mode": "solid"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"]["code"], "MIME_MISMATCH")

    def test_file_limit(self):
        response = self.client.post("/api/remove-background", json={"image": "x" * (server.FILE_LIMIT * 4 // 3 + 101), "mode": "solid"})
        self.assertEqual(response.status_code, 413)

    def test_pixel_limit(self):
        image = Image.new("RGB", (4001, 4000), "white")
        response = self.client.post("/api/remove-background", json={"image": ai.png_uri(image), "mode": "solid"})
        self.assertEqual(response.status_code, 413)

    def test_invalid_options(self):
        for options in ({"mode": "bad"}, {"tolerance": 101}, {"tolerance": True}):
            response = self.client.post("/api/remove-background", json={"image": self.image, **options})
            self.assertEqual(response.status_code, 400)

    def test_origin_and_host_protection(self):
        payload = {"image": self.image, "mode": "solid"}
        self.assertEqual(self.client.post("/api/remove-background", json=payload, headers={"Origin": "https://evil.example"}).status_code, 403)
        self.assertEqual(self.client.get("/api/status", headers={"Host": "evil.example"}).status_code, 403)
        self.assertEqual(self.client.post("/api/remove-background", json=payload, headers={"Origin": "http://testserver"}).status_code, 200)

    def test_bad_json(self):
        self.assertEqual(self.client.post("/api/try-on", content="{", headers={"Content-Type": "application/json"}).status_code, 400)
        self.assertEqual(self.client.post("/api/try-on", json=[]).status_code, 400)

    def test_body_limit_applies_before_decoding(self):
        with patch.object(server, "BODY_LIMIT", 32):
            response = self.client.post("/api/try-on", json={"padding": "x" * 100})
        self.assertEqual(response.status_code, 413)

    def test_subject_failure_keeps_lock_recoverable(self):
        with patch("rembg.new_session", side_effect=RuntimeError("synthetic model failure")):
            with patch.object(server, "REMBG_SESSION", None):
                response = self.client.post("/api/remove-background", json={"image": self.image, "mode": "subject"})
        self.assertEqual(response.status_code, 503)
        self.assertFalse(server.BG_LOCK.locked())
        self.assertNotIn("synthetic model failure", response.text)

    def test_revision_and_consent_validation(self):
        payload = {"personImage": self.image, "garmentImage": self.image, "designRevision": -1}
        self.assertEqual(self.client.post("/api/try-on", json=payload).status_code, 400)
        payload["designRevision"] = True
        self.assertEqual(self.client.post("/api/try-on", json=payload).status_code, 400)

    def test_injected_ai_contract_returns_revision(self):
        with patch.object(ai, "generate", return_value=(self.image, "openai")) as fake:
            response = self.client.post("/api/try-on", json={"personImage": self.image, "garmentImage": self.image, "designRevision": 7})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["designRevision"], 7)
            self.assertEqual(response.json()["image"], self.image)
            self.assertIsInstance(fake.call_args.args[0], Image.Image)

    def test_busy_does_not_call_engine(self):
        server.AI_LOCK.acquire()
        try:
            with patch.object(ai, "generate") as fake:
                response = self.client.post("/api/try-on", json={"personImage": self.image, "garmentImage": self.image, "designRevision": 1})
                self.assertEqual(response.status_code, 429)
                fake.assert_not_called()
        finally:
            server.AI_LOCK.release()

    def test_unavailable_engine_does_not_fake_success(self):
        with patch.object(ai, "generate", side_effect=ai.AIError(503, "AI_UNAVAILABLE", "AI chưa sẵn sàng.")):
            response = self.client.post("/api/try-on", json={"personImage": self.image, "garmentImage": self.image, "designRevision": 1})
            self.assertEqual(response.status_code, 503)
            self.assertNotIn("image", response.json())
            self.assertFalse(server.AI_LOCK.locked())

    def test_openai_requires_consent(self):
        with patch.object(ai, "api_key", return_value="synthetic-test-only"):
            with self.assertRaises(ai.AIError) as caught:
                ai.hosted_tryon(fixture(), fixture(), False)
        self.assertEqual(caught.exception.status, 403)

    def test_openai_edit_transport_and_secret_boundary(self):
        calls = []
        def transport(request):
            calls.append(request)
            return httpx.Response(200, json={"data": [{"b64_json": self.image.split(",")[1]}]})
        with patch.object(ai, "api_key", return_value="synthetic-test-only"):
            with httpx.Client(transport=httpx.MockTransport(transport)) as client:
                output = ai.hosted_tryon(fixture(), fixture(), True, client)
            response = self.client.get("/api/status")
        self.assertTrue(output.startswith("data:image/png;base64,"))
        self.assertEqual(str(calls[0].url), "https://api.openai.com/v1/images/edits")
        self.assertEqual(calls[0].content.count(b'name="image[]"'), 2)
        self.assertNotIn("synthetic-test-only", response.text)
        self.assertEqual(response.json()["tryOn"]["engine"], "openai")
        self.assertEqual(self.client.get("/.env").status_code, 404)

    def test_openai_error_is_sanitized(self):
        with patch.object(ai, "api_key", return_value="synthetic-test-only"):
            with httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(401, json={"error": "private-debug-data"}))) as client:
                with self.assertRaises(ai.AIError) as caught:
                    ai.hosted_tryon(fixture(), fixture(), True, client)
        self.assertNotIn("private-debug-data", caught.exception.message)

    def test_missing_key_blocks_network(self):
        with patch.object(ai, "api_key", return_value=""):
            with self.assertRaises(ai.AIError) as caught:
                ai.hosted_tryon(fixture(), fixture(), True)
        self.assertEqual(caught.exception.status, 503)

if __name__ == "__main__":
    unittest.main()
