# Screen Spec: S22 Create Order Screen

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S22` |
| Screen name | Create Order Screen |
| Actor | Customer |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-06.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S22-create_order_screen.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Allow customer to create an order from a selected design, input size, quantity, and shipping info.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S22](img/S22-create_order_screen.png)

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
| 10 | Back link | Button | Static: Back | No | Not applicable — display only |
| 11 | Make Order heading | Header | Static: Make Order | No | Not applicable — display only |
| 12 | Product image | Image | Selected design/product placeholder from cart_session_data (F-PAY-001) | No | Not applicable — display only |
| 13 | Product name | Header | Selected product name from cart_session_data [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 14 | Product specs | List | SKU, fabric, fit, cotton, colors, label | No | Not applicable — display only |
| 15 | Size guide heading | Header | Static: Size guide | No | Not applicable — display only |
| 16 | Size guide table | List | S through 4XL measurements | No | Not applicable — display only |
| 17 | Select size heading | Header | Static: Select size and quantity | No | Not applicable — display only |
| 18 | Size S label | Text | Static: Size S | No | Not applicable — display only |
| 19 | Size S decrement | Button | Minus icon | No | Not applicable — display only |
| 20 | Size S quantity input | Input | cart_items size S quantity (F-PAY-003) | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: quantity rules] |
| 21 | Size S increment | Button | Plus icon | No | Not applicable — display only |
| 22 | Size M label | Text | Static: Size M | No | Not applicable — display only |
| 23 | Size M decrement | Button | Minus icon | No | Not applicable — display only |
| 24 | Size M quantity input | Input | cart_items size M quantity (F-PAY-003) | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: quantity rules] |
| 25 | Size M increment | Button | Plus icon | No | Not applicable — display only |
| 26 | Size L label | Text | Static: Size L | No | Not applicable — display only |
| 27 | Size L decrement | Button | Minus icon | No | Not applicable — display only |
| 28 | Size L quantity input | Input | cart_items size L quantity (F-PAY-003) | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: quantity rules] |
| 29 | Size L increment | Button | Plus icon | No | Not applicable — display only |
| 30 | Size XL label | Text | Static: Size XL | No | Not applicable — display only |
| 31 | Size XL decrement | Button | Minus icon | No | Not applicable — display only |
| 32 | Size XL quantity input | Input | cart_items size XL quantity (F-PAY-003) | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: quantity rules] |
| 33 | Size XL increment | Button | Plus icon | No | Not applicable — display only |
| 34 | Size 2XL label | Text | Static: Size 2XL | No | Not applicable — display only |
| 35 | Size 2XL decrement | Button | Minus icon | No | Not applicable — display only |
| 36 | Size 2XL quantity input | Input | cart_items size 2XL quantity (F-PAY-003) | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: quantity rules] |
| 37 | Size 2XL increment | Button | Plus icon | No | Not applicable — display only |
| 38 | Size 3XL label | Text | Static: Size 3XL | No | Not applicable — display only |
| 39 | Size 3XL decrement | Button | Minus icon | No | Not applicable — display only |
| 40 | Size 3XL quantity input | Input | cart_items size 3XL quantity (F-PAY-003) | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: quantity rules] |
| 41 | Size 3XL increment | Button | Plus icon | No | Not applicable — display only |
| 42 | Size 4XL label | Text | Static: Size 4XL | No | Not applicable — display only |
| 43 | Size 4XL decrement | Button | Minus icon | No | Not applicable — display only |
| 44 | Size 4XL quantity input | Input | cart_items size 4XL quantity (F-PAY-003) | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: quantity rules] |
| 45 | Size 4XL increment | Button | Plus icon | No | Not applicable — display only |
| 46 | Total items | Text | Sum shown as 100 items; calculation [NEEDS CLARIFICATION] | No | Not applicable — display only |
| 47 | Shipping heading | Header | Static: Shipping Address & Contact Detail | No | Not applicable — display only |
| 48 | Email Address input | Input | shipping_info.email [NEEDS CLARIFICATION: schema] | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: validation rule not specified] |
| 49 | Full Name input | Input | shipping_info.full_name [NEEDS CLARIFICATION: schema] | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: validation rule not specified] |
| 50 | Address input | Input | shipping_info.address [NEEDS CLARIFICATION: schema] | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: validation rule not specified] |
| 51 | City input | Input | shipping_info.city [NEEDS CLARIFICATION: schema] | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: validation rule not specified] |
| 52 | Zip Code input | Input | shipping_info.zip_code [NEEDS CLARIFICATION: schema] | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: validation rule not specified] |
| 53 | Save address button | Button | Static: Save | No | Not applicable — display only |
| 54 | Move to editor button | Button | Static: Move to editor | No | Not applicable — display only |
| 55 | Zalo contact button | Button | Static: Zalo | No | Not applicable — display only |
| 56 | Telephone contact button | Button | Static: Tel | No | Not applicable — display only |
| 57 | Footer contact heading | Text | Static: Contact Information | No | Not applicable — display only |
| 58 | Company name | Text | Static: DONY Garment Manufacturing Co., Ltd. | No | Not applicable — display only |
| 59 | Tax code | Text | Static: 0315676786 | No | Not applicable — display only |
| 60 | Factory and office address | Text | Static address printed in mockup | No | Not applicable — display only |
| 61 | Phone numbers | Text | Static phone numbers printed in mockup | No | Not applicable — display only |
| 62 | Email addresses | Text | Static email addresses printed in mockup | No | Not applicable — display only |
| 63 | Footer DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 64 | Footer Facebook icon | Button | Facebook icon | No | Not applicable — display only |
| 65 | Footer X icon | Button | X icon | No | Not applicable — display only |
| 66 | Footer LinkedIn icon | Button | LinkedIn icon | No | Not applicable — display only |
| 67 | Footer YouTube icon | Button | YouTube icon | No | Not applicable — display only |
| 68 | Footer TikTok icon | Button | TikTok icon | No | Not applicable — display only |
| 69 | Footer certification badge | Image | Green certification badge | No | Not applicable — display only |
| 70 | Footer policy heading | Text | Static: Information - Policies | No | Not applicable — display only |
| 71 | Company profile link | Button | Static: DONY Garment Manufacturing Company Profile | No | Not applicable — display only |
| 72 | Quality policy link | Button | Static: Quality Policy | No | Not applicable — display only |
| 73 | Warranty policy link | Button | Static: Warranty Policy | No | Not applicable — display only |
| 74 | Delivery and return policy link | Button | Static: Delivery & Return Policy | No | Not applicable — display only |
| 75 | Second warranty policy link | Button | Static: Warranty Policy (repeated in mockup) | No | Not applicable — display only |
| 76 | Shipping policy link | Button | Static: Shipping Policy | No | Not applicable — display only |
| 77 | Payment methods link | Button | Static: Payment Methods | No | Not applicable — display only |
| 78 | Business areas link | Button | Static: Business Areas | No | Not applicable — display only |
| 79 | FAQ link | Button | Static: Frequently Asked Questions (FAQ) | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Product, size quantities, and shipping fields pre-filled. | Open S22 |
| Empty (no data) | [NEEDS CLARIFICATION: no selected design or no shipping data] | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: address/save loading treatment] | Data request or submit in progress |
| Error | [NEEDS CLARIFICATION: address/quantity error treatment] | Data request or submit fails |
| Success / confirmation | [NEEDS CLARIFICATION: address saved confirmation] | Successful relevant action |

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
| 9 | Back link | tap | Return to saved designs | S17 |
| 10 | Size S decrement | tap | Decrease quantity [NEEDS CLARIFICATION: limits] | stays |
| 11 | Size M decrement | tap | Decrease quantity [NEEDS CLARIFICATION: limits] | stays |
| 12 | Size L decrement | tap | Decrease quantity [NEEDS CLARIFICATION: limits] | stays |
| 13 | Size XL decrement | tap | Decrease quantity [NEEDS CLARIFICATION: limits] | stays |
| 14 | Size 2XL decrement | tap | Decrease quantity [NEEDS CLARIFICATION: limits] | stays |
| 15 | Size 3XL decrement | tap | Decrease quantity [NEEDS CLARIFICATION: limits] | stays |
| 16 | Size 4XL decrement | tap | Decrease quantity [NEEDS CLARIFICATION: limits] | stays |
| 17 | Size S quantity input | type | Set quantity [NEEDS CLARIFICATION: validation] | stays |
| 18 | Size M quantity input | type | Set quantity [NEEDS CLARIFICATION: validation] | stays |
| 19 | Size L quantity input | type | Set quantity [NEEDS CLARIFICATION: validation] | stays |
| 20 | Size XL quantity input | type | Set quantity [NEEDS CLARIFICATION: validation] | stays |
| 21 | Size 2XL quantity input | type | Set quantity [NEEDS CLARIFICATION: validation] | stays |
| 22 | Size 3XL quantity input | type | Set quantity [NEEDS CLARIFICATION: validation] | stays |
| 23 | Size 4XL quantity input | type | Set quantity [NEEDS CLARIFICATION: validation] | stays |
| 24 | Size S increment | tap | Increase quantity | stays |
| 25 | Size M increment | tap | Increase quantity | stays |
| 26 | Size L increment | tap | Increase quantity | stays |
| 27 | Size XL increment | tap | Increase quantity | stays |
| 28 | Size 2XL increment | tap | Increase quantity | stays |
| 29 | Size 3XL increment | tap | Increase quantity | stays |
| 30 | Size 4XL increment | tap | Increase quantity | stays |
| 31 | Email Address input | type | Update shipping_info | stays |
| 32 | Full Name input | type | Update shipping_info | stays |
| 33 | Address input | type | Update shipping_info | stays |
| 34 | City input | type | Update shipping_info | stays |
| 35 | Zip Code input | type | Update shipping_info | stays |
| 36 | Save address button | tap | Store entered shipping details; persistence [NEEDS CLARIFICATION] | stays |
| 37 | Move to editor button | tap | Proceed to merge choice according to usage flow; label/action mismatch [NEEDS CLARIFICATION] | S23 |
| 38 | Zalo contact button | tap | [NEEDS CLARIFICATION: contact destination] | stays |
| 39 | Telephone contact button | tap | [NEEDS CLARIFICATION: dial behavior] | stays |
| 40 | Footer Facebook icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 41 | Footer X icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 42 | Footer LinkedIn icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 43 | Footer YouTube icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 44 | Footer TikTok icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 45 | Company profile link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 46 | Quality policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 47 | Warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 48 | Delivery and return policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 49 | Second warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 50 | Shipping policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 51 | Payment methods link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 52 | Business areas link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 53 | FAQ link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | The screen collects size/quantity and shipping information before order flow continues. | screen-list.md |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-PAY-001 [NEEDS CLARIFICATION: module spec unavailable] | Display shopping cart information and the shipping address entry form. |
| F-PAY-003 [NEEDS CLARIFICATION: module spec unavailable] | Create a new order in the system with an initial status of "Pending". |

## 8. Responsive and accessibility notes

- Smallest supported width: [NEEDS CLARIFICATION: not specified in sources.]

- What collapses or stacks on a narrow screen: [NEEDS CLARIFICATION: no narrow-screen mockup or rule provided.]

- Text that must remain readable (contrast, minimum size): [NEEDS CLARIFICATION: no numeric accessibility criteria provided.]

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | [NEEDS CLARIFICATION: Screen List does not provide Must / Should / Could priority.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 2 | [NEEDS CLARIFICATION: module spec spec-MFG-06.md is not present in project.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 3 | [NEEDS CLARIFICATION: smallest supported width, narrow layout, and accessibility minimums are not specified.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 4 | [NEEDS CLARIFICATION: What does Move to editor do? The usage flow indicates merge choice next.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 5 | [NEEDS CLARIFICATION: What are quantity and shipping field rules?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
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
