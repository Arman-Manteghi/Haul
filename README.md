<h1 align="center">
  <img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/banner.svg?v=0.2.0" alt="Haul: credential exposure scanner for developer machines" width="900">
</h1>

<h3 align="center">If an infostealer ran on your machine right now, what would it take?</h3>

<p align="center">
  Haul finds every API key, token, SSH key and password lying where stealer malware looks first,<br>
  scores how exposed each one is, and tells you exactly how to fix it.<br>
  <b>It never reads a secret out. Read-only, offline, zero dependencies.</b>
</p>

<p align="center">
  <a href="https://pypi.org/project/haul-scanner/"><img alt="PyPI" src="https://img.shields.io/pypi/v/haul-scanner?style=flat-square&label=pypi&labelColor=11151c&color=3d5a7a&cacheSeconds=3600"></a>
  <img alt="Python 3.11 to 3.14" src="https://img.shields.io/badge/python-3.11%20%E2%80%93%203.14-4a5568?style=flat-square&labelColor=11151c">
  <img alt="Windows and Linux" src="https://img.shields.io/badge/platform-windows%20%C2%B7%20linux-3f6b66?style=flat-square&labelColor=11151c">
  <img alt="Zero runtime dependencies" src="https://img.shields.io/badge/dependencies-0-5b4f73?style=flat-square&labelColor=11151c">
  <img alt="No network access" src="https://img.shields.io/badge/network-none-7a4442?style=flat-square&labelColor=11151c">
  <img alt="Typed with mypy strict" src="https://img.shields.io/badge/typed-mypy%20strict-7a5a3d?style=flat-square&labelColor=11151c">
  <a href="#license"><img alt="License: free to use" src="https://img.shields.io/badge/license-free%20to%20use-4a5568?style=flat-square&labelColor=11151c"></a>
</p>

```bash
pip install haul-scanner
```

<p align="center">
  <a href="#why-haul">Why</a> ·
  <a href="#what-you-get">Features</a> ·
  <a href="#see-it-in-action">Screenshots</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#what-it-scans">Coverage</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#safety-model">Safety</a> ·
  <a href="#use-it-in-ci">CI</a> ·
  <a href="#faq">FAQ</a>
</p>

<br>

> **Defensive use only.** Haul is a read-only self-audit tool. Run it on systems you own or are
> explicitly authorized to test. It scans the current user's own account, refuses other users'
> profiles and network paths, and makes **zero** network connections.

## Why Haul

Infostealers don't need an exploit. They run once **as you**, then sweep everything you can already read:

- **cloud and package-registry credentials**: `~/.aws`, `gcloud`, `az`, `kubeconfig`, `.npmrc`, `.pypirc`
- **SSH keys** with no passphrase, **`.env` files** in every project folder, shell and PowerShell **history**
- and, increasingly, the **chat history of AI coding tools**, where keys get pasted and `.env` files get echoed back

Most secret scanners look at **repositories**. Haul looks at **your machine**: the home folder, project
folders, app-data stores and AI-tool transcripts that never reach a repo but sit on disk, readable by
anything you run. It reports, ranks and explains. It never takes.

