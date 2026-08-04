# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

"""
AEGIS Provider Manager — Real LLM Routing Layer

Detects available providers from environment variables and routes
capability requests to the best available model. Falls back to
simulation mode if no API keys are configured.

Priority order:
  1. OpenAI     (OPENAI_API_KEY)
  2. Anthropic  (ANTHROPIC_API_KEY)
  3. Gemini     (GOOGLE_API_KEY)
  4. Ollama     (OLLAMA_HOST — default http://localhost:11434)
  5. Simulation (no keys set — non-blocking fallback)
"""

import os
import re
import time


# ---------------------------------------------------------------------------
# Base Interface
# ---------------------------------------------------------------------------

class BaseProvider:
    """Abstract base for all LLM providers."""
    def execute(self, capability: str, prompt: str, context: dict) -> str:
        raise NotImplementedError("Providers must implement execute()")


# ---------------------------------------------------------------------------
# Real Provider Adapters
# ---------------------------------------------------------------------------

class OpenAIProvider(BaseProvider):
    def __init__(self, model: str = "gpt-4o"):
        self.model = model
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
            self._available = True
        except Exception:
            self._available = False

    def execute(self, capability: str, prompt: str, context: dict) -> str:
        if not self._available:
            return SimulationProvider("OpenAI[unavailable]").execute(capability, prompt, context)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
        )
        return response.choices[0].message.content


class AnthropicProvider(BaseProvider):
    def __init__(self, model: str = "claude-sonnet-4-5"):
        self.model = model
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
            self._available = True
        except Exception:
            self._available = False

    def execute(self, capability: str, prompt: str, context: dict) -> str:
        if not self._available:
            return SimulationProvider("Anthropic[unavailable]").execute(capability, prompt, context)
        message = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text


class GeminiProvider(BaseProvider):
    def __init__(self, model: str = "gemini-2.0-flash"):
        self.model = model
        try:
            import google.generativeai as genai
            genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
            self.client = genai.GenerativeModel(model)
            self._available = True
        except Exception:
            self._available = False

    def execute(self, capability: str, prompt: str, context: dict) -> str:
        if not self._available:
            return SimulationProvider("Gemini[unavailable]").execute(capability, prompt, context)
        response = self.client.generate_content(prompt)
        return response.text


class OllamaProvider(BaseProvider):
    def __init__(self, model: str = "llama3"):
        self.model = model
        self.host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        try:
            import ollama
            self.client = ollama
            self._available = True
        except Exception:
            self._available = False

    def execute(self, capability: str, prompt: str, context: dict) -> str:
        if not self._available:
            return SimulationProvider("Ollama[unavailable]").execute(capability, prompt, context)
        response = self.client.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]


class SimulationProvider(BaseProvider):
    """
    Non-blocking simulation — used when no API keys are set.
    Allows AEGIS to run its full 11-tick pipeline without requiring
    external LLM connectivity. Outputs are tagged [SIM] for transparency.
    """
    def __init__(self, name: str = "Simulation"):
        self.name = name

    def execute(self, capability: str, prompt: str, context: dict) -> str:
        time.sleep(0.3)
        return f"[SIM:{self.name}] Synthesized capability '{capability}' for: '{prompt}'"


# ---------------------------------------------------------------------------
# Provider Manager
# ---------------------------------------------------------------------------

class ProviderManager:
    """
    Loads capability registry from AEGIS-Specification/capability_registry.md,
    detects available real providers via environment variables, and routes
    each capability to the best available provider.
    """

    PROVIDER_ENV_MAP = {
        "OPENAI_API_KEY":    lambda: OpenAIProvider(),
        "ANTHROPIC_API_KEY": lambda: AnthropicProvider(),
        "GOOGLE_API_KEY":    lambda: GeminiProvider(),
    }

    def __init__(self, aegis_root: str):
        self.providers: dict[str, BaseProvider] = {}
        self.capability_map: dict[str, str] = {}
        self.aegis_root = aegis_root
        self._detect_providers()
        self._load_capability_registry()

    def _detect_providers(self):
        """Auto-detect available providers from environment variables."""
        detected = []
        for env_var, factory in self.PROVIDER_ENV_MAP.items():
            if os.environ.get(env_var):
                try:
                    provider = factory()
                    name = type(provider).__name__.replace("Provider", "")
                    self.providers[name] = provider
                    detected.append(name)
                except Exception as e:
                    print(f"[WARN] Failed to init provider for {env_var}: {e}")

        # Ollama — uses host, not API key
        if os.environ.get("OLLAMA_HOST") or self._ollama_running():
            try:
                self.providers["Ollama"] = OllamaProvider()
                detected.append("Ollama")
            except Exception:
                pass

        if detected:
            print(f"[SYS] Real providers detected: {', '.join(detected)}")
        else:
            print("[SYS] No API keys found — running in Simulation mode.")
            self.providers["Simulation"] = SimulationProvider()

    def _ollama_running(self) -> bool:
        """Check if Ollama is running locally."""
        try:
            import urllib.request
            urllib.request.urlopen("http://localhost:11434", timeout=1)
            return True
        except Exception:
            return False

    def _load_capability_registry(self):
        """Parse capability_registry.md to map capabilities → preferred providers."""
        registry_path = os.path.join(
            self.aegis_root, "AEGIS-Specification", "capability_registry.md"
        )
        if not os.path.exists(registry_path):
            print(f"[WARN] Capability Registry not found at {registry_path}")
            return

        with open(registry_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Format: - `capability.name`: Description. (Default: ModelName)
        matches = re.findall(r"-\s+`(.*?)`.*\(Default:\s+(.*?)\)", content)
        for capability, preferred_model in matches:
            self.capability_map[capability.strip()] = preferred_model.strip()

        print(f"[SYS] Loaded {len(self.capability_map)} capabilities from Registry.")

    def route_request(self, capability: str, prompt: str, context: dict) -> str:
        """
        Route a capability request to the best available provider.
        Falls back gracefully if the preferred provider is unavailable.
        """
        preferred = self.capability_map.get(capability)

        # Try preferred provider first
        if preferred and preferred in self.providers:
            return self.providers[preferred].execute(capability, prompt, context)

        # Try any available real provider
        for name, provider in self.providers.items():
            if not isinstance(provider, SimulationProvider):
                return provider.execute(capability, prompt, context)

        # Final fallback: simulation
        fallback = self.providers.get("Simulation", SimulationProvider())
        return fallback.execute(capability, prompt, context)
