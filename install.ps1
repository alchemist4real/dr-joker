# ==============================================================================
# dr.joker Universal Installer (Windows PowerShell)
# Installs dr.joker into Google Antigravity, Claude Code, OpenAI Codex, and Cursor
# ==============================================================================

$ErrorActionPreference = "Stop"
$RepoUrl = "https://github.com/antigravity-community/dr-joker.git"
$SkillName = "dr-joker"

Write-Host "🃏 Installing dr.joker Assessment Swarm..." -ForegroundColor Cyan

# 1. Google Antigravity
$AgyDir = Join-Path $HOME ".gemini\skills\$SkillName"
New-Item -ItemType Directory -Path (Join-Path $HOME ".gemini\skills") -Force | Out-Null

if (Test-Path $AgyDir) {
    Write-Host "  [UPDATE] Updating existing Antigravity skill..." -ForegroundColor Yellow
} else {
    Write-Host "  [INSTALL] Installing into Google Antigravity ($AgyDir)..." -ForegroundColor Green
    try {
        git clone --depth 1 $RepoUrl $AgyDir --quiet
    } catch {
        New-Item -ItemType Directory -Path $AgyDir -Force | Out-Null
        Copy-Item -Path "$PSScriptRoot\*" -Destination $AgyDir -Recurse -Force
    }
}

# 2. Claude Code
$ClaudeDir = Join-Path $HOME ".claude\skills\$SkillName"
New-Item -ItemType Directory -Path (Join-Path $HOME ".claude\skills") -Force | Out-Null
if (-not (Test-Path $ClaudeDir) -and (Test-Path $AgyDir)) {
    Write-Host "  [INSTALL] Linking to Claude Code ($ClaudeDir)..." -ForegroundColor Green
    Copy-Item -Path $AgyDir -Destination $ClaudeDir -Recurse -Force
}

# 3. OpenAI Codex
$CodexDir = Join-Path $HOME ".codex\skills\$SkillName"
New-Item -ItemType Directory -Path (Join-Path $HOME ".codex\skills") -Force | Out-Null
if (-not (Test-Path $CodexDir) -and (Test-Path $AgyDir)) {
    Write-Host "  [INSTALL] Linking to Codex ($CodexDir)..." -ForegroundColor Green
    Copy-Item -Path $AgyDir -Destination $CodexDir -Recurse -Force
}

Write-Host ""
Write-Host "✅ dr.joker installed successfully across all AI coding assistants!" -ForegroundColor Green
Write-Host "Usage in Antigravity / Claude / Codex:" -ForegroundColor Cyan
Write-Host "  Prompt: 'Gunakan dr.joker untuk menganalisis folder [awetan] dan [materi]'" -ForegroundColor White
