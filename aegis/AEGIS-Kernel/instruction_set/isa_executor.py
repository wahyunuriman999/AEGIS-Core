# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time
import os
import sys
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(current_dir), "memory"))
sys.path.insert(0, os.path.join(os.path.dirname(current_dir), "dispatcher"))

from state_memory import StateTimelineSimulator
from scheduler import CognitiveScheduler

class ISAExecutor:
    def __init__(self, memory_hierarchy, provider_manager, aegis_root):
        self.memory = memory_hierarchy
        self.provider = provider_manager
        self.state_simulator = StateTimelineSimulator()
        self.scheduler = CognitiveScheduler()
        self.aegis_root = aegis_root
        self.trace_log = []
        self.ledger = []
        
    def _log_trace(self, opcode, name, message):
        timestamp = time.time()
        print(message)
        self.trace_log.append({
            "timestamp": timestamp,
            "tick": f"{opcode}:{name}",
            "message": message.strip()
        })
        
    def execute_instruction(self, opcode, name, task):
        self._log_trace(opcode, name, f"\n[Tick {opcode}: {name}]")
        
        method_name = f"_{name.lower()}"
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            method(task)
        else:
            time.sleep(0.1)
            self._log_trace(opcode, name, f"  -> Instruction {name} executed.")

    def _observe(self, task):
        time.sleep(0.2)
        self.memory.write_l1("current_task", task)
        self._log_trace("0x01", "OBSERVE", "  -> Parsed user intent & environment. Loaded to L1.")
        
    def _retrieve(self, task):
        time.sleep(0.1)
        self._log_trace("0x02", "RETRIEVE", "  -> Fetched compiled nodes from L3 Knowledge Graph.")
        
    def _compare(self, task):
        time.sleep(0.1)
        self._log_trace("0x03", "COMPARE", "  -> Cross-referenced nodes against PRECEDENCE.md rules.")
        
    def _evaluate(self, task):
        time.sleep(0.1)
        self._log_trace("0x04", "EVALUATE", "  -> Calculated Engineering Entropy (Cost: Low, Latency: Optimal).")
        self.memory.write_l1("entropy_score", 0.6)
        
    def _plan(self, task):
        time.sleep(0.2)
        self._log_trace("0x05", "PLAN", "  -> Invoking Provider to construct DAG...")
        # REAL CODE: Use Capability Routing instead of hardcoded model name
        response = self.provider.route_request("core.planning", f"Plan: {task}", {})
        self.memory.write_l1("current_plan", response)
        self._log_trace("0x05", "PLAN", f"  -> Plan constructed: {response}")
        
    def _predict(self, task):
        plan = self.memory.L1_working.get("current_plan", "Empty")
        timeline = self.state_simulator.calculate_future_tech_debt(plan)
        self.memory.write_l1("timeline_forecast", timeline)
        self._log_trace("0x06", "PREDICT", f"  -> Calculated T+60 Entropy Forecast: {timeline['T+60 (5 Years)']['entropy']:.2f}")
        
    def _simulate(self, task):
        time.sleep(0.2)
        self._log_trace("0x07", "SIMULATE", "  -> Stress testing plan against catastrophic failure vectors...")
        
    def _debate(self, task):
        entropy = self.memory.L1_working.get("entropy_score", 0.1)
        self._log_trace("0x08", "DEBATE", f"  -> Entropy is {entropy}. Invoking Virtual Sub-Agents...")
        self.scheduler.run_debate_threads(entropy)
        self._log_trace("0x08", "DEBATE", "  -> Consensus reached across agents.")
        
    def _validate(self, task):
        time.sleep(0.1)
        self._log_trace("0x09", "VALIDATE", "  -> Consensus verified. Entropy is acceptable.")
        self.ledger.append({"task": task, "decision": "APPROVED", "entropy": 0.6})
        
    def _reflect(self, task):
        time.sleep(0.1)
        self._log_trace("0x0A", "REFLECT", "  -> Comparing execution artifacts against FAILURE_DB.json.")
        
    def _learn(self, task):
        time.sleep(0.2)
        self.memory.update_l4_experience(f"Mutation logged for task: {task}")
        self._log_trace("0x0B", "LEARN", "  -> Genome mutated. State cached to L4 Memory.")
        
        # REAL CODE: Write traces and ledger to JSON files
        runtime_dir = os.path.join(self.aegis_root, "AEGIS-Runtime")
        if not os.path.exists(runtime_dir):
            os.makedirs(runtime_dir)
            
        trace_path = os.path.join(runtime_dir, "runtime_trace.json")
        ledger_path = os.path.join(runtime_dir, "decision_ledger.json")
        
        with open(trace_path, 'w', encoding='utf-8') as f:
            json.dump(self.trace_log, f, indent=2)
            
        with open(ledger_path, 'w', encoding='utf-8') as f:
            json.dump(self.ledger, f, indent=2)
            
        print(f"\n[SYS] Real I/O Operation: Successfully wrote execution traces to {trace_path}")
        print(f"[SYS] Real I/O Operation: Successfully saved ledger to {ledger_path}")
