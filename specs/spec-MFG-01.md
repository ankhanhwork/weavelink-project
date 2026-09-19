# MFG-01 — Identity & Access

Implementation specification · Draft · 2026-09-19. Scope covers the complete system. Function/source traceability: [function list](../docs/function-list.md), rows 1–11; shared rules: [system decisions](../docs/system-decisions.md) D01–D03; factual provenance and pending human inputs: [user input register](../docs/user-input-needed.md).

## Purpose, roles and screens

Provide account creation, authentication, session termination and account recovery for customers and provisioned staff. Assignable roles are Customer, Sales Consultant, Company Admin and System Admin. Public registration creates Customer only. Staff accounts and company memberships are provisioned by System Admin. A Member means an authenticated active user. Authorization is enforced server-side; inaccessible objects return 404, missing authentication 401 and prohibited actions 403. Do not accept role, user ID or company membership from a client as authority.

Screens: S02 registration; S03 sign-in; S04 forgot password; S05 reset password; S06 profile/session entry; S08 public landing/catalog entry. S06 logout invokes F-USER-006. Forms expose loading, validation, error, success and retry states; preserve input on recoverable failure. Route redirects accept internal allowlisted destinations only.

## Entities and shared constraints

`User(id: UUID,email: normalized globally unique,full_name,password_hash,customer_capability:boolean,email_verified_at?,active,created_at,updated_at,version)`; `Membership(id,company_id,user_id,role:Company Admin|Sales Consultant,active,version)`; `SystemCapability(user_id,role:System Admin,active)`; `Session(id,user_id,token_hash,created_at,idle_expires_at,absolute_expires_at,revoked_at?)`; `OneTimeToken(id,user_id,purpose,token_hash,expires_at,consumed_at?)`. Do not model staff authority as one global `User.role`: authorization resolves Customer capability, active company Membership and system capability separately; staff selects only an active authorized company. Email is globally unique and case-normalized. Name is 1–100 characters. Password is 12–128 characters, spaces allowed, stored as a password hash. Verification links expire in 24 hours, reset links in 30 minutes; tokens are random, stored hashed, single-use and replaced on resend. Sessions use Secure, HttpOnly, SameSite=Lax cookies, CSRF protection, 30-minute idle and 24-hour absolute expiry. After five failed login attempts in 15 minutes, return the ordinary generic credential failure for attempt five; subsequent attempts in the account/IP window return 429 until the window clears. Link requests: 3/account/IP/hour. Generic reset responses do not expose account existence. D02 errors, UUIDs, UTC timestamps, version checks and idempotency apply.

## Function contracts (all IDs retained)