## What you get

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/icons/scanners.svg?v=0.2.0" width="46" align="left" alt="">
      <b>Nine scanners, one pass</b><br>
      <sub>Cloud &amp; package CLIs, SSH keys, <code>.env</code> files, shell &amp; PowerShell history, environment variables, 12 AI coding tools, browsers, desktop apps and sensitive files.</sub>
    </td>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/icons/ai.svg?v=0.2.0" width="46" align="left" alt="">
      <b>AI-history aware</b><br>
      <sub>Claude Code, Cursor, Copilot, Windsurf, Codex, Gemini CLI and more. Streams transcripts of any size and reads SQLite chat stores read-only. A key echoed 500× is one finding.</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/icons/git.svg?v=0.2.0" width="46" align="left" alt="">
      <b>Git aware</b><br>
      <sub>Knows whether a <code>.env</code> is ignored, <i>not</i> ignored, or already <b>committed</b>, by reading <code>.git</code> directly. Git is never executed.</sub>
    </td>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/icons/scoring.svg?v=0.2.0" width="46" align="left" alt="">
      <b>Real risk, not noise</b><br>
      <sub>58 provider rules plus assignment, YAML, JSON and XML heuristics. Aggressive false-positive filtering, and a 0–100 exposure score for every finding.</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/icons/sealed.svg?v=0.2.0" width="46" align="left" alt="">
      <b>Never discloses a value</b><br>
      <sub>Secrets are sealed in memory the moment they are found. Reports carry only a non-reversible fingerprint, and an output firewall double-checks every byte.</sub>
    </td>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/icons/network.svg?v=0.2.0" width="46" align="left" alt="">
      <b>Zero network, zero dependencies</b><br>
      <sub>An irreversible audit hook blocks sockets, DNS and subprocesses for the whole run. Pure standard library, so there is no supply chain to attack.</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/icons/reports.svg?v=0.2.0" width="46" align="left" alt="">
      <b>Reports people actually read</b><br>
      <sub>A worst-first terminal view with clickable paths, a self-contained HTML report, plus JSON, CSV and SARIF 2.1.0.</sub>
    </td>
    <td width="50%" valign="top">
      <img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/icons/ci.svg?v=0.2.0" width="46" align="left" alt="">
      <b>Built for CI</b><br>
      <sub>Exit codes by severity, <code>--fail-on</code>, baselines that survive edits, and SARIF that maps straight onto your repository's files.</sub>
    </td>
  </tr>
</table>

## See it in action

Run `haul` and it walks your machine once. The live progress bar keeps moving even through hundreds of
megabytes of AI transcripts.

<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/startup.svg?v=0.2.0" alt="Haul starting: the banner and the live progress bar" width="640"></p>

The report is **worst first**. Every finding names its kind (`API KEY`, `TOKEN`, `PRIVATE KEY`,
`PASSWORD`…), what it is and where it lives. Paths are **clickable** in modern terminals, and each fix
appears **once**, numbered, under *What to do*.

<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/terminal-report.svg?v=0.2.0" alt="Haul terminal report, worst findings first" width="840"></p>

Need to hand it to someone? `haul -f html -o report.html` writes **one self-contained file** with live
search, severity filters and the same fixes. It needs no internet and loads nothing external.

<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/html-report.png?v=0.2.0" alt="Haul HTML report with search and severity filters" width="840"></p>

<details>
<summary><b>The HTML report filtered to one severity</b></summary>
<br>
<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/html-report-filter.png?v=0.2.0" alt="Haul HTML report filtered to High findings" width="840"></p>
</details>

<sub>Every screenshot is real Haul output, captured on a demo profile seeded with fabricated secrets.</sub>

## Quick start

Install it once, then run it as any normal user. Haul needs **Python 3.11+** and nothing else.

```bash
pip install haul-scanner
```

<details>
<summary>Prefer an isolated install? Use <b>pipx</b> or <b>uv</b>.</summary>

```bash
pipx install haul-scanner
```

```bash
uv tool install haul-scanner
```
</details>

| Run this | To get |
|---|---|
| `haul` | The full scan: terminal report, worst first |
| `haul --min-severity high` | Only what matters most |
| `haul -f html -o haul-report.html` | A readable, shareable HTML report |
| `haul --only ai-tools` | Just your AI coding tools' history and configs |
| `haul --clean` | A dry run of redacting secrets from AI-chat history |
| `haul --list-scanners` | Every scanner and what it covers |

## What it scans

<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/scanners.svg?v=0.2.0" alt="haul --list-scanners output" width="840"></p>

