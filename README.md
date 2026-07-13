<!--
# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman.
# All rights reserved.
# ==========================================
-->
<div align="center">

[![AEGIS](https://img.shields.io/badge/AEGIS-v12.0_Cognitive_Runtime-blue?style=for-the-badge)](https://github.com/wahyunuriman999/AEGIS-Core)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()
[![Tier](https://img.shields.io/badge/Tier-Open_Source-brightgreen?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-Copyrighted-red?style=for-the-badge)]()

# AEGIS

### The Cognitive Runtime Platform for AI Engineering

*Engineering Intelligence Beyond the Language Model.*

[ [Architecture](#architecture) ] • [ [Installation](#installation) ] • [ [Usage](#usage) ] • [ [Tests](#tests) ] • [ [AEGIS Elite](#aegis-elite) ] • [ [FAQ](#faq) ]

</div>

---

## What is AEGIS?

AEGIS is a cognitive runtime layer that sits between the user and a language model. Instead of sending raw prompts, AEGIS structures reasoning into a formal pipeline — with planning, simulation, validation, and reflection — before any output is produced.

Language models are powerful, but they have no native scheduler, no memory hierarchy, and no way to enforce deterministic behavior. AEGIS adds that infrastructure.

---

## Architecture

AEGIS is divided into focused subsystems:

### Runtime Pipeline

```
User Intent → Planner → Scheduler → Knowledge + Genome
                                          ↓
                               Simulation → Validation
                                          ↓
                               Reflection → Memory Update → Output
```

### Kernel

Manages the lifecycle of the reasoning process.

```
Boot → Clock → Scheduler → Dispatcher → Memory → Instruction → Event Bus → Runtime Ready
```

### Memory Hierarchy

Modeled after CPU cache layers:

| Layer | Name | Contents |
|-------|------|----------|
| L1 | Working Memory | Active task context |
| L2 | Context Memory | Broader project state |
| L3 | Knowledge Memory | Engineering rules and patterns |
| L4 | Experience Memory | Past failures and successes |
| L5 | Evolution Memory | The Engineering Genome |

### Knowledge Compiler

Converts documentation and guidelines into structured runtime graphs, rather than raw prompt text.

```
Markdown → Parser → AST → Knowledge Graph → Instruction Graph → Execution Graph → Runtime Image
```

### Cognitive Instruction Set (ISA)

AEGIS executes reasoning through strict opcodes, not freeform prompts:

| Opcode | Name | Description |
|--------|------|-------------|
| `0x01` | OBSERVE | Read and understand current context |
| `0x02` | RETRIEVE | Fetch relevant knowledge |
| `0x03` | INFER | Draw conclusions from data |
| `0x04` | PLAN | Build execution graph |
| `0x05` | SIMULATE | Test plan before executing |
| `0x06` | VALIDATE | Check output against rules |
| `0x07` | EXECUTE | Apply changes |
| `0x08` | REFLECT | Review what happened |
| `0x09` | LEARN | Update memory and genome |

### Provider Layer

AEGIS routes tasks to the right model based on capability, not by name.

```
Cognitive Runtime → Provider Interface → OpenAI / Claude / Gemini / Ollama / 9Router / LiteLLM
```

---

## Current Capabilities

What is actually running today:

**1. System-Level Cognitive Injection**
AEGIS hooks into the agent's global rules via `AGENTS.md` and `SKILL.md`. It enforces a 4-tick pipeline on every task:
- Tick 1: OBSERVE
- Tick 4: PLAN
- Tick 8: EXECUTE
- Tick 9: REFLECT

**2. Event Loop Orchestration**
`kernel_runner.py` simulates the cognitive event loop, loads runtime images, and enforces the ISA.

**3. Triple-Output Synchronization**
When the core architecture is updated, AEGIS automatically: updates local files → syncs to the GitHub clone → packages into a distributable zip.

**4. Proprietary License Enforcement**
Injects the license header of Wahyu Nur Iman into all generated or modified source files.

---

## Installation

> [!WARNING]
> **Windows users:** If you see `Permission denied` during `git clone`, your terminal is probably opened in `C:\WINDOWS\System32`. Move to your user directory first (e.g., `cd $env:USERPROFILE\Documents`) before cloning.

### macOS / Linux

```bash
cd ~/Documents
git clone https://github.com/wahyunuriman999/AEGIS-Core.git
cd AEGIS-Core
pip install -r requirements.txt
python AEGIS-Runtime/kernel_runner.py --boot
```

### Windows (PowerShell)

```powershell
cd $env:USERPROFILE\Documents
git clone https://github.com/wahyunuriman999/AEGIS-Core.git
cd AEGIS-Core
pip install -r requirements.txt
python AEGIS-Runtime\kernel_runner.py --boot
```

---

## Usage

### Initialize a workspace

```bash
python AEGIS-Runtime/kernel_runner.py --init-workspace path/to/your/project
```

### Submit a task

```bash
python AEGIS-Runtime/kernel_runner.py --task "Refactor authentication module to use JWT and follow SOLID principles"
```

AEGIS runs the full pipeline (OBSERVE → PLAN → SIMULATE → EXECUTE) before touching any files.

### Compile new knowledge

```bash
python AEGIS-Compiler/build.py --ingest path/to/new/knowledge.md
```

### View execution graph

```bash
python AEGIS-Runtime/kernel_runner.py --show-graph
```

---

## Tests

AEGIS is verified through Python unit tests. Results from the latest run:

<div align="center">

[![Test Suite](https://img.shields.io/badge/Test_Suite-Passing-success?style=for-the-badge&logo=pytest)]()
[![Compiler Speed](https://img.shields.io/badge/Compiler_Speed-505.98_ms-blue?style=for-the-badge)]()
[![Pipeline Time](https://img.shields.io/badge/Cognitive_Pipeline-6.94_sec-blue?style=for-the-badge)]()

</div>

### Knowledge Compiler (`build.py`)

| Metric | Result | Status |
|--------|--------|--------|
| Output Artifacts | 3 Cognitive Graphs Generated | 🟢 PASSED |
| Integrity Check | Kernel Version Validated | 🟢 PASSED |
| Compilation Time | 505.98 ms | 🟢 PASSED |

### Cognitive Kernel (`kernel_runner.py`)

| Metric | Result | Status |
|--------|--------|--------|
| Memory Mounting | L0–L5 Memory Mounted | 🟢 PASSED |
| Provider Hand-off | GPT-4o & 9Router Linked | 🟢 PASSED |
| Pipeline Execution | 9 Ticks Completed | 🟢 PASSED |
| Total Time | 6.94 seconds | 🟢 PASSED |

<details>
<summary><b>View Raw Execution Logs</b></summary>

```
[TEST] Testing Knowledge Compiler (build.py)...
Initiating AEGIS Pipeline Compiler v12.0...
Compiling Memory Snapshots & Capability Registry...
Compilation Successful! 3 output graphs generated.
       -> SUCCESS: Compiled 3 Cognitive Graphs in 505.98 ms

[TEST] Testing Cognitive Kernel (kernel_runner.py)...
[BIOS: OK] Booting AEGIS Virtual Machine v12.0...
Kernel Version: v12.0.0-executable-kernel
Loaded 6 Providers via ABI.
Mounting L0-L5 Memory Hierarchy...

--- INCOMING EVENT: UNIT TEST DIAGNOSTIC TASK ---
[Tick 1: OBSERVE] Executing Opcode 0x01...
[Tick 4: PLAN] Executing Opcode 0x04...
   -> Provider: OpenAI (GPT-4o)
[Tick 7: EXECUTE] Executing Opcode 0x07...
   -> Provider: 9Router (Gateway)

[KERNEL] Event Loop Completed Successfully.
       -> SUCCESS: Kernel executed 9-Tick Pipeline in 6.94 seconds

Ran 2 tests in 7.468s
OK
```

</details>

---

## Core vs. Elite — Perbandingan Jujur

AEGIS-Core adalah fondasi. AEGIS-Elite adalah sistem operasi lengkap yang dibangun di atas fondasi ini. Tabel di bawah menunjukkan perbedaan secara jujur, tanpa melebih-lebihkan:

| Kemampuan | AEGIS-Core | AEGIS-Elite |
|---|:---:|:---:|
| **Cognitive Runtime (4-tick pipeline)** | ✅ | ✅ |
| **Knowledge Compiler** | ✅ | ✅ |
| **Memory Hierarchy (L1–L5)** | ✅ | ✅ |
| **Provider routing** (GPT, Claude, Gemini, dll.) | ✅ | ✅ |
| **Governance** | 1 lapisan (dasar) | **5 lapisan berlapis** |
| **Audit trail per-commit** | ❌ | ✅ |
| **Multi-agent consensus** | ❌ | ✅ 5 agen + veto power |
| **Risk analysis sebelum perubahan** | ❌ | ✅ Blast-radius scoring |
| **Cognitive Memory lintas sesi** | Basic (L4 Experience) | ✅ 4 subsystem (ADR ledger, topology diff, learning loop, trend analysis) |
| **Governance makin ketat dari kegagalan** | ❌ | ✅ LearningLoop auto-tightening |
| **Extension marketplace** | ❌ | ✅ 7 domain pack |
| **Verifiable benchmark suite** | ❌ | ✅ 6 metrik vs industry baseline |
| **Enterprise compliance** | ❌ | ✅ SOC2, GDPR, RBAC, audit trail |
| **Git pre-commit hook** | ❌ | ✅ |
| **Workflow multi-step dengan rollback** | ❌ | ✅ |
| **Learning curve** | ⭐⭐⭐⭐⭐ (mudah) | ⭐⭐⭐ (lebih curam) |
| **Cocok untuk** | Open source, integrasi, belajar | Tim besar, enterprise, regulasi ketat |

### Mengapa Core lebih unggul untuk beberapa kasus

Core sengaja lebih ringan dan itu adalah kekuatannya:

- **Lebih mudah dipelajari** — tidak ada konsep tambahan yang perlu dipahami dulu
- **Lebih mudah diintegrasikan** — bisa disisipkan ke Cursor, Copilot, Cline, Claude Code tanpa konfigurasi tambahan
- **Maintenance lebih ringan** — codebase kecil, mudah di-fork dan dikontribusi
- **Lebih cepat boot** — tanpa overhead governance dan consensus engine

Core adalah pilihan tepat jika Anda tidak membutuhkan semua lapisan enterprise yang ada di Elite.

---

## AEGIS Elite

Untuk tim yang membutuhkan lebih dari fondasi, ada tier premium bernama **AEGIS Elite**.

Elite bukan sekadar Core dengan fitur tambahan. Elite adalah platform engineering lengkap yang menggunakan Core sebagai kernelnya — sama seperti Ubuntu menggunakan kernel Linux sebagai fondasinya.

Yang Elite tambahkan secara nyata:
- Governance 5 lapisan yang memblokir commit bermasalah sebelum masuk ke codebase
- 5-agent AI council yang mendebat setiap perubahan, dengan hak veto untuk keamanan dan arsitektur
- Sistem memory kognitif yang belajar dari kegagalan dan makin ketat seiring waktu
- Risk assessment untuk menghitung dampak perubahan sebelum dieksekusi
- Extension packs untuk domain spesifik (React, Flutter, Laravel, Rust, Security, ML, Python)
- Enterprise compliance (SOC2, GDPR, RBAC, audit trail)

Tertarik atau ingin berdiskusi soal use case dan harga?
Hubungi: **wahyunuriman999@gmail.com**

GitHub Elite: [github.com/wahyunuriman999/AEGIS-ELITE](https://github.com/wahyunuriman999/AEGIS-ELITE)

---

## Memilih Core atau Elite

Ini bukan tentang mana yang "lebih baik" secara absolut. Ini tentang kebutuhan.

**Pilih Core jika:**
- Anda ingin memahami dan bereksperimen dengan AEGIS
- Tim Anda kecil (1–5 developer)
- Anda ingin mengintegrasikan AEGIS ke toolchain yang sudah ada
- Open source dan komunitas adalah prioritas

**Pilih Elite jika:**
- Tim Anda > 5 developer dengan standar kode yang perlu dijaga terpusat
- Anda butuh auditability dan governance untuk kepatuhan regulasi
- Perlu workflow otomatis dari requirement hingga deployment
- Setiap commit harus melewati validasi berlapis sebelum masuk ke production

---

## FAQ

**Mengapa tidak pakai GPT atau Claude langsung?**
Language models memprediksi token. AEGIS mengontrol *bagaimana* dan *kapan* mereka memprediksi token — menggunakan formal scheduler, reflection loop, dan simulation layer. LLM adalah compute, bukan otak.

**Mengapa tidak pakai LangChain atau CrewAI?**
Itu adalah workflow dan agent frameworks. AEGIS beroperasi di lapisan lebih bawah — mendefinisikan Instruction Set, Memory Hierarchy, dan Execution Graph yang framework-framework itu duduki di atasnya.

**Mengapa knowledge dikompilasi bukan di-prompt?**
Mengirim ribuan baris markdown ke prompt menghasilkan noise dan non-determinisme. Mengkompilasinya ke dalam graph memastikan runtime punya knowledge base yang terstruktur dan bisa di-query.

---

<div align="center">

**AEGIS** — *Engineering Intelligence Beyond the Language Model.*

Copyright © 2024–2026 Wahyu Nur Iman. All rights reserved. Proprietary and Confidential.

</div>
