# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time
import os
import re

class BaseProvider:
    def execute(self, capability, prompt, context):
        raise NotImplementedError("Providers must implement execute()")

class MockProvider(BaseProvider):
    def __init__(self, name):
        self.name = name
        
    def execute(self, capability, prompt, context):
        time.sleep(0.3)
        return f"[{self.name}] Synthesized capability '{capability}' for prompt: '{prompt}'"

class ProviderManager:
    def __init__(self, aegis_root):
        self.providers = {}
        self.capability_map = {}
        self.aegis_root = aegis_root
        self._load_capability_registry()
        
    def _load_capability_registry(self):
        """REAL CODE: Parses capability_registry.md to map capabilities to providers."""
        registry_path = os.path.join(self.aegis_root, "AEGIS-Specification", "capability_registry.md")
        if not os.path.exists(registry_path):
            print(f"[ERROR] Capability Registry not found at {registry_path}")
            return
            
        with open(registry_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find "- `capability`: Description. (Default: ModelName)"
        matches = re.findall(r'-\s+`(.*?)`.*\(Default:\s+(.*?)\)', content)
        for capability, model in matches:
            self.capability_map[capability] = model.strip()
            # Register mock for the extracted model if not exists
            if model not in self.providers:
                self.providers[model] = MockProvider(model)
                
        print(f"[SYS] Loaded {len(self.capability_map)} capabilities from Registry.")
        
    def route_request(self, capability, prompt, context):
        """Routes request dynamically based on parsed markdown capability registry."""
        provider_name = self.capability_map.get(capability)
        
        if not provider_name or provider_name not in self.providers:
            print(f"Warning: Capability '{capability}' not mapped. Using fallback.")
            provider_name = list(self.providers.keys())[0] if self.providers else None
            
        if provider_name:
            provider = self.providers[provider_name]
            return provider.execute(capability, prompt, context)
        return "ERROR: No providers registered."
