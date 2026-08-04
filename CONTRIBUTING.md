# Contributing to AEGIS-Core

Thank you for your interest in contributing to **AEGIS-Core** — the Cognitive Runtime Platform for AI Engineering.

---

## 🧠 Before You Start

Please read the [README.md](./README.md) to understand the architecture and boundaries of AEGIS-Core:

- **AEGIS-Core** is strictly an AI Engineering Engine (kernel, compiler, runtime, provider)
- It must never become a full platform — that is [AEGIS-Elite](https://github.com/wahyunuriman999/AEGIS-ELITE)'s domain

---

## 🛠️ Development Setup

```bash
# 1. Fork and clone
git clone https://github.com/<your-username>/AEGIS-Core.git
cd AEGIS-Core

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run tests
python -m pytest AEGIS-Tests/ -v

# 4. Run the kernel
python aegis/AEGIS-Runtime/kernel_runner.py --task "Test task"
```

---

## 📦 How to Contribute

### Reporting Bugs
1. Search [existing issues](https://github.com/wahyunuriman999/AEGIS-Core/issues) first
2. Use the **Bug Report** issue template
3. Include: OS, Python version, full error traceback

### Suggesting Features
1. Open a [Feature Request](https://github.com/wahyunuriman999/AEGIS-Core/issues/new)
2. Clearly explain: the problem, proposed solution, alternatives considered
3. Features must stay within **AEGIS-Core scope** (kernel/runtime/compiler/provider)

### Submitting Pull Requests
1. Branch from `main`: `git checkout -b feat/your-feature`
2. Follow the code style (PEP 8, docstrings, license header)
3. Add tests in `AEGIS-Tests/`
4. Run `python -m pytest AEGIS-Tests/ -v` and ensure all pass
5. Fill out the PR template completely

---

## 📋 Code Standards

### License Header
Every `.py` file **must** start with:
```python
# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
```

### Style Guide
- Follow **PEP 8**
- Max line length: **100 characters**
- All public functions must have a docstring
- No hardcoded paths — use `os.path` relative to `__file__` or project root auto-detection

### Commit Messages
Use [Conventional Commits](https://www.conventionalcommits.org/):
```
feat(kernel): add tick 5 SIMULATE opcode
fix(runtime): remove hardcoded aegis_root path
docs(readme): update architecture diagram
test(compiler): add unit tests for build.py
```

---

## 🏗️ Architecture Boundaries

| Module | Allowed | Not Allowed |
|--------|---------|-------------|
| `AEGIS-Kernel` | Memory, scheduler, dispatcher, ISA | Governance, consensus, analytics |
| `AEGIS-Runtime` | Event loop, boot, execution | Studio, marketplace, enterprise |
| `AEGIS-Compiler` | Markdown → graph pipeline | UI, API endpoints |
| `AEGIS-Provider` | LLM routing, adapters | Business logic, workflow orchestration |

---

## 🤝 Code of Conduct

Be respectful, constructive, and professional. We're building something ambitious together.

**Questions?** Open a [Discussion](https://github.com/wahyunuriman999/AEGIS-Core/discussions) or email **wahyunuriman999@gmail.com**