| Scanner | What it covers |
|---|---|
| **`cloud-cli`** | AWS (static keys, SSO and CLI caches), Azure, gcloud, kubeconfig, Docker, npm, Yarn, PyPI, Cargo, RubyGems, Composer, NuGet, Maven, Terraform Cloud, Vault, `.netrc` / `_netrc`, GitHub CLI and `.git-credentials`, resolved per OS. |
| **`ssh`** | `~/.ssh` plus every `IdentityFile` in `~/.ssh/config`. OpenSSH, PEM, PKCS#8 and PuTTY `.ppk`, flagging keys with **no passphrase**. Reads only the header; key material is never decoded. |
| **`dotenv`** | `.env`, `.env.*`, `.npmrc`, `.yarnrc.yml` and `.pypirc` across your project folders. Templates such as `.env.example` are skipped. Scored higher when not git-ignored, much higher when **committed**. |
| **`shell`** | bash, zsh and fish rc files, **PowerShell profiles**, and PSReadLine, bash, zsh and REPL histories, using a stricter detection profile built for history. |
| **`env-vars`** | Secret-looking variables in the environment Haul inherited. The report names the *variable*, never its value. |
| **`ai-tools`** | **Claude Code, Claude Desktop, Cursor, VS Code (Copilot chat), Windsurf, Cline, Roo Code, Codex, Gemini CLI, Continue, Zed and Aider**: transcripts, configs, MCP `env` blocks, the tools' own login files and SQLite chat stores. |
| **`browsers`** | **Presence only**: Chrome, Edge, Brave, Chromium, Vivaldi, Opera and Firefox password and cookie stores, plus how this OS protects them. Never opened. |
| **`desktop-apps`** | FileZilla (plaintext vs. master password), portable WinSCP, saved RDP passwords, OpenVPN profiles with inline keys. Presence and protection only. |
| **`sensitive-files`** | Key stores (`.pfx`, `.p12`, `.jks`, `.kdbx`), crypto wallets, password-manager and browser **exports**, and stray private keys like an EC2 `.pem` in Downloads. |

Haul walks your working folders **once** into a shared inventory. It skips `node_modules` and build output,
never follows symlinks or junctions, never touches network drives, and skips cloud-only OneDrive files, so
a scan can never trigger a download.

## How it works

<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/pipeline.svg?v=0.2.0" alt="Haul's pipeline: read, provider rules, heuristics, filters, seal, then mask, score, firewall, report" width="900"></p>

- **Specific beats generic.** Provider rules run first and claim their match, so an Anthropic key is
  reported once as Anthropic, never again as "OpenAI-shaped". Literal prefilters skip rules that can't
  match a line, which keeps multi-hundred-megabyte transcripts fast.
- **Two detection profiles.** Config files also report plaintext passwords under strong keys
  (`DB_PASSWORD=…`). History (transcripts, shell history, logs) reports only tokens and high-entropy
  values, because prose and code samples are full of `password: …`.
- **Noise is filtered out.** Haul drops placeholders (`your-token-here`), references (`${DB_PASSWORD}`,
  `op://…`), UUIDs, paths, URLs and token counters (`max_tokens`).
- **Nothing is skipped.** AI tools often write a whole conversation on one JSON line. Haul scans long
  lines in overlapping 64 KB windows and streams large files, so memory stays flat.
- **Optional offline validation.** `--verify-format` checks structure (JWT expiry, key shapes, GitHub
  token checksums) to cut false positives further, entirely in memory.

## Severity and scoring

<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/scoring.svg?v=0.2.0" alt="Haul scoring: base severity plus exposure modifiers, mapped to Info, Low, Medium, High and Critical" width="900"></p>

Every finding gets a **0–100 score**: a base severity, moved by how exposed the secret really is. The bands
are **≥ 85 Critical**, **≥ 65 High**, **≥ 40 Medium** and **≥ 20 Low**; anything lower is Info. The worst
severity becomes the exit code.

**A finding tells you everything except the secret:**
- its type, file, line, and how many times it occurs
- a **non-reversible preview**: a domain-separated SHA-256 fingerprint, plus the first 4 characters
  *only* for long random tokens, where they merely name the provider (`ghp_`, `AKIA`). Passwords never
  show a single character.
- its protection (passphrase, DPAPI, master password, none), inferred scope (a long-lived `AKIA` key vs. a
  temporary `ASIA` one), and a concrete fix

