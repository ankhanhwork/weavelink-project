# Screen Spec: S01 Home Page

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S01` |
| Screen name | Home Page |
| Actor | Guest |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-04.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S01-home_page.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Display homepage content and entry points to browse products, sign up, and sign in.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S01](img/S01-home_page.png)

<!-- The image is the visual contract: spacing, grouping, and hierarchy. The tables below are the behavioural contract. -->

## 3. Element inventory

<!-- Walk the mockup top to bottom, left to right. Every visible element gets a stable name. -->

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Home DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 2 | Home Catalog link | Button | Static: CATALOG | No | Not applicable — display only |
| 3 | Home About Dony link | Button | Static: ABOUT DONY | No | Not applicable — display only |
| 4 | Home My Design link | Button | Static: MY DESIGN | No | Not applicable — display only |
| 5 | Home My Order link | Button | Static: MY ORDER | No | Not applicable — display only |
| 6 | Home Contact Us link | Button | Static: CONTACT US | No | Not applicable — display only |
| 7 | Sign In button | Button | Static: Sign In | No | Not applicable — display only |
| 8 | Sign Up button | Button | Static: Sign Up | No | Not applicable — display only |
| 9 | Hero headline | Text | Static: CREATE YOUR OWN PRODUCT | No | Not applicable — display only |
| 10 | Hero benefit labels | List | Static: Easy to choose; Easy to use; Easy to delivery | No | Not applicable — display only |
| 11 | Hero call to action | Button | Unlabeled dark button; [NEEDS CLARIFICATION: text and action] | No | Not applicable — display only |
| 12 | Hero image | Image | Placeholder | No | Not applicable — display only |
| 13 | Trust statement | Text | Static: Trusted by 10K+ customer | No | Not applicable — display only |
| 14 | Best seller heading | Header | Static: BEST SELLER IS HERE | No | Not applicable — display only |
| 15 | Best seller product 1 | Image | T-Shirt placeholder | No | Not applicable — display only |
| 16 | Best seller product 2 | Image | Hoodie placeholder | No | Not applicable — display only |
| 17 | Best seller product 3 | Image | Sweatshirt placeholder | No | Not applicable — display only |
| 18 | How to create heading | Header | Static: HOW TO CREATE! | No | Not applicable — display only |
| 19 | How to create description | Text | Static introductory text | No | Not applicable — display only |
| 20 | Select product card | List | Image, title, description | No | Not applicable — display only |
| 21 | Select product card TRY NOW | Button | Static: TRY NOW | No | Not applicable — display only |
| 22 | Add design card | List | Image, title, description | No | Not applicable — display only |
| 23 | Add design card TRY NOW | Button | Static: TRY NOW | No | Not applicable — display only |
| 24 | Request consultation card | List | Image, title, description | No | Not applicable — display only |
| 25 | Request consultation card TRY NOW | Button | Static: TRY NOW | No | Not applicable — display only |
| 26 | Idea and inspiration heading | Header | Static: IDEA AND INSPIRATION | No | Not applicable — display only |
| 27 | Idea description | Text | Static description | No | Not applicable — display only |
| 28 | Idea image 1 | Image | Placeholder | No | Not applicable — display only |
| 29 | Idea image 2 | Image | Placeholder | No | Not applicable — display only |
| 30 | Idea image 3 | Image | Placeholder | No | Not applicable — display only |
| 31 | Idea image 4 | Image | Placeholder | No | Not applicable — display only |
| 32 | Idea image 5 | Image | Placeholder | No | Not applicable — display only |
| 33 | Get started heading | Header | Static: GET STARTED TODAY | No | Not applicable — display only |
| 34 | Get started description | Text | Static description | No | Not applicable — display only |
| 35 | Get started button | Button | Static: GET STARTED NOW | No | Not applicable — display only |
| 36 | Discount card 1 | List | Image, 20% discount, T-Shirt + Consultation | No | Not applicable — display only |
| 37 | Discount card 2 | List | Image, 25% discount, Sweatshirt + Consultation | No | Not applicable — display only |
| 38 | Discount next arrow | Button | Right arrow | No | Not applicable — display only |
| 39 | Zalo contact button | Button | Static: Zalo | No | Not applicable — display only |
| 40 | Telephone contact button | Button | Static: Tel | No | Not applicable — display only |
| 41 | Footer contact heading | Text | Static: Contact Information | No | Not applicable — display only |
| 42 | Company name | Text | Static: DONY Garment Manufacturing Co., Ltd. | No | Not applicable — display only |
| 43 | Tax code | Text | Static: 0315676786 | No | Not applicable — display only |
| 44 | Factory and office address | Text | Static address printed in mockup | No | Not applicable — display only |
| 45 | Phone numbers | Text | Static phone numbers printed in mockup | No | Not applicable — display only |
| 46 | Email addresses | Text | Static email addresses printed in mockup | No | Not applicable — display only |
| 47 | Footer DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 48 | Footer Facebook icon | Button | Facebook icon | No | Not applicable — display only |
| 49 | Footer X icon | Button | X icon | No | Not applicable — display only |
| 50 | Footer LinkedIn icon | Button | LinkedIn icon | No | Not applicable — display only |
| 51 | Footer YouTube icon | Button | YouTube icon | No | Not applicable — display only |
| 52 | Footer TikTok icon | Button | TikTok icon | No | Not applicable — display only |
| 53 | Footer certification badge | Image | Green certification badge | No | Not applicable — display only |
| 54 | Footer policy heading | Text | Static: Information - Policies | No | Not applicable — display only |
| 55 | Company profile link | Button | Static: DONY Garment Manufacturing Company Profile | No | Not applicable — display only |
| 56 | Quality policy link | Button | Static: Quality Policy | No | Not applicable — display only |
| 57 | Warranty policy link | Button | Static: Warranty Policy | No | Not applicable — display only |
| 58 | Delivery and return policy link | Button | Static: Delivery & Return Policy | No | Not applicable — display only |
| 59 | Second warranty policy link | Button | Static: Warranty Policy (repeated in mockup) | No | Not applicable — display only |
| 60 | Shipping policy link | Button | Static: Shipping Policy | No | Not applicable — display only |
| 61 | Payment methods link | Button | Static: Payment Methods | No | Not applicable — display only |
| 62 | Business areas link | Button | Static: Business Areas | No | Not applicable — display only |
| 63 | FAQ link | Button | Static: Frequently Asked Questions (FAQ) | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Homepage sections as shown. | Open S01 |
| Empty (no data) | Not applicable — page content is static in the mockup. | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: loading treatment for product or promotion content] | Data request or submit in progress |
| Error | [NEEDS CLARIFICATION: error treatment for unavailable product or promotion content] | Data request or submit fails |
| Success / confirmation | Not applicable — no confirmation action shown. | Successful relevant action |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Home DONY logo | tap | Open home | S01 |
| 2 | Home Catalog link | tap | Open catalog | S08 |
| 3 | Home About Dony link | tap | [NEEDS CLARIFICATION: destination] | stays |
| 4 | Home My Design link | tap | Open saved designs | S17 |
| 5 | Home My Order link | tap | Open orders | S26 |
| 6 | Home Contact Us link | tap | [NEEDS CLARIFICATION: destination] | stays |
| 7 | Sign In button | tap | Open login | S03 |
| 8 | Sign Up button | tap | Open registration | S02 |
| 9 | Hero call to action | tap | [NEEDS CLARIFICATION: button purpose] | stays |
| 10 | Best seller product 1 | tap | Open selected product detail | S09 |
| 11 | Best seller product 2 | tap | Open selected product detail | S09 |
| 12 | Best seller product 3 | tap | Open selected product detail | S09 |
| 13 | Select product card TRY NOW | tap | Open catalog | S08 |
| 14 | Add design card TRY NOW | tap | [NEEDS CLARIFICATION: base product selection before design] | S13 |
| 15 | Request consultation card TRY NOW | tap | [NEEDS CLARIFICATION: base product selection before service request] | S15 |
| 16 | Get started button | tap | [NEEDS CLARIFICATION: destination] | stays |
| 17 | Discount next arrow | tap | Show next discount card | stays |
| 18 | Zalo contact button | tap | [NEEDS CLARIFICATION: contact destination] | stays |
| 19 | Telephone contact button | tap | [NEEDS CLARIFICATION: dial behavior] | stays |
| 20 | Footer Facebook icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 21 | Footer X icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 22 | Footer LinkedIn icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 23 | Footer YouTube icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 24 | Footer TikTok icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 25 | Company profile link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 26 | Quality policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 27 | Warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 28 | Delivery and return policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 29 | Second warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 30 | Shipping policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 31 | Payment methods link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 32 | Business areas link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 33 | FAQ link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Only homepage content and entry points identified in Screen List are specified. | screen-list.md |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-PROD-001 [NEEDS CLARIFICATION: module spec unavailable] | Display the product list in a grid layout with images and basic pricing. |
| F-PROD-002 [NEEDS CLARIFICATION: module spec unavailable] | Display detailed product information, technical specifications, and available options. |

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
| 4 | [NEEDS CLARIFICATION: Are bestseller and discount cards dynamic or fixed?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
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
