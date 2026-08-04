# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import json
import os
import time
from knowledge_compiler import KnowledgeCompiler

def build_cognitive_pipeline():
    print("Initiating AEGIS Pipeline Compiler v12.0 (Real Execution Mode)...")
    time.sleep(0.5)
    
    # Auto-detect aegis_root relative to this file's location
    aegis_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 1. RUN REAL KNOWLEDGE COMPILER (No Mock)
    compiler = KnowledgeCompiler(aegis_root)
    # Ingesting actual markdown files from docs/ and kernel/
    compiler.compile_directory('docs')
    compiler.compile_directory('kernel')
    graph_path = compiler.generate_graph()
    
    # 2. GENERATE RUNTIME IMAGE
    runtime_path = os.path.join(aegis_root, 'runtime_image.json')
    instruction_path = os.path.join(aegis_root, 'instruction_graph.json')
    
    with open(graph_path, 'r', encoding='utf-8') as f:
        graph_data = json.load(f)
        
    print("Compiling Real Memory Snapshots...")
    
    runtime_image = {
        "build_timestamp": time.time(),
        "kernel_version": "v12.0.0-real-engine",
        "memory_snapshot": {
            "L0_working": {},
            "L1_context": {},
            "L2_experience": {},
            "L3_decision": "pointer:AEGIS-Runtime/decision_ledger.json",
            "L4_failure": "pointer:AEGIS-Knowledge/FAILURE_DB.json",
            "L5_evolution": f"nodes:{len(graph_data.get('nodes', {}))}"
        },
        "knowledge_graph_ref": graph_path
    }
    
    # Real 11-step ISA defined from kernel/isa.md
    instruction_graph = {
        "isa_version": "2.0",
        "sequence": [
            {"opcode": "0x01", "name": "OBSERVE"},
            {"opcode": "0x02", "name": "RETRIEVE"},
            {"opcode": "0x03", "name": "COMPARE"},
            {"opcode": "0x04", "name": "EVALUATE"},
            {"opcode": "0x05", "name": "PLAN"},
            {"opcode": "0x06", "name": "PREDICT"},
            {"opcode": "0x07", "name": "SIMULATE"},
            {"opcode": "0x08", "name": "DEBATE"},
            {"opcode": "0x09", "name": "VALIDATE"},
            {"opcode": "0x0A", "name": "REFLECT"},
            {"opcode": "0x0B", "name": "LEARN"}
        ]
    }
    
    with open(runtime_path, 'w', encoding='utf-8') as f:
        json.dump(runtime_image, f, indent=2)
    with open(instruction_path, 'w', encoding='utf-8') as f:
        json.dump(instruction_graph, f, indent=2)
        
    print(f"Compilation Successful! Real graphs generated.")

if __name__ == "__main__":
    build_cognitive_pipeline()
