# HTTP Contract

API responses: Cache-Control no-store. Bind 127.0.0.1 only. Check Origin/Host for mutations. JSON body <=29 MiB; each decoded image <=10 MiB, <=16 million pixels. Validate actual PNG/JPEG/WebP bytes, not only URI prefix. Never log payloads.

## GET /api/status

Returns `{backgroundRemoval: boolean, tryOn: {engine: 'local'|'fashn'|'unavailable', available: boolean, notice: string}}`. Readiness does not assert successful inference.

## POST /api/remove-background

Input `{image: dataURI, mode: 'subject'|'solid', tolerance: integer 5..100}` (defaults subject/35). Output `{image: pngDataURI}`. Solid mode removes border-connected matching pixels; subject uses local rembg.

## POST /api/try-on

Input `{personImage: dataURI, garmentImage: dataURI, designRevision: integer>=0, externalConsent: boolean=false}`. Output `{image: pngDataURI, designRevision, engine}`. One sample, complete flat-lay polo. Browser rejects stale design/person tokens. External engine requires key and consent; provider retention is explained independently.

## Errors

`{error:{code,message}}`: safe Vietnamese message; 400 invalid fields/image; 413 body/file/pixel limit; 403 origin/consent; 429 busy; 503 unavailable; 504 timeout; 502 processing/provider failure. Never expose raw upstream payloads, paths or secrets.
