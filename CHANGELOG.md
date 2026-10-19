# Changelog

All notable changes to Haul are documented here. Versions follow
[Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-10-19

The first public release.

### Scanning
- **Nine scanners in one pass**: `cloud-cli`, `ssh`, `dotenv`, `shell`, `env-vars`, `ai-tools`,
  `browsers`, `desktop-apps` and `sensitive-files`.
- **AI coding tools**: Claude Code, Claude Desktop, Cursor, VS Code (Copilot chat), Windsurf, Cline,
  Roo Code, Codex, Gemini CLI, Continue, Zed and Aider. Transcripts are streamed at any size, and SQLite
  chat stores are opened read-only.
- **58 provider rules** plus assignment, YAML, JSON and XML heuristics, two detection profiles (config and
  history), and strict false-positive filtering.
- **Git awareness**: ignored, not ignored or committed, read straight from `.git`.
- Long lines are scanned in overlapping windows, so nothing is skipped.

### Reports
- A worst-first **terminal report** with kind tags, clickable paths and one numbered fix per problem.
- A self-contained **HTML report** with search and severity filters.
- **JSON** (schema 2), formula-safe **CSV**, and **SARIF 2.1.0** with `SRCROOT`-relative paths.
- A live progress bar, `-q/--quiet`, baselines, `--min-severity` and `--fail-on`.

### Safety
- Secrets are sealed in an opaque `SecretValue`; findings carry only a non-reversible preview.
- An output firewall checks every rendered byte against the run's secrets.
- An irreversible audit hook blocks network access and subprocesses.
- Network locations (UNC paths, mapped drives) are refused before they are touched.
- `--clean` redacts secrets from AI-chat history: dry run by default, byte-exact, with a backup first.

### Exit codes
- `0`-`4` by worst severity, `64` usage error, `70` internal error, `74` I/O error, `130` interrupted.

[0.2.0]: https://github.com/Arman-Manteghi/Haul/releases/tag/v0.2.0