| Exit code | Meaning |
|:---:|---|
| `0` | Nothing at or above `--fail-on` (default `low`) |
| `1` · `2` · `3` · `4` | Worst finding is Low · Medium · High · Critical |
| `64` | Usage error: a bad flag, an unknown scanner name, a refused path |
| `70` · `74` | Internal error · I/O error |
| `130` | Interrupted (Ctrl+C) |

## Reports

| Format | Best for |
|---|---|
| `terminal` *(default)* | Reading at a glance. Colors and clickable paths when interactive, plain text when piped. |
| `html` | Handing to a person. One standalone file with search, filters and cards. |
| `json` | Automation. Schema 2 with summary, findings and errors. |
| `csv` | Spreadsheets. Hardened against formula injection. |
| `sarif` | Code scanning. SARIF 2.1.0 with paths relative to `SRCROOT` and stable fingerprints. |

Write several at once into a folder:

```bash
haul -f terminal -f html -f json -f csv -f sarif -o ./reports
```

<details>
<summary><b>What the JSON looks like</b></summary>

```json
{
  "tool": "haul",
  "version": "0.2.0",
  "schema": 2,
  "summary": {
    "total": 20, "unique_secrets": 15, "files_scanned": 5,
    "by_severity": { "Critical": 11, "High": 4, "Medium": 5, "Low": 0, "Info": 0 },
    "highest_severity": "Critical", "exit_code": 4, "elapsed_seconds": 0.02
  },
  "findings": [
    {
      "secret_type": "AWS Access Key ID",
      "severity": "Critical", "score": 92,
      "file": "C:\\Users\\dev\\.aws\\credentials", "line": 2, "occurrences": 1,
      "preview": "AKIA…[sha256:a108299cdc4e len=20]",
      "fingerprint": "a108299cdc4e",
      "protection": "none", "scope": "long-lived IAM user key",
      "remediation": "Prefer `aws sso login` / IAM Identity Center or short-lived STS credentials; …",
      "baseline_key": "cloud-cli|AWS Access Key ID|C:\\Users\\dev\\.aws\\credentials|a108299cdc4e"
    }
  ],
  "errors": []
}
```
</details>

## Command-line reference

