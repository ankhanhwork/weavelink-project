# Screen Spec: S03 Login Screen

<!--

DBIZ3 Session 4 template. One file per screen. Keep the DBIZ2 Screen ID unchanged.

The mockup image stays an image; everything around it becomes text.

-->

| Field | Value |
|---|---|
| Screen ID | `S03` |
| Screen name | Login Screen |
| Actor | Guest |
| Priority | [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List] |
| Belongs to module | `spec-MFG-01.md` [NEEDS CLARIFICATION: file unavailable] |
| Mockup image | `img/S03-login_screen.png` |
| Status | Draft |

## 1. Purpose

**Shown when:** Allow users to log in to the system.

**The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specified; documented interactions appear in section 5.]

## 2. Mockup

![S03](img/S03-login_screen.png)

<!-- The image is the visual contract: spacing, grouping, and hierarchy. The tables below are the behavioural contract. -->

## 3. Element inventory

<!-- Walk the mockup top to bottom, left to right. Every visible element gets a stable name. -->

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Brand panel logo | Image | Static LOGO placeholder | No | Not applicable — display only |
| 2 | Brand welcome heading | Header | Static: Welcome to Dony! | No | Not applicable — display only |
| 3 | Brand description | Text | Static welcome copy | No | Not applicable — display only |
| 4 | Brand image | Image | Placeholder | No | Not applicable — display only |
| 5 | Welcome back heading | Header | Static: Welcome back! | No | Not applicable — display only |
| 6 | Login subtitle | Text | Static: Meet the good taste today | No | Not applicable — display only |
| 7 | Email or phone label | Text | Static: E-mail or phone number | No | Not applicable — display only |
| 8 | Email or phone input | Input | [NEEDS CLARIFICATION: screenshot accepts email or phone, F-USER-005 names username_email] | Yes | [NEEDS CLARIFICATION: validation rule not specified] |
| 9 | Password label | Text | Static: Password | No | Not applicable — display only |
| 10 | Password input | Input | password (F-USER-005) | Yes | [NEEDS CLARIFICATION: validation rule not specified] |
| 11 | Forgot Password link | Button | Static: Forgot Password? | No | Not applicable — display only |
| 12 | Sign In submit button | Button | Static: Sign In | No | Not applicable — display only |
| 13 | Other accounts divider | Text | Static: or do it via other accounts | No | Not applicable — display only |
| 14 | Google sign-in | Button | Google icon | No | Not applicable — display only |
| 15 | Apple sign-in | Button | Apple icon | No | Not applicable — display only |
| 16 | Facebook sign-in | Button | Facebook icon | No | Not applicable — display only |
| 17 | New account prompt | Text | Static: Don’t have an account? | No | Not applicable — display only |
| 18 | Sign Up link | Button | Static: Sign Up | No | Not applicable — display only |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Default | Blank login form. | Open S03 |
| Empty (no data) | Blank credentials as shown; submit availability [NEEDS CLARIFICATION]. | No relevant records or input |
| Loading | [NEEDS CLARIFICATION: authentication loading treatment] | Data request or submit in progress |
| Error | [NEEDS CLARIFICATION: invalid credential display] | Data request or submit fails |
| Success / confirmation | Authenticated session; destination determined by redirect_url [NEEDS CLARIFICATION]. | Successful relevant action |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Email or phone input | type | Update login identifier | stays |
| 2 | Password input | type | Update password | stays |
| 3 | Forgot Password link | tap | Open password recovery | S04 |
| 4 | Sign In submit button | tap | F-USER-005 verifies credentials and creates session; redirect_url destination [NEEDS CLARIFICATION] | stays |
| 5 | Google sign-in | tap | [NEEDS CLARIFICATION: social sign-in behavior] | stays |
| 6 | Apple sign-in | tap | [NEEDS CLARIFICATION: social sign-in behavior] | stays |
| 7 | Facebook sign-in | tap | [NEEDS CLARIFICATION: social sign-in behavior] | stays |
| 8 | Sign Up link | tap | Open registration | S02 |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | [NEEDS CLARIFICATION: no additional screen-level rule documented] | Unspecified |

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| F-USER-004 [NEEDS CLARIFICATION: module spec unavailable] | Display the login interface requiring users to enter their username and password. |
| F-USER-005 [NEEDS CLARIFICATION: module spec unavailable] | Verify login credentials and generate a secure session token for the user. |

## 8. Responsive and accessibility notes

- Smallest supported width: [NEEDS CLARIFICATION: not specified in sources.]

- What collapses or stacks on a narrow screen: [NEEDS CLARIFICATION: no narrow-screen mockup or rule provided.]

- Text that must remain readable (contrast, minimum size): [NEEDS CLARIFICATION: no numeric accessibility criteria provided.]

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | [NEEDS CLARIFICATION: Screen List does not provide Must / Should / Could priority.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 2 | [NEEDS CLARIFICATION: module spec spec-MFG-01.md is not present in project.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 3 | [NEEDS CLARIFICATION: smallest supported width, narrow layout, and accessibility minimums are not specified.] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 4 | [NEEDS CLARIFICATION: Can users log in by phone, given function list names username_email?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
| 5 | [NEEDS CLARIFICATION: Where does a successful login navigate?] | [NEEDS CLARIFICATION: impact not assessed] | Open |
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
