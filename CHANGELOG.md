# Changelog

All notable changes to **AEGIS-Core** will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and [Semantic Versioning](https://semver.org/).

---

## [v12.1.0] — 2026-08-04

### Added
- `requirements.txt` — first-time install now works (`pip install -r requirements.txt`)
- `CONTRIBUTING.md` — contribution guide, code style, commit format, architecture boundaries
- `.github/workflows/test.yml` — GitHub Actions CI for Python 3.10 / 3.11 / 3.12
- `CHANGELOG.md` — this file
- `SECURITY.md` — vulnerability reporting policy
- Real LLM provider adapters: `OpenAIProvider`, `AnthropicProvider`, `GeminiProvider`, `OllamaProvider`
- Auto-detection of providers from environment variables (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, `OLLAMA_HOST`)
- `SimulationProvider` — non-blocking fallback when no API keys are configured
- `docs/ARCHITECTURE.md` — architecture overview document
- `docs/ISA.md` — full Cognitive Instruction Set reference

### Fixed
- **Hardcoded path** in `kernel_runner.py` — replaced with `os.path.dirname(os.path.abspath(__file__))`
- **Hardcoded path** in `build.py` — replaced with auto-detect

### Changed
- `provider_manager.py` fully refactored — real routing with graceful simulation fallback

---

## [v12.0.0] — 2026-07-01

### Added
- AEGIS Virtual Machine (`AegisVirtualMachine`) with 11-tick ISA pipeline
- Knowledge Compiler (`build.py`, `knowledge_compiler.py`) — Markdown → AST → Runtime Graph
- Memory Hierarchy (L0–L5) mount system
- Event Dispatcher with real capability routing
- `capability_registry.md` — SSOT for capability-to-model mapping
- `FAILURE_DB.json` — failure pattern database
- `REFLECTION_LOG.md` — cognitive reflection logs
- `routing.json` — model routing configuration
- `install.sh` / `install.ps1` — cross-platform installers
- GitHub community files: `ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE.md`

### Architecture
- AEGIS-Kernel: boot, clock, scheduler, dispatcher, memory, instruction set, events, state
- AEGIS-Runtime: event loop, kernel runner
- AEGIS-Compiler: build pipeline
- AEGIS-Provider: multi-LLM routing
- AEGIS-Specification: ABI spec, capability registry

---

## [v11.0.0] — 2026-06-01

### Added
- Initial AEGIS Cognitive Runtime Platform release
- 4-Tick pipeline: OBSERVE → PLAN → EXECUTE → REFLECT
- Basic memory hierarchy (L1–L3)
- Provider interface definition
