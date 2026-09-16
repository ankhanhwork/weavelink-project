# Screen Spec: S06 User Profile Screen

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S06` |
| Screen name | User Profile Screen |
| Actor | Member |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-02.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S06-user_profile_screen.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Allow users to view and update personal profile information and assigned roles.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S06](img/S06-user_profile_screen.png)

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
| 11 | Breadcrumb Account Info | Text | Static: Account Info | No | Not applicable — display only |
| 12 | Personal Info heading | Header | Static: Personal Info | No | Not applicable — display only |
| 13 | Profile sidebar icon | Image | Person icon | No | Not applicable — display only |
| 14 | Personal Info sidebar item | Button | Static: Personal Info | No | Not applicable — display only |
| 15 | Security sidebar icon | Image | Shield icon | No | Not applicable — display only |
| 16 | Login and Security sidebar item | Button | Static: Login and Security | No | Not applicable — display only |
| 17 | Language sidebar icon | Image | Globe icon | No | Not applicable — display only |
| 18 | Language sidebar item | Button | Static: Language | No | Not applicable — display only |
| 19 | Logout sidebar icon | Image | Exit icon | No | Not applicable — display only |
| 20 | Log out sidebar item | Button | Static: Log out | No | Not applicable — display only |
| 21 | Account Info subheading | Header | Static: Account Info | No | Not applicable — display only |
| 22 | Display name label | Text | Static: DISPLAY NAME | No | Not applicable — display only |
| 23 | Display name input | Input | current_profile_data.display_name [NEEDS CLARIFICATION: field name not defined in F-PROF-002] | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: validation rule not specified] |
| 24 | Real name label | Text | Static: REALNAME | No | Not applicable — display only |
| 25 | Real name input | Input | current_profile_data.real_name [NEEDS CLARIFICATION: field name not defined] | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: validation rule not specified] |
| 26 | Phone label | Text | Static: PHONE | No | Not applicable — display only |
| 27 | Phone input | Input | current_profile_data.phone [NEEDS CLARIFICATION: field name not defined] | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: validation rule not specified] |
| 28 | Email label | Text | Static: EMAIL | No | Not applicable — display only |
| 29 | Email input | Input | current_profile_data.email [NEEDS CLARIFICATION: field name not defined] | [NEEDS CLARIFICATION] | [NEEDS CLARIFICATION: validation rule not specified] |
| 30 | Company name label | Text | Static: COMPANY NAME (Optional) | No | Not applicable — display only |
| 31 | Company name input | Input | current_profile_data.company_name [NEEDS CLARIFICATION: field name not defined] | No | [NEEDS CLARIFICATION: validation rule not specified] |
| 32 | Update profile button | Button | Static: Update profile | No | Not applicable — display only |
| 33 | Cancel button | Button | Static: Cancel | No | Not applicable — display only |
| 34 | Zalo contact button | Button | Static: Zalo | No | Not applicable — display only |
| 35 | Telephone contact button | Button | Static: Tel | No | Not applicable — display only |
| 36 | Footer contact heading | Text | Static: Contact Information | No | Not applicable — display only |
| 37 | Company name | Text | Static: DONY Garment Manufacturing Co., Ltd. | No | Not applicable — display only |
| 38 | Tax code | Text | Static: 0315676786 | No | Not applicable — display only |
| 39 | Factory and office address | Text | Static address printed in mockup | No | Not applicable — display only |
| 40 | Phone numbers | Text | Static phone numbers printed in mockup | No | Not applicable — display only |
| 41 | Email addresses | Text | Static email addresses printed in mockup | No | Not applicable — display only |
| 42 | Footer DONY logo | Image | Static DONY logo | No | Not applicable — display only |
| 43 | Footer Facebook icon | Button | Facebook icon | No | Not applicable — display only |
| 44 | Footer X icon | Button | X icon | No | Not applicable — display only |
| 45 | Footer LinkedIn icon | Button | LinkedIn icon | No | Not applicable — display only |
| 46 | Footer YouTube icon | Button | YouTube icon | No | Not applicable — display only |
| 47 | Footer TikTok icon | Button | TikTok icon | No | Not applicable — display only |
| 48 | Footer certification badge | Image | Green certification badge | No | Not applicable — display only |
| 49 | Footer policy heading | Text | Static: Information - Policies | No | Not applicable — display only |
| 50 | Company profile link | Button | Static: DONY Garment Manufacturing Company Profile | No | Not applicable — display only |
| 51 | Quality policy link | Button | Static: Quality Policy | No | Not applicable — display only |
| 52 | Warranty policy link | Button | Static: Warranty Policy | No | Not applicable — display only |
| 53 | Delivery and return policy link | Button | Static: Delivery & Return Policy | No | Not applicable — display only |
| 54 | Second warranty policy link | Button | Static: Warranty Policy (repeated in mockup) | No | Not applicable — display only |
| 55 | Shipping policy link | Button | Static: Shipping Policy | No | Not applicable — display only |
| 56 | Payment methods link | Button | Static: Payment Methods | No | Not applicable — display only |
| 57 | Business areas link | Button | Static: Business Areas | No | Not applicable — display only |
| 58 | FAQ link | Button | Static: Frequently Asked Questions (FAQ) | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Profile fields populated with shown sample values. | Open S06 |
| Empty (no data) | [NEEDS CLARIFICATION: behavior when profile data is missing] | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: loading treatment for user_profile_object] | Data request or submit in progress |
| Error | [NEEDS CLARIFICATION: save or load error treatment] | Data request or submit fails |
| Success / confirmation | F-PROF-003 provides success_notification; placement [NEEDS CLARIFICATION]. | Successful relevant action |

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
| 10 | Personal Info sidebar item | tap | Show current profile | stays |
| 11 | Login and Security sidebar item | tap | [NEEDS CLARIFICATION: whether opens S07 or a different screen] | stays |
| 12 | Language sidebar item | tap | [NEEDS CLARIFICATION: language screen/behavior] | stays |
| 13 | Log out sidebar item | tap | F-USER-006 invalidates session and redirects to login | S03 |
| 14 | Display name input | type | Update field locally | stays |
| 15 | Real name input | type | Update field locally | stays |
| 16 | Phone input | type | Update field locally | stays |
| 17 | Email input | type | Update field locally | stays |
| 18 | Company name input | type | Update field locally | stays |
| 19 | Update profile button | tap | F-PROF-003 saves updated_fields; success_notification behavior [NEEDS CLARIFICATION] | stays |
| 20 | Cancel button | tap | [NEEDS CLARIFICATION: discard or navigation behavior] | stays |
| 21 | Zalo contact button | tap | [NEEDS CLARIFICATION: contact destination] | stays |
| 22 | Telephone contact button | tap | [NEEDS CLARIFICATION: dial behavior] | stays |
| 23 | Footer Facebook icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 24 | Footer X icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 25 | Footer LinkedIn icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 26 | Footer YouTube icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 27 | Footer TikTok icon | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 28 | Company profile link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 29 | Quality policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 30 | Warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 31 | Delivery and return policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 32 | Second warranty policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 33 | Shipping policy link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 34 | Payment methods link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 35 | Business areas link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |
| 36 | FAQ link | tap | [NEEDS CLARIFICATION: external or in-system destination] | stays |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Company Name is explicitly marked Optional in the mockup. | Mockup |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-PROF-001 [NEEDS CLARIFICATION: module spec unavailable] | Retrieve and display the current user's personal profile details. |
| F-PROF-002 [NEEDS CLARIFICATION: module spec unavailable] | Display a form allowing the user to modify their personal contact information. |
| F-PROF-003 [NEEDS CLARIFICATION: module spec unavailable] | Save the changes made to the user's personal information into the system. |
| F-USER-006 [NEEDS CLARIFICATION: module spec unavailable] | Invalidate the current session token, revoke user access permissions, redirect to the login screen |

## 8. Responsive and accessibility notes

- Smallest supported width: [NEEDS CLARIFICATION: not specified in sources.]

- What collapses or stacks on a narrow screen: [NEEDS CLARIFICATION: no narrow-screen mockup or rule provided.]

- Text that must remain readable (contrast, minimum size): [NEEDS CLARIFICATION: no numeric accessibility criteria provided.]

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | [NEEDS CLARIFICATION: Screen List does not provide Must / Should / Could priority.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 2 | [NEEDS CLARIFICATION: module spec spec-MFG-02.md is not present in project.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 3 | [NEEDS CLARIFICATION: smallest supported width, narrow layout, and accessibility minimums are not specified.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 4 | [NEEDS CLARIFICATION: Screen Overview mentions assigned roles, but none are visible in the mockup. Where are roles displayed?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
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