| Option | What it does |
|---|---|
| `paths…` | Extra project folders to include (on this machine) |
| `--home DIR` | Scan this home instead of yours. Other users' profiles and network paths are refused. |
| `--only` · `--skip SCANNERS` | Choose scanners (comma-separated or repeated). Unknown names are an error, never ignored. |
| `--max-depth N` | How deep to walk project folders (1–32, default 6) |
| `--verify-format` | Offline structural validation to cut false positives |
| `--allow-plugins` | Load third-party scanners from the `haul.scanners` entry point |
| `-f, --format` | `terminal`, `html`, `json`, `csv`, `sarif` (repeatable) |
| `-o, --output` | A file for one format, or a folder for several |
| `--min-severity` | Only report findings at or above this severity |
| `--fail-on` | Exit non-zero only when a finding reaches this severity |
| `--baseline FILE` | Hide the findings recorded in a previous JSON report |
| `--no-color` · `-q, --quiet` | No colors · no banner, progress or notices |
| `--clean [--apply] [--yes] [--no-backup]` | Redact secrets from AI-tool history ([details](#cleaning-ai-chat-history)) |
| `--list-scanners` · `--version` | List the scanners · print the version |

<details>
<summary><b>The full <code>haul --help</code></b></summary>
<br>
<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/help.svg?v=0.2.0" alt="haul --help output" width="780"></p>
</details>

## Use it in CI

Haul makes a good gate. Fail on High or worse, and send SARIF to GitHub code scanning. Paths are relative
to the folder Haul runs in, so findings land on the right files.

```yaml
name: secrets
on: [push, pull_request]
permissions:
  contents: read
  security-events: write
jobs:
  haul:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install haul-scanner
      - name: Scan the repository
        run: haul --only dotenv,sensitive-files -f sarif -o haul.sarif --fail-on high -q "$GITHUB_WORKSPACE"
      - if: always()
        uses: github/codeql-action/upload-sarif@v3
        with: { sarif_file: haul.sarif }
```

**Baselines** accept known findings and fail only on new ones. They ignore line numbers, so editing a file
doesn't bring an accepted finding back:

```bash
haul -f json -o baseline.json        # record today's state once
haul --baseline baseline.json        # from now on, only new findings
```

## Cleaning AI-chat history

A key pasted into an AI chat stays in its transcript for good. `--clean` removes it. This is the **only**
mode that writes to disk, and it is deliberately careful:

<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/clean-dry-run.svg?v=0.2.0" alt="haul --clean dry run" width="640"></p>

- **A dry run by default.** It lists what would change. Rewriting needs `--apply`, then typing `redact` (or `--yes`).
- **History only.** It never touches configs, a tool's own login file (that would log you out) or SQLite stores, and only works on regular files you own inside your home.
- **Byte-exact.** It works on raw bytes, so line endings and encodings survive unchanged. Whole private-key blocks are redacted, not just their first line.
- **Backup first.** It writes a backup with the same permissions, never overwrites an earlier one, replaces the file atomically, and backs off if the file changes mid-way.
- **Never discloses.** Each secret becomes a non-reversible marker: `«haul-redacted:sha256:…»`.

> **Rotate first.** The `*.haul-bak-*` backups still contain the original secrets. Rotate the exposed
> credentials, then delete the backups. Redaction is cleanup, not remediation.

## Safety model

A tool that knows where every secret lives must be impossible to turn into a stealer. Haul enforces that in
layers, each of which would stop a leak on its own:

<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/safety.svg?v=0.2.0" alt="Haul safety layers around the sealed SecretValue" width="900"></p>

| Layer | Guarantee |
|---|---|
| **SecretValue** | Raw values are sealed the moment they're found. `repr`, `str` and `format` give `<redacted>`; `pickle` and `copy` refuse; comparison is constant-time. |
| **Masking** | Previews are a domain-separated SHA-256 fingerprint, plus a provider prefix for long tokens only. Just five internal modules may unseal a value, and the release build fails if any other code tries. |
| **Finding** | A finding validates itself and refuses to hold a sealed value anywhere, even nested. The only secret-derived field is the masked preview. |
| **Output firewall** | Every rendered report is checked against the secrets seen in this run before a single byte is written. |
| **Network kill-switch** | An irreversible audit hook blocks sockets, connects, DNS, `subprocess`, `exec`, `os.startfile` and loading network libraries. Network paths are refused before they are touched. |
| **Build gates** | Fabricated secrets are planted in every supported location, and the release fails if any of them shows up in any output format. |

The full threat model, and its honest limits, is in **[SECURITY.md](https://github.com/Arman-Manteghi/Haul/blob/main/SECURITY.md)**.

## Inside the package

One focused package, written against the standard library only and fully typed. Each layer has a single job:

<p align="center"><img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/architecture.svg?v=0.2.0" alt="Haul package layout: interface, engine, detection, scanners, safety and remediation layers" width="900"></p>

## Plugins

Third-party scanners plug in through an entry point and load only with `--allow-plugins`. They inherit
every safety layer above, including the network kill-switch.

```python
from collections.abc import Iterator

from haul.core.context import ScanContext
from haul.core.models import Finding, ScanCategory
from haul.core.registry import register
from haul.scanners.base import Scanner


@register
class MyToolScanner(Scanner):
    name = "my-tool"
    category = ScanCategory.CLOUD_CLI
    description = "Credentials written by my-tool"

    def scan(self, ctx: ScanContext) -> Iterator[Finding]:
        path = ctx.home_path(".mytool", "config")
        if path.is_file():
            yield from self.scan_file(ctx, path, remediation="Run `mytool login --keychain`.")
```

```toml
[project.entry-points."haul.scanners"]
my-tool = "my_package.haul_plugin"
```

## Performance

<table>
  <tr>
    <td align="center" width="25%"><h3>1 walk</h3><sub>Your folders are read once into a shared inventory, not once per scanner.</sub></td>
    <td align="center" width="25%"><h3>~15 MB/s</h3><sub>per core on AI transcripts, thanks to literal prefilters and keyword-driven parsing.</sub></td>
    <td align="center" width="25%"><h3>~100 s</h3><sub>for a full scan of a laptop holding 1.2 GB of AI transcripts.</sub></td>
    <td align="center" width="25%"><h3>Flat memory</h3><sub>Large files are streamed and long lines windowed. Nothing is loaded whole.</sub></td>
  </tr>
</table>

## FAQ

<details>
<summary><b>Does Haul upload or send anything?</b></summary>

No. It makes zero network connections, and an audit hook enforces that at runtime: sockets, DNS,
subprocesses and network libraries are blocked for the whole process. Reports are written only where you
point `-o`, or to your terminal.
</details>

<details>
<summary><b>Does it read my browser passwords?</b></summary>

No. Browser stores are reported by **presence only**, together with the protection that guards them on your
OS. Haul never opens, decrypts, parses or counts their contents.
</details>

<details>
<summary><b>Why do some previews show 4 characters and others none?</b></summary>

For long random tokens the first 4 characters only name the provider (`ghp_`, `AKIA`, `sk_l`) and reveal
nothing useful. For passwords, the first characters are part of the secret, so Haul shows none.
</details>

<details>
<summary><b>It found a key in an AI chat I deleted long ago. Is that real?</b></summary>

Almost certainly. Many AI tools keep transcripts and SQLite chat stores long after a conversation disappears
from the UI. Rotate the key, then run `haul --clean` to remove it from the history files.
</details>

<details>
<summary><b>Does it scan git history?</b></summary>

It reads `.git` to tell you a file is **committed** (and scores it higher), but it doesn't walk old commits.
Rotate anything that was ever committed, and use a history scanner for the rest.
</details>

<details>
<summary><b>Why is the package called <code>haul-scanner</code>?</b></summary>

The name `haul` was already taken on PyPI. The command you run is still simply `haul`.
</details>

<details>
<summary><b>Is Haul open source?</b></summary>

No. Haul is free to use, for personal and commercial work, but it is not open source. It is distributed
through PyPI under its own license; see [License](#license).
</details>

<details>
<summary><b>Does it run on macOS?</b></summary>

Haul knows the macOS locations of every supported tool, but macOS is not yet a verified platform. Windows
(the primary target) and Linux are.
</details>

## Limitations

- **Heuristic by nature.** Expect occasional false positives and misses. `--verify-format` and baselines help.
- **The working tree only.** Git history beyond the index is out of scope.
- **Presence-only stores** (browsers, gcloud and Azure caches, key stores) are reported, never inspected.
- **No Windows Registry reads.** WinSCP sessions stored in the registry, for example, are not covered.
- **Defense in depth, not a sandbox.** The kill-switch binds everything that goes through Python's audit
  layer; native extension code could bypass it, which is why plugins are opt-in.

## Security

Found a way to make Haul emit, copy or transmit a secret, reach the network, or write outside `--clean`'s
scope? Please report it privately through
**[a security advisory](https://github.com/Arman-Manteghi/Haul/security/advisories/new)**, not a public issue.

> **Reports are sensitive too.** They contain no secret values, but they are a precise map of where
> secrets live on a machine. Store and share them like any sensitive document.

## License

**Free to use, all rights reserved.** Haul is proprietary freeware © 2026 Arman Manteghi.

| You may | You may not |
|---|---|
| Install and run Haul for free, personally or commercially | Modify it, or redistribute, resell or sublicense it |
| Use it on systems you own or are authorized to assess | Remove its copyright or license notices |
| Keep the unmodified package in an internal mirror | Use it against systems you aren't authorized to assess |

The binding text is in **[LICENSE](https://github.com/Arman-Manteghi/Haul/blob/main/LICENSE)**.

<br>

<p align="center">
  <img src="https://raw.githubusercontent.com/Arman-Manteghi/Haul/main/docs/assets/icons/sealed.svg?v=0.2.0" width="30" alt=""><br>
  <sub>Built by <a href="https://github.com/Arman-Manteghi"><b>Arman Manteghi</b></a></sub><br>
  <sub>Read-only · zero network · zero dependencies · no secret ever leaves the process</sub>
</p>
