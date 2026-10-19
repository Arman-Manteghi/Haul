# Security model

Haul is a tool that, by its nature, locates sensitive material. Its design is
built around one promise:

> **Haul reports exposure. It never collects, moves, or transmits a secret
> value, and it cannot be repurposed into a stealer.**

This document describes the scope, the guarantees Haul enforces, their limits,
and how to report a vulnerability.

## Scope and authorized use

- Haul scans **the current user's own account** on the local machine. Use it
  only on systems you own or are explicitly authorized to test.
- `--home` and extra paths that point at **another user's profile**, a **UNC
  path**, or a **mapped network drive** are refused (exit 64).
- Junctions and symlinks are never followed. Cloud placeholder files (OneDrive
  Files On-Demand) are skipped so a scan never triggers a download.
- Haul does not escalate privileges; it can only read what you can read.

## Guarantees and how they are enforced

### 1. `SecretValue`: an opaque wrapper
Every raw value is wrapped in `haul.core.secret.SecretValue` the moment it is
detected. `repr`, `str`, and `format` return `<redacted>`; `pickle` and `copy`
raise; equality is only defined against another `SecretValue` and uses a
constant-time comparison. The raw value is reachable only via `reveal()`.

### 2. `reveal()` allow-list (build-enforced)
An AST lint in the release pipeline parses the whole package and fails the build if
`reveal()` is called anywhere except five modules that need the raw bytes for
an in-memory purpose: masking (hashing), the output firewall (comparison),
offline validators (structure checks), the redactor (overwrite in place), and
the definition itself.

### 3. `Finding` cannot carry a secret
`haul.core.models.Finding` validates in `__post_init__` that no field — including
anything nested in `extra` — is a `SecretValue`, and that `preview` is a
`MaskedPreview`. Serializing a finding therefore cannot disclose a secret.

### 4. Non-reversible previews
A preview is a **domain-separated** SHA-256 fingerprint
(`sha256("haul:v1:" + value)`, 12 hex chars) plus, only for long high-entropy
tokens, their first 4 characters (which identify the provider, e.g. `ghp_`).
Password-like values — plaintext credentials and URL/database/netrc passwords —
never show any characters. Domain separation means public rainbow tables of
plain SHA-256 hashes do not apply.

### 5. Output firewall
Every reporter passes its rendered text through `haul.core.firewall.guard`.
The firewall holds a ledger of every raw value materialized during the run and
replaces any occurrence with a marker (warning on stderr) before anything is
written. By construction it should never fire; it exists to catch bugs.

*Limit:* values shorter than 8 characters, and plain alphabetic words up to 16
characters, are not scrubbed — such values are never rendered by construction
(they get no preview prefix), and scrubbing a word like `password` would
corrupt Haul's own report text. Real tokens and keys contain digits/symbols.

### 6. Network and process kill-switch
The CLI installs a `sys.addaudithook` that raises on socket creation, connect,
bind, send (TCP and UDP), DNS lookups, `urllib`, `subprocess`/`os.system`/
`exec`/`spawn`/`fork`, `os.startfile`, and `ctypes` loading of network
libraries (`ws2_32`, `winhttp`, `wininet`, …). Audit hooks cannot be removed
once installed, so this also binds plugins loaded later.

*Limit:* this is defense in depth for an in-process tool, not a sandbox.
Native extension code could in principle bypass Python's audit layer, which is
why the AST lint also forbids importing any networking module, and why
third-party plugins load only with `--allow-plugins`.

### 7. Canary test (build-enforced)
A canary test in the release pipeline plants fabricated secrets in every supported
location — dotfiles, CLI credentials, XML configs, MCP configs, AI
transcripts (including one 70 KB into a single line), a SQLite chat store, the
environment, private keys — runs the full engine, and fails the build if any
canary appears in any output format, in the finding dictionaries, or in any
`Finding` attribute.

## What is read, and how

| Source | Access |
|--------|--------|
| Credential/config files, `.env`, transcripts | read-only, streamed; values wrapped immediately |
| Private keys | first 8 KB only (header); key material is never decoded or emitted |
| AI SQLite chat stores | `mode=ro` (fallback `immutable=1`) + `PRAGMA query_only`; never written |
| `.git/index`, `.gitignore` | parsed read-only to decide ignored/committed; git is never executed |
| Browser stores, gcloud/Azure caches, key stores, wallets, exports | **existence only** — never opened |
| FileZilla / WinSCP / RDP | scanned for the *presence and protection* of stored-password fields; values never decoded |

## The `--clean` mode (the only write path)

- Operates **only** on `history` locations of AI tools — never configs, never a
  tool's own login file, never SQLite — and only on regular files inside your
  home that you own (not links/junctions).
- **Dry run by default**; rewriting requires `--apply` plus typing `redact`
  (or `--yes`).
- Works on bytes with `surrogateescape`: line endings, encodings and invalid
  bytes are preserved exactly; only secret spans change. Whole private-key
  blocks are redacted, not just their header.
- Writes a backup **next to** the original with the original's permissions,
  never overwriting an earlier backup; replaces the file atomically; aborts
  untouched if the file changed meanwhile (e.g. the tool is still writing).
- Never prints or transmits a value.

**Backups contain the original secrets.** Rotate the exposed credentials, then
delete the `*.haul-bak-*` files. Redaction is cleanup, not remediation.

## Reports are sensitive too

A Haul report contains no secret values, but it is a precise **map** of where
secrets live on your machine. Store and share reports as you would any
sensitive document; Haul reminds you when it writes one to disk.

## Reporting a vulnerability

If you find any way to make Haul emit, copy, or transmit a raw secret, reach
the network, or write outside `--clean`'s documented scope, please open a
**private security advisory** on the repository rather than a public issue.
Include the version, platform, and a minimal reproduction using fabricated
values. We aim to acknowledge reports within a few business days.
