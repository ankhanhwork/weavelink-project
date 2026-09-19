# MFG-02 — Profile & Settings

Implementation specification · Draft · 2026-09-19. Complete-system scope. Traceability: [function list](../docs/function-list.md), rows 12–16; shared contracts: [system decisions](../docs/system-decisions.md) D01–D03, D11; factual provenance: [user input register](../docs/user-input-needed.md).

## Purpose, access and screens

Authenticated active members view and maintain their own identity details and change password after current-password verification. The server derives identity from the session; user_id supplied by clients is ignored/rejected. This module never changes roles, company memberships or account ownership. S06 shows profile summary and edit mode for name/email, plus logout; S07 is exclusively the password-change form; S38 displays notifications. At 360px layouts stack; forms retain values on recoverable errors and provide loading, empty/error, success and retry states.

## Entities and invariants

`User(id: UUID, email: normalized globally unique, pending_email nullable, full_name: 1..100, password_hash, customer_capability, active, created_at immutable, updated_at, version)`; staff authority is per-company Membership and System Admin is a separate system capability, never a single role field. Email change requires current-password reauthentication, unique normalized pending address and single-use hashed verification token expiring in 24 hours. Old email remains active until token consumption atomically confirms global uniqueness and swaps addresses; notify old and new addresses through the outbox without exposing token. Resend invalidates prior token. Duplicate address or expired/used token returns 409. Successful change revokes other sessions. Optional text is null or trimmed text. Password is 12–128 characters with spaces; hash only. Password change requires current password and revokes all other sessions. D02 types, timestamps, versioned mutation, standard errors and session policy apply.

## Function contracts

| Function | Inputs | Output and validation |
|---|---|---|
| F-PROF-001 Profile View (FR-001) | Authenticated session; legacy `user_id` is server-derived, UUID. | `user_profile_object`: own id, full_name, email, verification state, created_at, current version. 401 unauthenticated. |
| F-PROF-002 Edit Profile Form (FR-002) | Session and current profile read; no mutation body. | S06 edit-mode view model prefilled only from own profile; editable full_name/email, with pending-email verification notice. |
| F-PROF-003 Save Profile Logic (FR-003) | `updated_fields` allowlist `{full_name,pending_email}`, current_password when changing email, `expected_version`; never role/company fields. | Save name atomically. For email change, reauthenticate, reserve unique pending email and issue 24-hour single-use verification token; do not replace current email yet. On token consumption, lock user/address uniqueness, atomically promote pending_email and clear it, then revoke other sessions and enqueue notices to old and new addresses. Stale version 409; invalid name/email/token 422; address already in use 409. Repeated token use 409. |
| F-PROF-004 Change Password Form (FR-004) | Authenticated session only. | S07 form model with current, new, confirmation inputs; secrets never returned or logged. |
| F-PROF-005 Save Password Logic (FR-005) | `old_password`, `new_password`, `confirm_password`, expected version; CSRF-valid request. | Verify current password then atomically replace hash, emit `password_changed_event`, return success alert, revoke other sessions. Wrong current password 422; mismatch/weak password 422; stale version 409. |

## Flow and acceptance

Use cases: UC-M05 View Profile (F-PROF-001); UC-M07 Edit Profile (F-PROF-002..003); UC-M08 Change Password (F-PROF-004..005). Member opens S06 → server loads session-owned profile → edit mode → submits allowlisted fields/version → for email, reauthenticate and verify pending address before swap → refreshed profile. Password flow verifies current password, policy and confirmation, saves hash, revokes other sessions and confirms on S07.

- **Given** an active member requests profile, **when** F-PROF-001 runs, **then** only that session's profile is returned; a different user ID cannot select another profile.
- **Given** a valid full_name edit with current version, **when** saved, **then** trimmed value persists and the response contains incremented version. Empty/overlong name yields field error and persists nothing.
- **Given** two profile edits use the same expected version, **when** they race, **then** one succeeds and the stale mutation returns 409 without overwriting the winner.
- **Given** a member changes email, **when** saved after password reauthentication, **then** the existing email remains active while the unique pending address is verified; only consuming the valid 24-hour token swaps email, clears pending_email, revokes other sessions and sends notices to both addresses. Duplicate or concurrently claimed address returns 409 with old email unchanged.
- **Given** the correct current password and compliant matching new password, **when** F-PROF-005 commits, **then** the new hash works, old password fails, current session remains valid and other sessions are revoked.
- **Given** wrong current password, weak password or mismatched confirmation, **when** submitted, **then** a field-safe error appears, no hash changes and secret values are cleared from the form.
- **Given** a signed-out user calls any profile function, **when** authorized, **then** request fails with 401; staff cannot edit another user's profile by changing a URL.

## Errors and traceability

Use D02 error envelope; do not reveal hashes, reset tokens or passwords. Database outage returns 503 with submitted nonsecret profile values retained. All five source function IDs map one-to-one to FR-001..FR-005 above. Historical MVP scope exclusions do not remove these functions from the complete system.
