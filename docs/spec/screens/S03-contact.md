# Screen Spec: S03 Contact Dony

| Field | Value |
|---|---|
| Screen ID | `S03` |
| Screen name | Contact Dony |
| Actor | Guest and authenticated users |
| Priority | Should (MVP) |
| Belongs to module | [MFG-04](../specs/spec-MFG-04.md) |
| Route | `/contact` |
| Mockup image | img/S03-01-contact.png |
| Status | Approved final demo specification |


## 1. Purpose

**Shown when:** A visitor opens the public Contact page from the storefront. S03 shares the public navigation used by the [S01 Home Page](S01-home-page.md); it presents the verified public contact details available in the supplied sources so prospective customers can reach Dony about garment orders.

**The user leaves this screen when:** They follow a public storefront navigation link or return to S01.

## 2. Mockup

![Contact Dony screen mockup](img/S03-01-contact.png)

### Mockup deviations

- Treat mockup imagery and its map-like panel as illustrative, not a verified photograph or map of Dony's premises.
- Treat extra promotional copy and map controls as placeholders; do not implement a precise map pin until its location is confirmed.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Storefront header | Navigation | Home, Products, About Dony, Contact | Yes | Links target S01 `/`, S14 `/catalog`, S02 `/about`, and S03 `/contact`. |
| 2 | Page heading | Heading | “Let’s talk about your next order” | Yes | Static page heading. |
| 3 | Phone | Contact link | `090 189 3234` | As configured | Render as a tap-to-call link on supported devices. |
| 4 | Workshop and office | Address | `C2/1F Quách Điêu, Vĩnh Lộc A, Bình Chánh, TP.HCM` | As configured | Do not use the address to imply a verified map pin. |
| 5 | Website | External link | [dongphuc.dony.vn](https://dongphuc.dony.vn/) | As configured | Open the configured public website. |
| 6 | Visual location area | Illustration / map treatment | Neutral location illustration | No | Do not show a precise map pin until its location is confirmed. |
| 7 | Footer | Navigation | Existing storefront footer pattern | Yes | Repeat About and Contact links; follow the S01 storefront footer pattern. |

## 4. States

**Loading, access, errors and retry:** Show a labelled Loading state while reads resolve. A missing or inaccessible route returns a safe 401/403/404 without disclosing protected records. Error states show the API code, message, field_errors and request_id while preserving safe input. Retry transient reads; retry a mutation only with the original idempotency key and identical payload. Preserve safe user input after recoverable failures.

| State | What the user sees | Trigger |
|---|---|---|
| Success | Configured public contact details and storefront navigation. | Contact details are available |
| Empty | Hide any unavailable contact detail; do not fabricate a replacement. | A contact detail is not configured |
| Loading / error | Keep storefront navigation available; show the shared loading or failure treatment. | Content is loading or a read fails |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Home | Activate | Open the storefront home page. | S01 |
| 2 | Products | Activate | Open the public catalog. | S14 |
| 3 | About Dony | Activate | Open the About page. | S02 |
| 4 | Contact | Activate | Remain on the Contact page. | S03 |
| 5 | Phone | Activate | Start a phone call on supported devices. | External phone handler |
| 6 | Website | Activate | Open Dony's configured public website. | External website |

Portal: Guest and authenticated users. Route: `/contact`. Navigation follows the public storefront pattern on S01.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Check access and ownership on the server; never trust submitted customer, company, role, price, stage or provider status. Apply the documented 401/403/404 behavior and field rules. | Project baseline |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected versions and idempotency keys where specified. | Project baseline |
| SR-003 | Apply the owning module's lifecycle and validation rules; preserve immutable submitted snapshots and design versions. | Project baseline |
| SR-004 | Use documented project assumptions; do not invent factual company, author, client-approval or course identifiers. | Project baseline |
| S03-001 | This is a public read-only information page; do not add a contact form, submission, inbox, or response-time promise. | MFG-04/FR-001; S03 confirmed behavior |
| S03-002 | Render only configured public contacts; hide unavailable details rather than fabricating them. | S03 confirmed behavior |
| S03-003 | Do not show a precise map pin until its location is confirmed. | S03 content scope |
| S03-004 | Contact details are reported in the 21 May 2025 source and must be confirmed current before implementation. | S03 source note |

### Acceptance scenarios

1. When configured contact details are available, render those details and keep phone/website actions usable.
2. When a contact detail is unavailable, hide it without adding a substitute value.
3. Do not display a precise map pin or provide form submission on this page.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-04/FR-001 | Provides the public Contact page as part of the storefront navigation; no contact form is included. |

## 8. Responsive and accessibility notes

Support 360px through desktop. Keep headings semantic, contact links keyboard-operable with visible focus, text contrast at least 4.5:1 (3:1 for large text), and pointer targets at least 24px. Phone and external website actions must have clear accessible names. Preserve safe input after recoverable failures.

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | Confirm that the reported public contact details remain current before implementation. | No | Verify before implementation |

## 10. Sources

- [Thanh Niên — Đồng phục DONY - Xưởng may đồng phục chuyên nghiệp, giá tốt](https://thanhnien.vn/dong-phuc-dony-xuong-may-dong-phuc-chuyen-nghiep-gia-tot-185250521140043262.htm)
- [Dony Yellow Pages listing](https://www.yellowpages.com.vn/listings/1187834433/cong-ty-tnhh-may-mac-dony.html)
