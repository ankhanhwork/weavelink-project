# Screen Spec: S16 Design Service Payment Screen

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S16` |
| Screen name | Design Service Payment Screen |
| Actor | Customer |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-05.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S16-design_service_payment_screen.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Allow customers to pay for design service.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S16](img/S16-design_service_payment_screen.png)

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
| 11 | Payment heading | Header | Static: Payment | No | Not applicable — display only |
| 12 | Design Request Summary heading | Header | Static: Design Request Summary | No | Not applicable — display only |
| 13 | Request ID | Text | request_id (F-DES-007) | No | Not applicable — display only |
| 14 | Product name | Text | new_request_record product name [NEEDS CLARIFICATION: field schema] | No | Not applicable — display only |
| 15 | Description | Text | requirement_text (F-DES-006) | No | Not applicable — display only |
| 16 | Desired delivery date | Text | deadline (F-DES-006) | No | Not applicable — display only |
| 17 | Additional notes | Text | [NEEDS CLARIFICATION: notes field absent from F-DES-006] | No | Not applicable — display only |
| 18 | Design fee | Text | Static mockup example: $30; [NEEDS CLARIFICATION: fee data source] | No | Not applicable — display only |
| 19 | Payment scope note | Text | Static: Payment applies to design service only. Production orders are paid later. | No | Not applicable — display only |
| 20 | Confirm and Pay button | Button | Static: Confirm and Pay | No | Not applicable — display only |
| 21 | Zalo contact button | Button | Static: Zalo | No | Not applicable — display only |
| 22 | Telephone contact button | Button | Static: Tel | No | Not applicable — display only |
| 23 | Footer contact heading | Text | Static: Contact Information | No | Not applicable — display only |
| 24 | Company name | Text | Static: DONY Garment Manufacturing Co., Ltd. | No | Not applicable — display only |
| 25 | Tax code | Text | Static: 0315676786 | No | Not applicable — display only |
| 26 | Factory and office address | Text | Static address printed in mockup | No | Not applicable — display only |
| 27 | Phone numbers | Text | Static phone numbers printed in mockup | No | Not applicable — display only |
| 28 | Email addresses | Text | Static email addresses printed in mockup | No | Not applicable — display only |
| 29 | Footer DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 30 | Footer Facebook icon | Button | Facebook icon | No | Not applicable — display only |
| 31 | Footer X icon | Button | X icon | No | Not applicable — display only |
| 32 | Footer LinkedIn icon | Button | LinkedIn icon | No | Not applicable — display only |
| 33 | Footer YouTube icon | Button | YouTube icon | No | Not applicable — display only |
| 34 | Footer TikTok icon | Button | TikTok icon | No | Not applicable — display only |
| 35 | Footer certification badge | Image | Green certification badge | No | Not applicable — display only |
| 36 | Footer policy heading | Text | Static: Information - Policies | No | Not applicable — display only |
| 37 | Company profile link | Button | Static: DONY Garment Manufacturing Company Profile | No | Not applicable — display only |
| 38 | Quality policy link | Button | Static: Quality Policy | No | Not applicable — display only |
| 39 | Warranty policy link | Button | Static: Warranty Policy | No | Not applicable — display only |
| 40 | Delivery and return policy link | Button | Static: Delivery & Return Policy | No | Not applicable — display only |
| 41 | Second warranty policy link | Button | Static: Warranty Policy (repeated in mockup) | No | Not applicable — display only |
| 42 | Shipping policy link | Button | Static: Shipping Policy | No | Not applicable — display only |
| 43 | Payment methods link | Button | Static: Payment Methods | No | Not applicable — display only |
| 44 | Business areas link | Button | Static: Business Areas | No | Not applicable — display only |
| 45 | FAQ link | Button | Static: Frequently Asked Questions (FAQ) | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Design request summary with $30 design fee. | Open S16 |
| Empty (no data) | [NEEDS CLARIFICATION: missing design request behavior] | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: payment processing indicator] | Data request or submit in progress |
| Error | [NEEDS CLARIFICATION: failed payment display] | Data request or submit fails |
| Success / confirmation | F-DES-007 sets request status Paid; confirmation presentation [NEEDS CLARIFICATION]. | Successful relevant action |

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
| 9 | Back link | tap | Return to design service request | S15 |
| 10 | Confirm and Pay button | tap | Initiate design service payment; F-DES-007 updates request status when successful; gateway and next screen [NEEDS CLARIFICATION] | stays |
| 11 | Zalo contact button | tap | [NEEDS CLARIFICATION: contact destination] | stays |
| 12 | Telephone contact button | tap | [NEEDS CLARIFICATION: dial behavior] | stays |
| 13 | Footer Facebook icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 14 | Footer X icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 15 | Footer LinkedIn icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 16 | Footer YouTube icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 17 | Footer TikTok icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 18 | Company profile link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 19 | Quality policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 20 | Warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 21 | Delivery and return policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 22 | Second warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 23 | Shipping policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 24 | Payment methods link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 25 | Business areas link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 26 | FAQ link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Payment applies to the design service only; production orders are paid later. | Mockup |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-DES-007 [NEEDS CLARIFICATION: module spec unavailable] | Update the design request status to "Paid" upon successful transaction. |

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
| 4 | [NEEDS CLARIFICATION: What service payment provider, transaction flow, and return screen are used?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
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
