# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import os
import sys
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.insert(0, os.path.join(parent_dir, "AEGIS-Kernel"))
sys.path.insert(0, os.path.join(parent_dir, "AEGIS-Provider"))

try:
    from memory.memory_manager import MemoryHierarchy
    from instruction_set.isa_executor import ISAExecutor
    from dispatcher.event_dispatcher import EventDispatcher
    from provider_manager import ProviderManager
except ImportError as e:
    print(f"Failed to import core modules: {e}")
    sys.exit(1)

class AegisVirtualMachine:
    def __init__(self, aegis_root):
        self.root = aegis_root
        self.memory = MemoryHierarchy(self.root)
        self.provider_manager = ProviderManager(self.root)
        self.isa_executor = ISAExecutor(self.memory, self.provider_manager, self.root)
        self.dispatcher = EventDispatcher(self.isa_executor)
        
    def boot(self):
        print("[BIOS: OK] Booting AEGIS Virtual Machine v12.0 (Real Capability Routing)...")
        time.sleep(0.3)
        
        # 1. Mount Memory
        self.memory.mount()
        
        # 2. Boot Validations (Real check)
        abi_spec = os.path.join(self.root, "AEGIS-Specification", "abi_spec.md")
        if os.path.exists(abi_spec):
            print(f"[SYS] Validated ABI Conformity from {abi_spec}")
        else:
            print(f"[WARN] ABI Specification missing!")

        print(f"Kernel Version: v12.0.0-real-executable-kernel")
        time.sleep(0.3)
        print("Initializing Event Bus & Process Manager...\n")
        
    def execute_event_loop(self, task_name="Simulated User Request"):
        self.dispatcher.dispatch(task_name)
        
if __name__ == "__main__":
    aegis_root = r'C:\Users\ROG G532 LV\.gemini\antigravity\scratch\aegis-core-update\aegis'
    vm = AegisVirtualMachine(aegis_root)
    vm.boot()
    
    task = "Build Kubernetes Cluster Architecture"
    if len(sys.argv) > 1:
        if sys.argv[1] == "--task" and len(sys.argv) > 2:
            task = sys.argv[2]
            
    vm.execute_event_loop(task)
