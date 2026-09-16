# Screen Spec: S09 Product Detail Screen

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S09` |
| Screen name | Product Detail Screen |
| Actor | Guest |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-04.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S09-product_detail_screen.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Display detailed product information and entry points to product design or order creation.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S09](img/S09-product_detail_screen.png)

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
| 10 | Breadcrumb Home | Button | Static: Home | No | Not applicable — display only |
| 11 | Breadcrumb category | Button | Static: Men’s Clothing | No | Not applicable — display only |
| 12 | Breadcrumb product type | Button | Static: T-Shirts | No | Not applicable — display only |
| 13 | Breadcrumb product | Text | Static: Garment-Dyed T-shirt | No | Not applicable — display only |
| 14 | Main product image | Image | full_product_details image (F-PROD-002) | No | Not applicable — display only |
| 15 | Thumbnail 1 | Image | full_product_details image 1 | No | Not applicable — display only |
| 16 | Thumbnail 2 | Image | full_product_details image 2 | No | Not applicable — display only |
| 17 | Thumbnail 3 | Image | full_product_details image 3 | No | Not applicable — display only |
| 18 | Thumbnail 4 | Image | full_product_details image 4 | No | Not applicable — display only |
| 19 | Product name | Header | full_product_details.name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 20 | Product specification bullets | List | SKU T001; fabric; fit; cotton; colors; label from full_product_details (F-PROD-002) | No | Not applicable — display only |
| 21 | Start designing button | Button | Static: Start designing | No | Not applicable — display only |
| 22 | Request Design Service button | Button | Static: Request Design Service | No | Not applicable — display only |
| 23 | About heading | Header | Static: About | No | Not applicable — display only |
| 24 | About description | Text | full_product_details.description [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 25 | Key features heading | Header | Static: Key features | No | Not applicable — display only |
| 26 | Key feature 1 | List | Icon, title, description; feature 1 | No | Not applicable — display only |
| 27 | Key feature 2 | List | Icon, title, description; feature 2 | No | Not applicable — display only |
| 28 | Key feature 3 | List | Icon, title, description; feature 3 | No | Not applicable — display only |
| 29 | Key feature 4 | List | Icon, title, description; feature 4 | No | Not applicable — display only |
| 30 | Care instructions heading | Header | Static: Care instructions | No | Not applicable — display only |
| 31 | Care icons | List | Five care icons | No | Not applicable — display only |
| 32 | Care description | Text | Static care copy | No | Not applicable — display only |
| 33 | Size guide heading | Header | Static: Size guide | No | Not applicable — display only |
| 34 | Size guide table | List | S through 4XL; width, length, sleeve length, tolerance values | No | Not applicable — display only |
| 35 | You may like heading | Header | Static: You may like | No | Not applicable — display only |
| 36 | Recommended product 1 | List | Image and name; product 1 | No | Not applicable — display only |
| 37 | Recommended product 2 | List | Image and name; product 2 | No | Not applicable — display only |
| 38 | Recommended product 3 | List | Image and name; product 3 | No | Not applicable — display only |
| 39 | Recommended product 4 | List | Image and name; product 4 | No | Not applicable — display only |
| 40 | Recommended next arrow | Button | Right arrow | No | Not applicable — display only |
| 41 | Zalo contact button | Button | Static: Zalo | No | Not applicable — display only |
| 42 | Telephone contact button | Button | Static: Tel | No | Not applicable — display only |
| 43 | Footer contact heading | Text | Static: Contact Information | No | Not applicable — display only |
| 44 | Company name | Text | Static: DONY Garment Manufacturing Co., Ltd. | No | Not applicable — display only |
| 45 | Tax code | Text | Static: 0315676786 | No | Not applicable — display only |
| 46 | Factory and office address | Text | Static address printed in mockup | No | Not applicable — display only |
| 47 | Phone numbers | Text | Static phone numbers printed in mockup | No | Not applicable — display only |
| 48 | Email addresses | Text | Static email addresses printed in mockup | No | Not applicable — display only |
| 49 | Footer DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 50 | Footer Facebook icon | Button | Facebook icon | No | Not applicable — display only |
| 51 | Footer X icon | Button | X icon | No | Not applicable — display only |
| 52 | Footer LinkedIn icon | Button | LinkedIn icon | No | Not applicable — display only |
| 53 | Footer YouTube icon | Button | YouTube icon | No | Not applicable — display only |
| 54 | Footer TikTok icon | Button | TikTok icon | No | Not applicable — display only |
| 55 | Footer certification badge | Image | Green certification badge | No | Not applicable — display only |
| 56 | Footer policy heading | Text | Static: Information - Policies | No | Not applicable — display only |
| 57 | Company profile link | Button | Static: DONY Garment Manufacturing Company Profile | No | Not applicable — display only |
| 58 | Quality policy link | Button | Static: Quality Policy | No | Not applicable — display only |
| 59 | Warranty policy link | Button | Static: Warranty Policy | No | Not applicable — display only |
| 60 | Delivery and return policy link | Button | Static: Delivery & Return Policy | No | Not applicable — display only |
| 61 | Second warranty policy link | Button | Static: Warranty Policy (repeated in mockup) | No | Not applicable — display only |
| 62 | Shipping policy link | Button | Static: Shipping Policy | No | Not applicable — display only |
| 63 | Payment methods link | Button | Static: Payment Methods | No | Not applicable — display only |
| 64 | Business areas link | Button | Static: Business Areas | No | Not applicable — display only |
| 65 | FAQ link | Button | Static: Frequently Asked Questions (FAQ) | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Garment-Dyed T-shirt detail as shown. | Open S09 |
| Empty (no data) | [NEEDS CLARIFICATION: missing product display] | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: product detail loading treatment] | Data request or submit in progress |
| Error | [NEEDS CLARIFICATION: unavailable product error treatment] | Data request or submit fails |
| Success / confirmation | Not applicable — this screen has no save or submit confirmation. | Successful relevant action |

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
| 9 | Breadcrumb Home | tap | Open home | S01 |
| 10 | Breadcrumb category | tap | Open catalog category | S08 |
| 11 | Breadcrumb product type | tap | Open catalog product type | S08 |
| 12 | Thumbnail 1 | tap | Change main product image | stays |
| 13 | Thumbnail 2 | tap | Change main product image | stays |
| 14 | Thumbnail 3 | tap | Change main product image | stays |
| 15 | Thumbnail 4 | tap | Change main product image | stays |
| 16 | Start designing button | tap | Open design workspace for base_product_id | S13 |
| 17 | Request Design Service button | tap | Open design service form | S15 |
| 18 | Recommended product 1 | tap | Open selected product | S09 |
| 19 | Recommended product 2 | tap | Open selected product | S09 |
| 20 | Recommended product 3 | tap | Open selected product | S09 |
| 21 | Recommended product 4 | tap | Open selected product | S09 |
| 22 | Recommended next arrow | tap | Show next recommendations | stays |
| 23 | Zalo contact button | tap | [NEEDS CLARIFICATION: contact destination] | stays |
| 24 | Telephone contact button | tap | [NEEDS CLARIFICATION: dial behavior] | stays |
| 25 | Footer Facebook icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 26 | Footer X icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 27 | Footer LinkedIn icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 28 | Footer YouTube icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 29 | Footer TikTok icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 30 | Company profile link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 31 | Quality policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 32 | Warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 33 | Delivery and return policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 34 | Second warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 35 | Shipping policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 36 | Payment methods link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 37 | Business areas link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 38 | FAQ link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | The mockup offers Start designing and Request Design Service. | Mockup |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-PROD-002 [NEEDS CLARIFICATION: module spec unavailable] | Display detailed product information, technical specifications, and available options. |
| F-DES-001 [NEEDS CLARIFICATION: module spec unavailable] | Display a visual design interface allowing customization of colors and materials. |
| F-DES-005 [NEEDS CLARIFICATION: module spec unavailable] | Display a form for customers to enter special design service requirements. |

## 8. Responsive and accessibility notes

- Smallest supported width: [NEEDS CLARIFICATION: not specified in sources.]

- What collapses or stacks on a narrow screen: [NEEDS CLARIFICATION: no narrow-screen mockup or rule provided.]

- Text that must remain readable (contrast, minimum size): [NEEDS CLARIFICATION: no numeric accessibility criteria provided.]

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | [NEEDS CLARIFICATION: Screen List does not provide Must / Should / Could priority.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 2 | [NEEDS CLARIFICATION: module spec spec-MFG-04.md is not present in project.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 3 | [NEEDS CLARIFICATION: smallest supported width, narrow layout, and accessibility minimums are not specified.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 4 | [NEEDS CLARIFICATION: Screen Overview mentions an order creation entry point, but none is visible in this mockup.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 5 | [NEEDS CLARIFICATION: mockup file uses a descriptive suffix; template assumes img/<SCREEN-ID>.png.] | [NEEDS CLARIFICATION: impact not assessed] | Open |

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
