# Polo design demo

Run from the repository root:

```powershell
demo/polo/.venv/Scripts/python.exe -X utf8 demo/polo/server.py
```

Open http://127.0.0.1:8765. The server binds to loopback only.

## OpenAI setup (part 03)

Open `docs/env/.env` yourself in a text editor and put your key after `OPENAI_API_KEY=`. Do not paste it into chat, frontend code, screenshots or Git. The user moved the credential file to this location. `.env.example` contains no key and can be committed; `.env` is ignored by Git. Environment `OPENAI_API_KEY` takes precedence. Configuration is read at request time; no restart is needed after entering the key.

Part 03 uses OpenAI `POST /v1/images/edits` with `gpt-image-1`, two PNG references (person first, designed polo second), high input fidelity and medium quality. Account permissions and API credit are required. No local try-on or FASHN fallback remains. Synthetic presets are deterministic previews, not generated API output. Part 01 still has its independent rembg background removal and solid-background option.

The frontend requires explicit consent to transmit both images before generation. Calls can incur charges; no automatic retries are made. Stopping a browser request does not guarantee cancellation or refund of provider processing. Logo lettering and identity may still vary; review the generated image.

## Secret and image boundaries

The key is backend-only and sent only to `https://api.openai.com`; redirects are disabled. Status returns availability only. Provider errors are replaced with safe messages; request bodies and authorization headers are not logged. Only `web/` is publicly served; `.env` is outside it. Do not enable HTTP debug logging.

Git ignore prevents accidental ordinary commits, not access by your Windows account, administrators, malware or an agent allowed to read the file. The demo's AGENTS.md tells agents not to read secret files; this is a behavioral instruction, not an access-control sandbox. Do not share `.env` when sharing the project. For stronger isolation, configure the backend under a separate account/secret manager outside the agent workspace.

Uploads/results remain in application RAM and are discarded on reload/end session. Once sent to OpenAI, provider data policies apply; application session-only storage is not a guarantee of provider session-only retention. See https://developers.openai.com/api/docs/guides/your-data .

## Verification

```powershell
demo/polo/.venv/Scripts/python.exe -X utf8 -m unittest discover -s demo/polo/tests -v
node --test demo/polo/tests/geometry.test.mjs demo/polo/tests/print-surface.test.mjs demo/polo/tests/session.test.mjs
```

Transport tests use synthetic keys and HTTP mocks; they do not make paid calls. Model caches and previously installed local packages are not used by part 03 and have not been purged. This demo is not a production service or a manufacturing export tool.
