# Screen Spec: S26 Customer Order List Screen

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S26` |
| Screen name | Customer Order List Screen |
| Actor | Customer |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-07.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S26-customer_order_list_screen.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Display all customer orders with current statuses.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S26](img/S26-customer_order_list_screen.png)

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
| 11 | Breadcrumb My Order | Text | Static: My Order | No | Not applicable — display only |
| 12 | My Order heading | Header | Static: My Order | No | Not applicable — display only |
| 13 | Upcoming Orders tab | Button | Static: UPCOMING ORDERS | No | Not applicable — display only |
| 14 | Previous Orders tab | Button | Static: PREVIOUS ORDERS | No | Not applicable — display only |
| 15 | Order 1 ID | Text | list_of_orders[1].order_id [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 16 | Order 1 payment status | Text | list_of_orders[1].payment_status [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 17 | Order 1 total | Text | list_of_orders[1].total [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 18 | Order 1 contract status | Text | list_of_orders[1].contract_status [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 19 | Order 1 estimated arrival | Text | list_of_orders[1].estimated_arrival [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 20 | Order 1 Pay Now button | Button | Static: PAY NOW | No | Not applicable — display only |
| 21 | Order 1 Detail button | Button | Static: DETAIL | No | Not applicable — display only |
| 22 | Order 1 contract button | Button | Static: VIEW CONTRACT | No | Not applicable — display only |
| 23 | Order 1 Track button | Button | Static: TRACK | No | Not applicable — display only |
| 24 | Order 2 ID | Text | list_of_orders[2].order_id [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 25 | Order 2 payment status | Text | list_of_orders[2].payment_status [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 26 | Order 2 total | Text | list_of_orders[2].total [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 27 | Order 2 contract status | Text | list_of_orders[2].contract_status [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 28 | Order 2 estimated arrival | Text | list_of_orders[2].estimated_arrival [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 29 | Order 2 Pay Now button | Button | Static: PAY NOW | No | Not applicable — display only |
| 30 | Order 2 Detail button | Button | Static: DETAIL | No | Not applicable — display only |
| 31 | Order 2 contract button | Button | Static: SIGN NOW | No | Not applicable — display only |
| 32 | Order 2 Track button | Button | Static: TRACK | No | Not applicable — display only |
| 33 | Order 3 ID | Text | list_of_orders[3].order_id [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 34 | Order 3 payment status | Text | list_of_orders[3].payment_status [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 35 | Order 3 total | Text | list_of_orders[3].total [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 36 | Order 3 contract status | Text | list_of_orders[3].contract_status [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 37 | Order 3 estimated arrival | Text | list_of_orders[3].estimated_arrival [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 38 | Order 3 Pay Now button | Button | Static: PAY NOW | No | Not applicable — display only |
| 39 | Order 3 Detail button | Button | Static: DETAIL | No | Not applicable — display only |
| 40 | Order 3 contract button | Button | Static: SIGN NOW | No | Not applicable — display only |
| 41 | Order 3 Track button | Button | Static: TRACK | No | Not applicable — display only |
| 42 | Zalo contact button | Button | Static: Zalo | No | Not applicable — display only |
| 43 | Telephone contact button | Button | Static: Tel | No | Not applicable — display only |
| 44 | Footer contact heading | Text | Static: Contact Information | No | Not applicable — display only |
| 45 | Company name | Text | Static: DONY Garment Manufacturing Co., Ltd. | No | Not applicable — display only |
| 46 | Tax code | Text | Static: 0315676786 | No | Not applicable — display only |
| 47 | Factory and office address | Text | Static address printed in mockup | No | Not applicable — display only |
| 48 | Phone numbers | Text | Static phone numbers printed in mockup | No | Not applicable — display only |
| 49 | Email addresses | Text | Static email addresses printed in mockup | No | Not applicable — display only |
| 50 | Footer DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 51 | Footer Facebook icon | Button | Facebook icon | No | Not applicable — display only |
| 52 | Footer X icon | Button | X icon | No | Not applicable — display only |
| 53 | Footer LinkedIn icon | Button | LinkedIn icon | No | Not applicable — display only |
| 54 | Footer YouTube icon | Button | YouTube icon | No | Not applicable — display only |
| 55 | Footer TikTok icon | Button | TikTok icon | No | Not applicable — display only |
| 56 | Footer certification badge | Image | Green certification badge | No | Not applicable — display only |
| 57 | Footer policy heading | Text | Static: Information - Policies | No | Not applicable — display only |
| 58 | Company profile link | Button | Static: DONY Garment Manufacturing Company Profile | No | Not applicable — display only |
| 59 | Quality policy link | Button | Static: Quality Policy | No | Not applicable — display only |
| 60 | Warranty policy link | Button | Static: Warranty Policy | No | Not applicable — display only |
| 61 | Delivery and return policy link | Button | Static: Delivery & Return Policy | No | Not applicable — display only |
| 62 | Second warranty policy link | Button | Static: Warranty Policy (repeated in mockup) | No | Not applicable — display only |
| 63 | Shipping policy link | Button | Static: Shipping Policy | No | Not applicable — display only |
| 64 | Payment methods link | Button | Static: Payment Methods | No | Not applicable — display only |
| 65 | Business areas link | Button | Static: Business Areas | No | Not applicable — display only |
| 66 | FAQ link | Button | Static: Frequently Asked Questions (FAQ) | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Upcoming Orders selected, three order cards. | Open S26 |
| Empty (no data) | [NEEDS CLARIFICATION: no orders message] | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: list loading treatment] | Data request or submit in progress |
| Error | [NEEDS CLARIFICATION: list error treatment] | Data request or submit fails |
| Success / confirmation | Not applicable — this is an order navigation screen. | Successful relevant action |

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
| 10 | Upcoming Orders tab | tap | Show upcoming orders | stays |
| 11 | Previous Orders tab | tap | Show previous orders | stays |
| 12 | Order 1 Pay Now button | tap | Open order payment | S35 |
| 13 | Order 2 Pay Now button | tap | Open order payment | S35 |
| 14 | Order 3 Pay Now button | tap | Open order payment | S35 |
| 15 | Order 1 Detail button | tap | Open selected order detail | S27 |
| 16 | Order 2 Detail button | tap | Open selected order detail | S27 |
| 17 | Order 3 Detail button | tap | Open selected order detail | S27 |
| 18 | Order 1 contract button | tap | Open contract | S34 |
| 19 | Order 2 contract button | tap | Open contract | S34 |
| 20 | Order 3 contract button | tap | Open contract | S34 |
| 21 | Order 1 Track button | tap | Open selected order tracking detail | S27 |
| 22 | Order 2 Track button | tap | Open selected order tracking detail | S27 |
| 23 | Order 3 Track button | tap | Open selected order tracking detail | S27 |
| 24 | Zalo contact button | tap | [NEEDS CLARIFICATION: contact destination] | stays |
| 25 | Telephone contact button | tap | [NEEDS CLARIFICATION: dial behavior] | stays |
| 26 | Footer Facebook icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 27 | Footer X icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 28 | Footer LinkedIn icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 29 | Footer YouTube icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 30 | Footer TikTok icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 31 | Company profile link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 32 | Quality policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 33 | Warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 34 | Delivery and return policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 35 | Second warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 36 | Shipping policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 37 | Payment methods link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 38 | Business areas link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 39 | FAQ link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Cards display order status, payment status, contract sign, and arrival estimate as shown. | Mockup |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-ORD-001 [NEEDS CLARIFICATION: module spec unavailable] | Display the user's order history along with current tracking statuses. |

## 8. Responsive and accessibility notes

- Smallest supported width: [NEEDS CLARIFICATION: not specified in sources.]

- What collapses or stacks on a narrow screen: [NEEDS CLARIFICATION: no narrow-screen mockup or rule provided.]

- Text that must remain readable (contrast, minimum size): [NEEDS CLARIFICATION: no numeric accessibility criteria provided.]

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | [NEEDS CLARIFICATION: Screen List does not provide Must / Should / Could priority.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 2 | [NEEDS CLARIFICATION: module spec spec-MFG-07.md is not present in project.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 3 | [NEEDS CLARIFICATION: smallest supported width, narrow layout, and accessibility minimums are not specified.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 4 | [NEEDS CLARIFICATION: Are Pay Now and Sign Now actions enabled for every status shown?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
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
