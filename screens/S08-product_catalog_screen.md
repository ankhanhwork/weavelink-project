# Screen Spec: S08 Product Catalog Screen

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S08` |
| Screen name | Product Catalog Screen |
| Actor | Guest |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-04.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S08-product_catalog_screen.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Display all available products with browsing and search functionality.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S08](img/S08-product_catalog_screen.png)

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
| 10 | Catalog hero image | Image | Wide placeholder | No | Not applicable — display only |
| 11 | Filter heading | Header | Static: Filter | No | Not applicable — display only |
| 12 | T-Shirt category button | Button | Static: T-Shirt | No | Not applicable — display only |
| 13 | Uniform category button | Button | Static: Uniform | No | Not applicable — display only |
| 14 | Jacket category button | Button | Static: Jacket | No | Not applicable — display only |
| 15 | Workwear category button | Button | Static: Workwear | No | Not applicable — display only |
| 16 | Search product input | Input | search_keyword (F-PROD-003) | No | [NEEDS CLARIFICATION: search rules] |
| 17 | Price filter | Button | Static: Price | No | Not applicable — display only |
| 18 | Size filter | Button | Static: Size | No | Not applicable — display only |
| 19 | Color filter | Button | Static: Color | No | Not applicable — display only |
| 20 | Type filter | Button | Static: Type | No | Not applicable — display only |
| 21 | Long Sleeves checkbox | Toggle | filter_attributes.type=Long Sleeves (F-PROD-003) | No | Not applicable — option toggle |
| 22 | Sweatshirt checkbox | Toggle | filter_attributes.type=Sweatshirt (F-PROD-003) | No | Not applicable — option toggle |
| 23 | Product 1 image | Image | filtered_product_list[1].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 24 | Product 1 name | Text | filtered_product_list[1].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 25 | Product 1 price | Text | filtered_product_list[1].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 26 | Product 2 image | Image | filtered_product_list[2].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 27 | Product 2 name | Text | filtered_product_list[2].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 28 | Product 2 price | Text | filtered_product_list[2].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 29 | Product 3 image | Image | filtered_product_list[3].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 30 | Product 3 name | Text | filtered_product_list[3].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 31 | Product 3 price | Text | filtered_product_list[3].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 32 | Product 4 image | Image | filtered_product_list[4].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 33 | Product 4 name | Text | filtered_product_list[4].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 34 | Product 4 price | Text | filtered_product_list[4].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 35 | Product 5 image | Image | filtered_product_list[5].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 36 | Product 5 name | Text | filtered_product_list[5].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 37 | Product 5 price | Text | filtered_product_list[5].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 38 | Product 6 image | Image | filtered_product_list[6].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 39 | Product 6 name | Text | filtered_product_list[6].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 40 | Product 6 price | Text | filtered_product_list[6].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 41 | Product 7 image | Image | filtered_product_list[7].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 42 | Product 7 name | Text | filtered_product_list[7].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 43 | Product 7 price | Text | filtered_product_list[7].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 44 | Product 8 image | Image | filtered_product_list[8].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 45 | Product 8 name | Text | filtered_product_list[8].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 46 | Product 8 price | Text | filtered_product_list[8].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 47 | Product 9 image | Image | filtered_product_list[9].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 48 | Product 9 name | Text | filtered_product_list[9].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 49 | Product 9 price | Text | filtered_product_list[9].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 50 | Product 10 image | Image | filtered_product_list[10].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 51 | Product 10 name | Text | filtered_product_list[10].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 52 | Product 10 price | Text | filtered_product_list[10].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 53 | Product 11 image | Image | filtered_product_list[11].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 54 | Product 11 name | Text | filtered_product_list[11].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 55 | Product 11 price | Text | filtered_product_list[11].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 56 | Product 12 image | Image | filtered_product_list[12].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 57 | Product 12 name | Text | filtered_product_list[12].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 58 | Product 12 price | Text | filtered_product_list[12].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 59 | Product 13 image | Image | filtered_product_list[13].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 60 | Product 13 name | Text | filtered_product_list[13].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 61 | Product 13 price | Text | filtered_product_list[13].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 62 | Product 14 image | Image | filtered_product_list[14].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 63 | Product 14 name | Text | filtered_product_list[14].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 64 | Product 14 price | Text | filtered_product_list[14].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 65 | Product 15 image | Image | filtered_product_list[15].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 66 | Product 15 name | Text | filtered_product_list[15].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 67 | Product 15 price | Text | filtered_product_list[15].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 68 | Product 16 image | Image | filtered_product_list[16].image [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 69 | Product 16 name | Text | filtered_product_list[16].name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 70 | Product 16 price | Text | filtered_product_list[16].price [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 71 | Bestsellers heading | Header | Static: Try our bestsellers | No | Not applicable — display only |
| 72 | Bestsellers description | Text | Static paragraph | No | Not applicable — display only |
| 73 | Bestseller card 1 | List | Product image, $10, name, subtitle | No | Not applicable — display only |
| 74 | Bestseller card 2 | List | Product image, $12, name, subtitle | No | Not applicable — display only |
| 75 | Bestseller next arrow | Button | Right arrow | No | Not applicable — display only |
| 76 | Zalo contact button | Button | Static: Zalo | No | Not applicable — display only |
| 77 | Telephone contact button | Button | Static: Tel | No | Not applicable — display only |
| 78 | Footer contact heading | Text | Static: Contact Information | No | Not applicable — display only |
| 79 | Company name | Text | Static: DONY Garment Manufacturing Co., Ltd. | No | Not applicable — display only |
| 80 | Tax code | Text | Static: 0315676786 | No | Not applicable — display only |
| 81 | Factory and office address | Text | Static address printed in mockup | No | Not applicable — display only |
| 82 | Phone numbers | Text | Static phone numbers printed in mockup | No | Not applicable — display only |
| 83 | Email addresses | Text | Static email addresses printed in mockup | No | Not applicable — display only |
| 84 | Footer DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 85 | Footer Facebook icon | Button | Facebook icon | No | Not applicable — display only |
| 86 | Footer X icon | Button | X icon | No | Not applicable — display only |
| 87 | Footer LinkedIn icon | Button | LinkedIn icon | No | Not applicable — display only |
| 88 | Footer YouTube icon | Button | YouTube icon | No | Not applicable — display only |
| 89 | Footer TikTok icon | Button | TikTok icon | No | Not applicable — display only |
| 90 | Footer certification badge | Image | Green certification badge | No | Not applicable — display only |
| 91 | Footer policy heading | Text | Static: Information - Policies | No | Not applicable — display only |
| 92 | Company profile link | Button | Static: DONY Garment Manufacturing Company Profile | No | Not applicable — display only |
| 93 | Quality policy link | Button | Static: Quality Policy | No | Not applicable — display only |
| 94 | Warranty policy link | Button | Static: Warranty Policy | No | Not applicable — display only |
| 95 | Delivery and return policy link | Button | Static: Delivery & Return Policy | No | Not applicable — display only |
| 96 | Second warranty policy link | Button | Static: Warranty Policy (repeated in mockup) | No | Not applicable — display only |
| 97 | Shipping policy link | Button | Static: Shipping Policy | No | Not applicable — display only |
| 98 | Payment methods link | Button | Static: Payment Methods | No | Not applicable — display only |
| 99 | Business areas link | Button | Static: Business Areas | No | Not applicable — display only |
| 100 | FAQ link | Button | Static: Frequently Asked Questions (FAQ) | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Product grid with 16 visible cards and filters. | Open S08 |
| Empty (no data) | [NEEDS CLARIFICATION: empty search or catalog message] | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: catalog loading treatment] | Data request or submit in progress |
| Error | [NEEDS CLARIFICATION: catalog fetch error treatment] | Data request or submit fails |
| Success / confirmation | Not applicable — browsing and filtering show results without confirmation. | Successful relevant action |

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
| 9 | T-Shirt category button | tap | Apply category_filter; refresh catalog | stays |
| 10 | Uniform category button | tap | Apply category_filter; refresh catalog | stays |
| 11 | Jacket category button | tap | Apply category_filter; refresh catalog | stays |
| 12 | Workwear category button | tap | Apply category_filter; refresh catalog | stays |
| 13 | Search product input | type | Apply search_keyword; show F-PROD-003 filtered_product_list | stays |
| 14 | Price filter | tap | [NEEDS CLARIFICATION: available filter values and response] | stays |
| 15 | Size filter | tap | [NEEDS CLARIFICATION: available filter values and response] | stays |
| 16 | Color filter | tap | [NEEDS CLARIFICATION: available filter values and response] | stays |
| 17 | Type filter | tap | [NEEDS CLARIFICATION: available filter values and response] | stays |
| 18 | Long Sleeves checkbox | tap | Apply filter_attributes | stays |
| 19 | Sweatshirt checkbox | tap | Apply filter_attributes | stays |
| 20 | Product 1 image | tap | Open selected product | S09 |
| 21 | Product 2 image | tap | Open selected product | S09 |
| 22 | Product 3 image | tap | Open selected product | S09 |
| 23 | Product 4 image | tap | Open selected product | S09 |
| 24 | Product 5 image | tap | Open selected product | S09 |
| 25 | Product 6 image | tap | Open selected product | S09 |
| 26 | Product 7 image | tap | Open selected product | S09 |
| 27 | Product 8 image | tap | Open selected product | S09 |
| 28 | Product 9 image | tap | Open selected product | S09 |
| 29 | Product 10 image | tap | Open selected product | S09 |
| 30 | Product 11 image | tap | Open selected product | S09 |
| 31 | Product 12 image | tap | Open selected product | S09 |
| 32 | Product 13 image | tap | Open selected product | S09 |
| 33 | Product 14 image | tap | Open selected product | S09 |
| 34 | Product 15 image | tap | Open selected product | S09 |
| 35 | Product 16 image | tap | Open selected product | S09 |
| 36 | Product 1 name | tap | Open selected product | S09 |
| 37 | Product 2 name | tap | Open selected product | S09 |
| 38 | Product 3 name | tap | Open selected product | S09 |
| 39 | Product 4 name | tap | Open selected product | S09 |
| 40 | Product 5 name | tap | Open selected product | S09 |
| 41 | Product 6 name | tap | Open selected product | S09 |
| 42 | Product 7 name | tap | Open selected product | S09 |
| 43 | Product 8 name | tap | Open selected product | S09 |
| 44 | Product 9 name | tap | Open selected product | S09 |
| 45 | Product 10 name | tap | Open selected product | S09 |
| 46 | Product 11 name | tap | Open selected product | S09 |
| 47 | Product 12 name | tap | Open selected product | S09 |
| 48 | Product 13 name | tap | Open selected product | S09 |
| 49 | Product 14 name | tap | Open selected product | S09 |
| 50 | Product 15 name | tap | Open selected product | S09 |
| 51 | Product 16 name | tap | Open selected product | S09 |
| 52 | Bestseller card 1 | tap | Open selected product | S09 |
| 53 | Bestseller card 2 | tap | Open selected product | S09 |
| 54 | Bestseller next arrow | tap | Show next bestseller | stays |
| 55 | Zalo contact button | tap | [NEEDS CLARIFICATION: contact destination] | stays |
| 56 | Telephone contact button | tap | [NEEDS CLARIFICATION: dial behavior] | stays |
| 57 | Footer Facebook icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 58 | Footer X icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 59 | Footer LinkedIn icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 60 | Footer YouTube icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 61 | Footer TikTok icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 62 | Company profile link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 63 | Quality policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 64 | Warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 65 | Delivery and return policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 66 | Second warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 67 | Shipping policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 68 | Payment methods link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 69 | Business areas link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 70 | FAQ link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | The grid shows image, product name, and price. | Mockup |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-PROD-001 [NEEDS CLARIFICATION: module spec unavailable] | Display the product list in a grid layout with images and basic pricing. |
| F-PROD-003 [NEEDS CLARIFICATION: module spec unavailable] | Display a list of products matching the user's search keywords. |

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
| 4 | [NEEDS CLARIFICATION: Function list requires pagination_controls, but none are visible in this mockup. How is pagination shown?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
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
