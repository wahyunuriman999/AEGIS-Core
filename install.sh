#!/bin/bash
# Installation script for AEGIS v4.2 on macOS/Linux

TARGET_DIR="$HOME/.gemini/config/skills/aegis"

echo "Installing AEGIS v4.2 global skill..."
mkdir -p "$TARGET_DIR"

cp -r aegis/* "$TARGET_DIR/"

echo "Successfully installed AEGIS v4.2 to $TARGET_DIR"
echo "Restart your AI agent or IDE to reload the custom skills."
