# Installation script for SCUW v4.2 on Windows

$targetDir = "$env:USERPROFILE\.gemini\config\skills\super-claude-unified-workspace"

Write-Host "Installing SCUW v4.2 global skill on Windows..."
if (!(Test-Path $targetDir)) {
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
}

Copy-Item -Recurse -Force -Path "super-claude-unified-workspace\*" -Destination $targetDir

Write-Host "Successfully installed SCUW v4.2 to $targetDir" -ForegroundColor Green
Write-Host "Restart your AI agent or IDE to reload the custom skills."
