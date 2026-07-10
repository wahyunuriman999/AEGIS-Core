#!/bin/bash
# Installation script for SCUW v4.2 on macOS/Linux

TARGET_DIR="$HOME/.gemini/config/skills/super-claude-unified-workspace"

echo "Installing SCUW v4.2 global skill..."
mkdir -p "$TARGET_DIR"

cp -r super-claude-unified-workspace/* "$TARGET_DIR/"

echo "Successfully installed SCUW v4.2 to $TARGET_DIR"
echo "Restart your AI agent or IDE to reload the custom skills."
