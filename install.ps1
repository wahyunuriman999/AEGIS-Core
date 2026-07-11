# Installation script for AEGIS v4.2 on Windows

$targetDir = "$env:USERPROFILE\.gemini\config\skills\aegis"

Write-Host "Installing AEGIS v4.2 global skill on Windows..."
if (!(Test-Path $targetDir)) {
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
}

Copy-Item -Recurse -Force -Path "aegis\*" -Destination $targetDir

Write-Host "Successfully installed AEGIS v4.2 to $targetDir" -ForegroundColor Green
Write-Host "Restart your AI agent or IDE to reload the custom skills."
