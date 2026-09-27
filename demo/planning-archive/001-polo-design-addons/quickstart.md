# Quickstart and Validation

From repository root, PowerShell:

```powershell
uv venv --python 3.12 demo/polo/.venv
uv pip install --python demo/polo/.venv/Scripts/python.exe -r demo/polo/requirements.txt
demo/polo/.venv/Scripts/python.exe demo/polo/server.py
```

Open http://127.0.0.1:8765 . Model caches contain weights only. See demo/polo/README.md for optional local real AI setup.

## Scenarios

1. Upload/resize/place front artwork, change colour, select six mockups; upload distinct back artwork and verify surfaces.
2. Remove subject/solid background -> compare -> cancel/apply -> restore; placement unchanged.
3. Inspect male/female/child presets; upload real photo and generate with a configured engine. Unavailable never appears as success.
4. Change input/end session while processing; stale results cannot appear. Reload; uploads/results gone.
5. Validate 390px and desktop layouts, keyboard controls and errors.

```powershell
demo/polo/.venv/Scripts/python.exe -m unittest discover -s demo/polo/tests -v
```

Automated checks include actual decoding/limits, privacy headers, solid-background processing and injected-provider transitions. A mocked AI test does not satisfy SC-004. tasks.md records measured readiness and verification limits.
