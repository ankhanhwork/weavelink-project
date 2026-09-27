# Session Data Model

## Draft and artwork

Draft: colour, fabric (cotton/blend), front/back surface, integer revision, assets and selected ID. Illustrative print area 300 x 400 mm. At most five PNG/JPEG/WebP assets <=10 MiB each. Non-negative X/Y and positive width/height bounds fit the area. Each asset has session ID, original/active data URI and surface/placement. All pixels are RAM-only. Review result changes active pixels only on Apply; restore selects original. View/zoom never changes millimetres.

## Person and result

Person: synthetic preset or uploaded data URI plus input generation token. Result: image, exact draft revision/person token and engine label. Only matching tokens may commit. Changing design clears the result. End session clears all user-image references/review state and invalidates pending requests. Reload starts a synthetic default draft.

## Processing state

Idle -> Processing -> Review (cutout) / Success (try-on) or Error. Busy returns retryable status; absent engine returns Unavailable. Request/Pillow image memory released after response; model weights may remain loaded. No user images in model caches, files or logs.

Front print coordinates include the chest. Shortcuts set wearer-left/right chest positions; coordinates remain in the same 300 x 400 mm domain. View mapping is a calibrated quadrilateral, projected with a homography; pointer input uses the inverse. Fabric changes increment draft revision; End session resets to cotton.
# Surface rendering metadata

Each angled template includes a fixed `surface` 5 x 5 array of normalized image points in physical left-to-right/top-to-bottom order and an `occlusion` polygon over the placket. These are public template metadata, not user data. Artwork retains its original millimetre placement and source pixels. Shaded/warped canvases exist only for the render call; no personalized render cache or persistent image storage is introduced.
