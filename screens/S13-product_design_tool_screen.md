# Screen Spec: S13 Product Design Tool Screen

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S13` |
| Screen name | Product Design Tool Screen |
| Actor | Customer |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-05.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S13-product_design_tool_screen.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Allow customers to customize product attributes, upload images, preview design, and save designs.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S13](img/S13-product_design_tool_screen.png)

<!-- The image is the visual contract: spacing, grouping, and hierarchy. The tables below are the behavioural contract. -->

## 3. Element inventory

<!-- Walk the mockup top to bottom, left to right. Every visible element gets a stable name. -->

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Shipping promotion banner | Text | Static: For free shipping on orders over $100 and more use code FREESHIPPINGYAY | No | Not applicable — display only |
| 2 | Header logo | Image | Static logo placeholder | No | Not applicable — display only |
| 3 | Catalog navigation | Button | Static: CATALOG | No | Not applicable — display only |
| 4 | About Dony navigation | Button | Static: ABOUT DONY | No | Not applicable — display only |
| 5 | My Design navigation | Button | Static: MY DESIGN | No | Not applicable — display only |
| 6 | My Order navigation | Button | Static: MY ORDER | No | Not applicable — display only |
| 7 | Contact Us navigation | Button | Static: CONTACT US | No | Not applicable — display only |
| 8 | Notification bell | Button | Bell icon | No | Not applicable — display only |
| 9 | Account icon | Button | Account icon | No | Not applicable — display only |
| 10 | Upload tool | Button | Upload icon and label | No | Not applicable — display only |
| 11 | Add Text tool | Button | T icon and label | No | Not applicable — display only |
| 12 | My Library tool | Button | Folder icon and label | No | Not applicable — display only |
| 13 | Graphics tool | Button | Shapes icon and label | No | Not applicable — display only |
| 14 | Templates tool | Button | Drawing icon and label | No | Not applicable — display only |
| 15 | New upload heading | Header | Static: New upload | No | Not applicable — display only |
| 16 | My Device upload button | Button | Static: My Device | No | Not applicable — display only |
| 17 | Print file requirements | List | JPG, PNG, SVG; max 100 MiB JPG/PNG or 20 MiB SVG; print area 4494 × 5097 px (300 DPI); max resolution 30000 × 30000 px | No | Not applicable — display only |
| 18 | Edit tab | Button | Static: Edit | No | Not applicable — display only |
| 19 | Preview tab | Button | Static: Preview | No | Not applicable — display only |
| 20 | Product design canvas | Image | interactive_canvas_3d_configurator_ui (F-DES-001); T-shirt with print area | No | Not applicable — display only |
| 21 | Frontside button | Button | Static: Frontside | No | Not applicable — display only |
| 22 | Backside button | Button | Static: Backside | No | Not applicable — display only |
| 23 | Zoom out | Button | Minus icon | No | Not applicable — display only |
| 24 | Zoom percentage | Button | Static: 21% | No | Not applicable — display only |
| 25 | Zoom in | Button | Plus icon | No | Not applicable — display only |
| 26 | Pan tool | Button | Hand icon | No | Not applicable — display only |
| 27 | Save product button | Button | Static: Save product | No | Not applicable — display only |
| 28 | Zalo contact button | Button | Static: Zalo | No | Not applicable — display only |
| 29 | Telephone contact button | Button | Static: Tel | No | Not applicable — display only |
| 30 | Footer contact heading | Text | Static: Contact Information | No | Not applicable — display only |
| 31 | Company name | Text | Static: DONY Garment Manufacturing Co., Ltd. | No | Not applicable — display only |
| 32 | Tax code | Text | Static: 0315676786 | No | Not applicable — display only |
| 33 | Factory and office address | Text | Static address printed in mockup | No | Not applicable — display only |
| 34 | Phone numbers | Text | Static phone numbers printed in mockup | No | Not applicable — display only |
| 35 | Email addresses | Text | Static email addresses printed in mockup | No | Not applicable — display only |
| 36 | Footer DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 37 | Footer Facebook icon | Button | Facebook icon | No | Not applicable — display only |
| 38 | Footer X icon | Button | X icon | No | Not applicable — display only |
| 39 | Footer LinkedIn icon | Button | LinkedIn icon | No | Not applicable — display only |
| 40 | Footer YouTube icon | Button | YouTube icon | No | Not applicable — display only |
| 41 | Footer TikTok icon | Button | TikTok icon | No | Not applicable — display only |
| 42 | Footer certification badge | Image | Green certification badge | No | Not applicable — display only |
| 43 | Footer policy heading | Text | Static: Information - Policies | No | Not applicable — display only |
| 44 | Company profile link | Button | Static: DONY Garment Manufacturing Company Profile | No | Not applicable — display only |
| 45 | Quality policy link | Button | Static: Quality Policy | No | Not applicable — display only |
| 46 | Warranty policy link | Button | Static: Warranty Policy | No | Not applicable — display only |
| 47 | Delivery and return policy link | Button | Static: Delivery & Return Policy | No | Not applicable — display only |
| 48 | Second warranty policy link | Button | Static: Warranty Policy (repeated in mockup) | No | Not applicable — display only |
| 49 | Shipping policy link | Button | Static: Shipping Policy | No | Not applicable — display only |
| 50 | Payment methods link | Button | Static: Payment Methods | No | Not applicable — display only |
| 51 | Business areas link | Button | Static: Business Areas | No | Not applicable — display only |
| 52 | FAQ link | Button | Static: Frequently Asked Questions (FAQ) | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Upload panel, edit tab, front-side canvas. | Open S13 |
| Empty (no data) | Canvas without uploaded art, as shown. | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: image upload/preview/save loading treatment] | Data request or submit in progress |
| Error | [NEEDS CLARIFICATION: invalid upload or save error treatment] | Data request or submit fails |
| Success / confirmation | F-DES-003 saves design; confirmation and navigation [NEEDS CLARIFICATION]. | Successful relevant action |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Header logo | tap | Open home page | S01 |
| 2 | Catalog navigation | tap | Open product catalog | S08 |
| 3 | About Dony navigation | tap | [NEEDS CLARIFICATION: destination not in Screen List] | stays |
| 4 | My Design navigation | tap | Open saved designs | S17 |
| 5 | My Order navigation | tap | Open customer orders | S26 |
| 6 | Contact Us navigation | tap | [NEEDS CLARIFICATION: destination not in Screen List] | stays |
| 7 | Notification bell | tap | Open notification panel | S38 |
| 8 | Account icon | tap | Open user profile | S06 |
| 9 | Upload tool | tap | Select design tool; exact panel behavior [NEEDS CLARIFICATION] | stays |
| 10 | Add Text tool | tap | Select design tool; exact panel behavior [NEEDS CLARIFICATION] | stays |
| 11 | My Library tool | tap | Select design tool; exact panel behavior [NEEDS CLARIFICATION] | stays |
| 12 | Graphics tool | tap | Select design tool; exact panel behavior [NEEDS CLARIFICATION] | stays |
| 13 | Templates tool | tap | Select design tool; exact panel behavior [NEEDS CLARIFICATION] | stays |
| 14 | My Device upload button | tap | Choose image file; validate stated file constraints | stays |
| 15 | Edit tab | tap | Show editing view | stays |
| 16 | Preview tab | tap | F-DES-002 generates rendered_image_model | stays |
| 17 | Product design canvas | drag/tap | [NEEDS CLARIFICATION: canvas gestures and editable properties] | stays |
| 18 | Frontside button | tap | Show front side | stays |
| 19 | Backside button | tap | Show back side | stays |
| 20 | Zoom out | tap | Reduce displayed zoom | stays |
| 21 | Zoom percentage | tap | [NEEDS CLARIFICATION: zoom selector behavior] | stays |
| 22 | Zoom in | tap | Increase displayed zoom | stays |
| 23 | Pan tool | tap | Select pan mode | stays |
| 24 | Save product button | tap | F-DES-003 saves configuration_json and returns saved_design_id; destination [NEEDS CLARIFICATION] | stays |
| 25 | Zalo contact button | tap | [NEEDS CLARIFICATION: contact destination] | stays |
| 26 | Telephone contact button | tap | [NEEDS CLARIFICATION: dial behavior] | stays |
| 27 | Footer Facebook icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 28 | Footer X icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 29 | Footer LinkedIn icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 30 | Footer YouTube icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 31 | Footer TikTok icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 32 | Company profile link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 33 | Quality policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 34 | Warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 35 | Delivery and return policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 36 | Second warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 37 | Shipping policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 38 | Payment methods link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 39 | Business areas link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 40 | FAQ link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Upload requirements are printed in the mockup. | Mockup |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-DES-001 [NEEDS CLARIFICATION: module spec unavailable] | Display a visual design interface allowing customization of colors and materials. |
| F-DES-002 [NEEDS CLARIFICATION: module spec unavailable] | Check compatibility rules and generate a real-time preview image of the product. |
| F-DES-003 [NEEDS CLARIFICATION: module spec unavailable] | Save the customer's custom design configuration into the database. |

## 8. Responsive and accessibility notes

- Smallest supported width: [NEEDS CLARIFICATION: not specified in sources.]

- What collapses or stacks on a narrow screen: [NEEDS CLARIFICATION: no narrow-screen mockup or rule provided.]

- Text that must remain readable (contrast, minimum size): [NEEDS CLARIFICATION: no numeric accessibility criteria provided.]

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | [NEEDS CLARIFICATION: Screen List does not provide Must / Should / Could priority.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 2 | [NEEDS CLARIFICATION: module spec spec-MFG-05.md is not present in project.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 3 | [NEEDS CLARIFICATION: smallest supported width, narrow layout, and accessibility minimums are not specified.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 4 | [NEEDS CLARIFICATION: How are colors and materials customized? Function List mentions them, but no controls are visible.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 5 | [NEEDS CLARIFICATION: Is Save product intended to save a design rather than a product?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 6 | [NEEDS CLARIFICATION: mockup file uses a descriptive suffix; template assumes img/<SCREEN-ID>.png.] | [NEEDS CLARIFICATION: impact not assessed] | Open |

---

## Completion checklist

- [ ] The mockup is a separate cropped image file, named with the Screen ID. [NEEDS CLARIFICATION: actual image filenames include descriptive suffixes.]

- [x] Every visible element in the mockup appears in the element inventory.

- [x] Every input element has a validation rule or an explicit clarification.

- [x] All five states are filled in, or marked not applicable with a reason.

- [x] Every navigation target is an existing Screen ID or "stays".

- [ ] Every element that displays data names the field it displays, matching the module spec. [NEEDS CLARIFICATION: module specs and several field schemas unavailable.]

---

Template source: DBIZ3, VJCBI College - FTU, Session 4. Built on the DBIZ2 Screen Design structure (Screen List and Screen Layout), per DBIZ3 Syllabus v3.
