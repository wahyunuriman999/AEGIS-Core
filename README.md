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
[![License](https://img.shields.io/badge/License-Copyrighted-red?style=for-the-badge)]()

# AEGIS

### The Cognitive Runtime Platform for AI Engineering

*Engineering Intelligence Beyond the Language Model.*

[ [Architecture](#architecture) ] • [ [Installation](#installation) ] • [ [Usage](#usage) ] • [ [Tests](#tests) ] • [ [FAQ](#faq) ]

</div>

---

## What is AEGIS?

AEGIS is a cognitive runtime layer that sits between the user and a language model. Instead of sending raw prompts, AEGIS structures reasoning into a formal pipeline — with planning, simulation, validation, and reflection — before any output is produced.

The idea is simple: language models are powerful, but they have no native scheduler, no memory hierarchy, and no way to enforce deterministic behavior. AEGIS adds that infrastructure.

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

## AEGIS Elite

AEGIS Core is open and free to use. For teams that need more, there is a premium tier called **AEGIS Elite**.

Elite extends the Core runtime with features built for production use — multi-agent coordination, enterprise governance, and active evolution of the system's own behavior based on real outcomes.

### What Elite adds over Core

| Feature | Core | Elite |
|---------|------|-------|
| Cognitive Runtime (4-tick pipeline) | ✅ | ✅ |
| Knowledge Compiler | ✅ | ✅ |
| Memory Hierarchy (L1–L5) | ✅ | ✅ |
| Provider routing (GPT, Claude, Gemini, etc.) | ✅ | ✅ |
| Multi-agent consensus voting | ❌ | ✅ |
| Active Capability Graph (runtime self-mapping) | ❌ | ✅ |
| Engineering Genome evolution (auto-mutation based on outcomes) | ❌ | ✅ |
| Governance engine with audit trail | ❌ | ✅ |
| Domain extension packs (security, data, infra, etc.) | ❌ | ✅ |
| Enterprise deployment support | ❌ | ✅ |

### Interested?

Send an email to **wahyunuriman999@gmail.com** to discuss use case and pricing.

---

## FAQ

**Why not just use GPT or Claude directly?**
Language models predict tokens. AEGIS controls *how* and *when* they predict tokens — using a formal scheduler, reflection loop, and simulation layer. The LLM is the compute, not the brain.

**Why not use LangChain or CrewAI?**
Those are workflow and agent frameworks. AEGIS operates at a lower layer — it defines the Instruction Set, Memory Hierarchy, and Execution Graph that those frameworks would sit on top of.

**Why compile knowledge instead of including it in prompts?**
Sending thousands of lines of markdown into a prompt introduces noise and non-determinism. Compiling it into a graph ensures the runtime has a structured, queryable knowledge base.

---

<div align="center">

**AEGIS** — *Engineering Intelligence Beyond the Language Model.*

Copyright © 2024–2026 Wahyu Nur Iman. All rights reserved. Proprietary and Confidential.

</div>
