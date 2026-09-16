# Screen Spec: S17 Customer Designs Screen

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S17` |
| Screen name | Customer Designs Screen |
| Actor | Customer |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-05.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S17-customer_designs_screen.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Display all customer designs, including self-designed and consultant-provided designs.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S17](img/S17-customer_designs_screen.png)

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
| 11 | Breadcrumb My Design | Text | Static: My Design | No | Not applicable — display only |
| 12 | My Design heading | Header | Static: My Design | No | Not applicable — display only |
| 13 | Search designs input | Input | [NEEDS CLARIFICATION: search field not specified by F-DES-004] | No | [NEEDS CLARIFICATION: search matching rules] |
| 14 | Category filter | Button | Static: Category | No | Not applicable — display only |
| 15 | Date filter | Button | Static: Date | No | Not applicable — display only |
| 16 | Design table headers | List | Name, Category, Created date, Updated date | No | Not applicable — display only |
| 17 | Design row 1 thumbnail | Image | gallery_of_saved_designs[1] image [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 18 | Design row 1 name | Text | gallery_of_saved_designs[1] name [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 19 | Design row 1 category | Text | gallery_of_saved_designs[1] category [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 20 | Design row 1 created date | Text | gallery_of_saved_designs[1] created date [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 21 | Design row 1 updated date | Text | gallery_of_saved_designs[1] updated date [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 22 | Design row 1 edit icon | Button | Pencil icon | No | Not applicable — display only |
| 23 | Design row 1 copy icon | Button | Copy icon | No | Not applicable — display only |
| 24 | Design row 1 delete icon | Button | Trash icon | No | Not applicable — display only |
| 25 | Design row 1 Make order | Button | Static: Make order | No | Not applicable — display only |
| 26 | Design row 2 thumbnail | Image | gallery_of_saved_designs[2] image [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 27 | Design row 2 name | Text | gallery_of_saved_designs[2] name [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 28 | Design row 2 category | Text | gallery_of_saved_designs[2] category [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 29 | Design row 2 created date | Text | gallery_of_saved_designs[2] created date [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 30 | Design row 2 updated date | Text | gallery_of_saved_designs[2] updated date [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 31 | Design row 2 edit icon | Button | Pencil icon | No | Not applicable — display only |
| 32 | Design row 2 copy icon | Button | Copy icon | No | Not applicable — display only |
| 33 | Design row 2 delete icon | Button | Trash icon | No | Not applicable — display only |
| 34 | Design row 2 Make order | Button | Static: Make order | No | Not applicable — display only |
| 35 | Design row 3 thumbnail | Image | gallery_of_saved_designs[3] image [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 36 | Design row 3 name | Text | gallery_of_saved_designs[3] name [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 37 | Design row 3 category | Text | gallery_of_saved_designs[3] category [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 38 | Design row 3 created date | Text | gallery_of_saved_designs[3] created date [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 39 | Design row 3 updated date | Text | gallery_of_saved_designs[3] updated date [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 40 | Design row 3 edit icon | Button | Pencil icon | No | Not applicable — display only |
| 41 | Design row 3 copy icon | Button | Copy icon | No | Not applicable — display only |
| 42 | Design row 3 delete icon | Button | Trash icon | No | Not applicable — display only |
| 43 | Design row 3 Make order | Button | Static: Make order | No | Not applicable — display only |
| 44 | Design row 4 thumbnail | Image | gallery_of_saved_designs[4] image [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 45 | Design row 4 name | Text | gallery_of_saved_designs[4] name [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 46 | Design row 4 category | Text | gallery_of_saved_designs[4] category [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 47 | Design row 4 created date | Text | gallery_of_saved_designs[4] created date [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 48 | Design row 4 updated date | Text | gallery_of_saved_designs[4] updated date [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 49 | Design row 4 edit icon | Button | Pencil icon | No | Not applicable — display only |
| 50 | Design row 4 copy icon | Button | Copy icon | No | Not applicable — display only |
| 51 | Design row 4 delete icon | Button | Trash icon | No | Not applicable — display only |
| 52 | Design row 4 Make order | Button | Static: Make order | No | Not applicable — display only |
| 53 | Design row 5 thumbnail | Image | gallery_of_saved_designs[5] image [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 54 | Design row 5 name | Text | gallery_of_saved_designs[5] name [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 55 | Design row 5 category | Text | gallery_of_saved_designs[5] category [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 56 | Design row 5 created date | Text | gallery_of_saved_designs[5] created date [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 57 | Design row 5 updated date | Text | gallery_of_saved_designs[5] updated date [NEEDS CLARIFICATION: schema] | No | Not applicable — display only |
| 58 | Design row 5 edit icon | Button | Pencil icon | No | Not applicable — display only |
| 59 | Design row 5 copy icon | Button | Copy icon | No | Not applicable — display only |
| 60 | Design row 5 delete icon | Button | Trash icon | No | Not applicable — display only |
| 61 | Design row 5 Make order | Button | Static: Make order | No | Not applicable — display only |
| 62 | Rows per page control | Button | Static: View 5 designs per page | No | Not applicable — display only |
| 63 | Result count | Text | Static sample: 5 of 9 products | No | Not applicable — display only |
| 64 | Previous page arrow | Button | Left arrow | No | Not applicable — display only |
| 65 | Page 1 button | Button | Static: 1 | No | Not applicable — display only |
| 66 | Page 2 button | Button | Static: 2 | No | Not applicable — display only |
| 67 | Next page arrow | Button | Right arrow | No | Not applicable — display only |
| 68 | Zalo contact button | Button | Static: Zalo | No | Not applicable — display only |
| 69 | Telephone contact button | Button | Static: Tel | No | Not applicable — display only |
| 70 | Footer contact heading | Text | Static: Contact Information | No | Not applicable — display only |
| 71 | Company name | Text | Static: DONY Garment Manufacturing Co., Ltd. | No | Not applicable — display only |
| 72 | Tax code | Text | Static: 0315676786 | No | Not applicable — display only |
| 73 | Factory and office address | Text | Static address printed in mockup | No | Not applicable — display only |
| 74 | Phone numbers | Text | Static phone numbers printed in mockup | No | Not applicable — display only |
| 75 | Email addresses | Text | Static email addresses printed in mockup | No | Not applicable — display only |
| 76 | Footer DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 77 | Footer Facebook icon | Button | Facebook icon | No | Not applicable — display only |
| 78 | Footer X icon | Button | X icon | No | Not applicable — display only |
| 79 | Footer LinkedIn icon | Button | LinkedIn icon | No | Not applicable — display only |
| 80 | Footer YouTube icon | Button | YouTube icon | No | Not applicable — display only |
| 81 | Footer TikTok icon | Button | TikTok icon | No | Not applicable — display only |
| 82 | Footer certification badge | Image | Green certification badge | No | Not applicable — display only |
| 83 | Footer policy heading | Text | Static: Information - Policies | No | Not applicable — display only |
| 84 | Company profile link | Button | Static: DONY Garment Manufacturing Company Profile | No | Not applicable — display only |
| 85 | Quality policy link | Button | Static: Quality Policy | No | Not applicable — display only |
| 86 | Warranty policy link | Button | Static: Warranty Policy | No | Not applicable — display only |
| 87 | Delivery and return policy link | Button | Static: Delivery & Return Policy | No | Not applicable — display only |
| 88 | Second warranty policy link | Button | Static: Warranty Policy (repeated in mockup) | No | Not applicable — display only |
| 89 | Shipping policy link | Button | Static: Shipping Policy | No | Not applicable — display only |
| 90 | Payment methods link | Button | Static: Payment Methods | No | Not applicable — display only |
| 91 | Business areas link | Button | Static: Business Areas | No | Not applicable — display only |
| 92 | FAQ link | Button | Static: Frequently Asked Questions (FAQ) | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Five saved design rows, first page. | Open S17 |
| Empty (no data) | [NEEDS CLARIFICATION: empty designs message] | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: design list loading treatment] | Data request or submit in progress |
| Error | [NEEDS CLARIFICATION: design list error treatment] | Data request or submit fails |
| Success / confirmation | [NEEDS CLARIFICATION: edit/copy/delete confirmation behavior] | Successful relevant action |

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
| 10 | Search designs input | type | [NEEDS CLARIFICATION: filtering behavior] | stays |
| 11 | Category filter | tap | [NEEDS CLARIFICATION: filter choices] | stays |
| 12 | Date filter | tap | [NEEDS CLARIFICATION: filter choices] | stays |
| 13 | Design row 1 edit icon | tap | Open design editor | S13 |
| 14 | Design row 2 edit icon | tap | Open design editor | S13 |
| 15 | Design row 3 edit icon | tap | Open design editor | S13 |
| 16 | Design row 4 edit icon | tap | Open design editor | S13 |
| 17 | Design row 5 edit icon | tap | Open design editor | S13 |
| 18 | Design row 1 copy icon | tap | [NEEDS CLARIFICATION: duplicate behavior] | stays |
| 19 | Design row 2 copy icon | tap | [NEEDS CLARIFICATION: duplicate behavior] | stays |
| 20 | Design row 3 copy icon | tap | [NEEDS CLARIFICATION: duplicate behavior] | stays |
| 21 | Design row 4 copy icon | tap | [NEEDS CLARIFICATION: duplicate behavior] | stays |
| 22 | Design row 5 copy icon | tap | [NEEDS CLARIFICATION: duplicate behavior] | stays |
| 23 | Design row 1 delete icon | tap | [NEEDS CLARIFICATION: delete behavior] | stays |
| 24 | Design row 2 delete icon | tap | [NEEDS CLARIFICATION: delete behavior] | stays |
| 25 | Design row 3 delete icon | tap | [NEEDS CLARIFICATION: delete behavior] | stays |
| 26 | Design row 4 delete icon | tap | [NEEDS CLARIFICATION: delete behavior] | stays |
| 27 | Design row 5 delete icon | tap | [NEEDS CLARIFICATION: delete behavior] | stays |
| 28 | Design row 1 Make order | tap | Create order from selected design | S22 |
| 29 | Design row 2 Make order | tap | Create order from selected design | S22 |
| 30 | Design row 3 Make order | tap | Create order from selected design | S22 |
| 31 | Design row 4 Make order | tap | Create order from selected design | S22 |
| 32 | Design row 5 Make order | tap | Create order from selected design | S22 |
| 33 | Rows per page control | tap | Change visible page/row count | stays |
| 34 | Previous page arrow | tap | Change visible page/row count | stays |
| 35 | Page 1 button | tap | Change visible page/row count | stays |
| 36 | Page 2 button | tap | Change visible page/row count | stays |
| 37 | Next page arrow | tap | Change visible page/row count | stays |
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
| SR-001 | Each shown design row offers Make order. | Mockup |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-DES-004 [NEEDS CLARIFICATION: module spec unavailable] | Display a list of design templates the user has previously saved. |

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
| 4 | [NEEDS CLARIFICATION: Are consultant-provided designs distinguished visually from self-designed designs?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
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