| Function | Actor | Inputs and validation | Result / behavior |
|---|---|---|---|
| F-USER-001 Registration Screen (FR-001) | Guest | No business body; route/session context only. | S02 view model: full name, email, password and confirmation fields; consent/verification explanation. |
| F-USER-002 Registration Logic (FR-002) | Guest | `full_name` 1–100; `email` valid and normalized; `password` 12–128; confirmation equal. | Transaction creates Customer capability inactive pending verification and returns user summary plus generic success. Invalid fields: 422; duplicate global email: 409. |
| F-USER-003 Send Verification (FR-003) | Guest/System | `user_id` is server-derived from registration; resend takes email and is rate-limited. | Create one 24-hour verification token and enqueue email atomically. SMTP delivery is secondary; failed delivery remains retryable and never exposes token in logs. Verification activates account once; expired/consumed token is rejected. |
| F-USER-004 Login Screen (FR-004) | Guest | No body; route/session context. | S03 view model with email and password inputs and generic recovery link. |
| F-USER-005 Authentication Logic (FR-005) | Guest | `username_email`, `password`; normalized email; rate limits above. | Valid verified active user receives revocable server session, Customer capability plus active membership/system capabilities and safe internal redirect. Invalid credentials return generic 401; unverified account gets resend guidance without session; after five failures later attempts are rate-limited 429. New invited staff may use S03 invitation mode to consume a valid invitation and set full_name/password; existing identities must authenticate before accepting membership. |
| F-USER-006 Logout Logic (FR-006) | Member | Current session from secure cookie; no client-supplied token. | Revoke session, clear cookie/local transient auth state, return `session_invalidated=true`; navigate S03. Repeated logout is successful no-op. |
| F-USER-007 Forgot Password Screen (FR-007) | Guest/Member | No body; S04 form asks registered email. | S04 recovery form view model; never prefill or reveal account status. |
| F-USER-008 Identity Validation (FR-008) | Guest/Member | `email_address_or_phone_number` normalized email; 3 requests/hour. | Return generic `accepted` whether account exists; for eligible account enqueue reset issuance. No phone channel is enabled in this release. |
| F-USER-009 Send Reset Link (FR-009) | System | Server-derived user ID and email delivery channel. | Issue single-use 30-minute token and enqueue HTTPS internal reset URL. Outbox retries after 1, 5, 30 minutes; failed delivery is visible to operations. |
| F-USER-010 Verify Token Logic (FR-010) | Guest | `reset_token` opaque token; purpose and expiry checked against hash. | Return `valid` only for unconsumed, unexpired token and allow reset form; otherwise `invalid_or_expired`, without revealing account details. Concurrent consumption permits only one winner. |
| F-USER-011 Update Password Logic (FR-011) | Guest with valid reset token | `new_password`, `confirm_password`; policy above; token valid at commit. | Atomically consume token, replace hash and revoke all user sessions. Return confirmation and updated user summary. Stale/used token 409; weak/mismatch 422. |

## Flows and acceptance

Registration: guest submits S02 → validate and create inactive Customer → send verification → user follows link → activate → sign in at S03 → safe destination or S08. Authentication: guest submits credentials → rate limit and verify → establish session → route. Recovery: submit email → generic acknowledgement → email link → token check → submit new password → consume token and revoke sessions. Sign-out revokes the current session.

Use cases: UC-G03 Register Account (F-USER-001..003); UC-M01 Log In (F-USER-004..005); UC-M04 Log Out (F-USER-006); UC-M02 Forgot Password (F-USER-007..009); UC-M03 Reset Password (F-USER-010..011).

- **Given** a new valid email and matching policy-compliant password, **when** the guest registers, **then** one pending Customer and one verification outbox event exist; retrying with the same email produces 409 without a second account.
- **Given** an unverified account, **when** correct credentials are submitted, **then** no session is issued and the UI offers verification resend; after successful verification the same credentials establish a session.
- **Given** invalid credentials, **when** a login is attempted, **then** attempts one through five return generic 401 and subsequent attempts in the 15-minute account/IP window return 429; account existence is not disclosed.
- **Given** any submitted reset email, **when** recovery is requested, **then** the same acknowledgement is returned; known accounts receive a single-use link and unknown addresses reveal nothing.
- **Given** two requests consume the same valid reset token concurrently, **when** both attempt password update, **then** exactly one commits; the other receives 409 and the winning update revokes existing sessions.
- **Given** an expired, resent or consumed token, **when** it is opened or submitted, **then** the form reports an expired/invalid link and offers a new recovery request.
- **Given** a signed-in user logs out twice, **when** either request reaches the server, **then** access is revoked on the first call and the second is an idempotent success; protected routes then return 401.
- **Given** a login redirect contains an external URL, **when** authentication succeeds, **then** the redirect is discarded and the safe default is used.

## Errors and operations

Use common D02 error envelope/status codes. Preserve forms on 422/503. Email outage does not roll back account/token state; show generic next steps and keep delivery retryable. Audit auth outcomes without passwords, raw tokens or secrets. Trace each FR to the corresponding F-USER identifier above; no implementation scope is excluded by historical MVP notes.
