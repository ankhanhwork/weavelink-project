# Demo credential boundary

Never read, display, search, attach or copy `.env` or `.env.*` except `.env.example`. Never print process environment or authorization headers. Tests must use synthetic keys and mocked transport. Do not make paid API calls unless explicitly requested.
