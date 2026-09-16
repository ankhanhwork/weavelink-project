# Screen Spec: S35 Order Payment Screen

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S35` |
| Screen name | Order Payment Screen |
| Actor | Customer |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-06.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S35-order_payment_screen.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Display order information and allow customer to initiate payment.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S35](img/S35-order_payment_screen.png)

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
| 11 | Order Information heading | Header | Static: Order Information | No | Not applicable — display only |
| 12 | Your Order heading | Header | Static: Your Order (1 Item) | No | Not applicable — display only |
| 13 | Product image | Image | Order item placeholder from order_details (F-PAY-006) | No | Not applicable — display only |
| 14 | Product name and color | Text | Order item name and color from order_details [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 15 | Item unit price | Text | Static sample: $21.99 | No | Not applicable — display only |
| 16 | Order quantity | Text | Static sample: QTY: 100 | No | Not applicable — display only |
| 17 | Order number | Text | order_id from order_details [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 18 | Size subtotal | Text | Static sample: $2199 | No | Not applicable — display only |
| 19 | Shipping and Processing | Text | Static sample: Free | No | Not applicable — display only |
| 20 | Promo code input | Input | [NEEDS CLARIFICATION: promo code absent from F-PAY-004] | No | [NEEDS CLARIFICATION: promo validation] |
| 21 | Generate code button | Button | Static: Generate code | No | Not applicable — display only |
| 22 | Tax amount | Text | tax_amount (F-PAY-002) | No | Not applicable — display only |
| 23 | Merge fees | Text | Static sample: $63; [NEEDS CLARIFICATION: fee data source] | No | Not applicable — display only |
| 24 | Merge savings | Text | Static sample: -$300; [NEEDS CLARIFICATION: savings data source] | No | Not applicable — display only |
| 25 | Total amount | Text | order_amount (F-PAY-004) / calculated_total_cost (F-PAY-002) | No | Not applicable — display only |
| 26 | Terms and Privacy checkbox | Toggle | Agreement to Terms & Condition and Privacy Policy | [NEEDS CLARIFICATION: mandatory status] | [NEEDS CLARIFICATION: validation rule not specified] |
| 27 | Terms and Condition link | Button | Static: Terms & Condition | No | Not applicable — display only |
| 28 | Privacy Policy link | Button | Static: Privacy Policy | No | Not applicable — display only |
| 29 | Merge Policy checkbox | Toggle | Agreement to Merge Policy (only for merge orders) | [NEEDS CLARIFICATION: conditional requirement] | [NEEDS CLARIFICATION: validation rule not specified] |
| 30 | Merge Policy link | Button | Static: Merge Policy | No | Not applicable — display only |
| 31 | Marketing email checkbox | Toggle | Agreement to receive general emails and product offers | No | [NEEDS CLARIFICATION: validation rule not specified] |
| 32 | Make payment button | Button | Static: Make payment | No | Not applicable — display only |
| 33 | Zalo contact button | Button | Static: Zalo | No | Not applicable — display only |
| 34 | Telephone contact button | Button | Static: Tel | No | Not applicable — display only |
| 35 | Footer contact heading | Text | Static: Contact Information | No | Not applicable — display only |
| 36 | Company name | Text | Static: DONY Garment Manufacturing Co., Ltd. | No | Not applicable — display only |
| 37 | Tax code | Text | Static: 0315676786 | No | Not applicable — display only |
| 38 | Factory and office address | Text | Static address printed in mockup | No | Not applicable — display only |
| 39 | Phone numbers | Text | Static phone numbers printed in mockup | No | Not applicable — display only |
| 40 | Email addresses | Text | Static email addresses printed in mockup | No | Not applicable — display only |
| 41 | Footer DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 42 | Footer Facebook icon | Button | Facebook icon | No | Not applicable — display only |
| 43 | Footer X icon | Button | X icon | No | Not applicable — display only |
| 44 | Footer LinkedIn icon | Button | LinkedIn icon | No | Not applicable — display only |
| 45 | Footer YouTube icon | Button | YouTube icon | No | Not applicable — display only |
| 46 | Footer TikTok icon | Button | TikTok icon | No | Not applicable — display only |
| 47 | Footer certification badge | Image | Green certification badge | No | Not applicable — display only |
| 48 | Footer policy heading | Text | Static: Information - Policies | No | Not applicable — display only |
| 49 | Company profile link | Button | Static: DONY Garment Manufacturing Company Profile | No | Not applicable — display only |
| 50 | Quality policy link | Button | Static: Quality Policy | No | Not applicable — display only |
| 51 | Warranty policy link | Button | Static: Warranty Policy | No | Not applicable — display only |
| 52 | Delivery and return policy link | Button | Static: Delivery & Return Policy | No | Not applicable — display only |
| 53 | Second warranty policy link | Button | Static: Warranty Policy (repeated in mockup) | No | Not applicable — display only |
| 54 | Shipping policy link | Button | Static: Shipping Policy | No | Not applicable — display only |
| 55 | Payment methods link | Button | Static: Payment Methods | No | Not applicable — display only |
| 56 | Business areas link | Button | Static: Business Areas | No | Not applicable — display only |
| 57 | FAQ link | Button | Static: Frequently Asked Questions (FAQ) | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Order information and example total $1977.05. | Open S35 |
| Empty (no data) | [NEEDS CLARIFICATION: no order data] | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: payment redirect/processing display] | Data request or submit in progress |
| Error | F-PAY-006 supports success/fail result; placement or screen [NEEDS CLARIFICATION]. | Data request or submit fails |
| Success / confirmation | F-PAY-006 supports receipt/transaction result; destination [NEEDS CLARIFICATION]. | Successful relevant action |

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
| 9 | Back link | tap | Return to contract detail | S34 |
| 10 | Promo code input | type | Update promo code; processing [NEEDS CLARIFICATION] | stays |
| 11 | Generate code button | tap | [NEEDS CLARIFICATION: code generation or coupon application behavior] | stays |
| 12 | Terms and Privacy checkbox | tap | Toggle agreement | stays |
| 13 | Terms and Condition link | tap | [NEEDS CLARIFICATION: destination] | stays |
| 14 | Privacy Policy link | tap | [NEEDS CLARIFICATION: destination] | stays |
| 15 | Merge Policy checkbox | tap | Toggle merge-policy agreement | stays |
| 16 | Merge Policy link | tap | Open merge terms | S24 |
| 17 | Marketing email checkbox | tap | Toggle marketing email consent | stays |
| 18 | Make payment button | tap | F-PAY-004 generates secure redirect_url to VNPay; F-PAY-005 updates payment status; return destination [NEEDS CLARIFICATION] | stays |
| 19 | Zalo contact button | tap | [NEEDS CLARIFICATION: contact destination] | stays |
| 20 | Telephone contact button | tap | [NEEDS CLARIFICATION: dial behavior] | stays |
| 21 | Footer Facebook icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 22 | Footer X icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 23 | Footer LinkedIn icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 24 | Footer YouTube icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 25 | Footer TikTok icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 26 | Company profile link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 27 | Quality policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 28 | Warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 29 | Delivery and return policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 30 | Second warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 31 | Shipping policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 32 | Payment methods link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 33 | Business areas link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 34 | FAQ link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Merge Policy checkbox label says it applies only when merge option was chosen. | Mockup |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-PAY-002 [NEEDS CLARIFICATION: module spec unavailable] | Display the order overview including shipping costs and taxes before payment. |
| F-PAY-004 [NEEDS CLARIFICATION: module spec unavailable] | Generate a secure hash string and redirect the user to the VNPay gateway. |
| F-PAY-005 [NEEDS CLARIFICATION: module spec unavailable] | Process the automatic response from VNPay to update the order payment status. |
| F-PAY-006 [NEEDS CLARIFICATION: module spec unavailable] | Display the electronic receipt or transaction result (Success/Fail) to the user. |

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
| 4 | [NEEDS CLARIFICATION: Where does VNPay return the customer?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 5 | [NEEDS CLARIFICATION: Are the terms checkbox and promo code action required for payment?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
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
