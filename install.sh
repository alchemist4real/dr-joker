#!/usr/bin/env bash
# ==============================================================================
# dr.joker Universal Installer (Linux, macOS, WSL, Git Bash)
# Installs dr.joker into Google Antigravity, Claude Code, OpenAI Codex, and Cursor
# ==============================================================================
set -e

REPO_URL="https://github.com/alchemist4real/dr-joker.git"
SKILL_NAME="dr-joker"

echo "🃏 Installing dr.joker Assessment Swarm..."

# 1. Antigravity Skills Directory
AGY_SKILLS_DIR="$HOME/.gemini/skills/$SKILL_NAME"
mkdir -p "$HOME/.gemini/skills"
if [ -d "$AGY_SKILLS_DIR" ]; then
    echo "  [UPDATE] Updating existing Antigravity skill..."
    git -C "$AGY_SKILLS_DIR" pull --quiet || true
else
    echo "  [INSTALL] Installing into Antigravity ($AGY_SKILLS_DIR)..."
    git clone --depth 1 "$REPO_URL" "$AGY_SKILLS_DIR" --quiet || {
        mkdir -p "$AGY_SKILLS_DIR"
        cp -r . "$AGY_SKILLS_DIR" 2>/dev/null || true
    }
fi

# 2. Claude Code Skills Directory
CLAUDE_SKILLS_DIR="$HOME/.claude/skills/$SKILL_NAME"
mkdir -p "$HOME/.claude/skills"
if [ ! -d "$CLAUDE_SKILLS_DIR" ]; then
    echo "  [INSTALL] Linking to Claude Code ($CLAUDE_SKILLS_DIR)..."
    cp -r "$AGY_SKILLS_DIR" "$CLAUDE_SKILLS_DIR" 2>/dev/null || true
fi

# 3. OpenAI Codex Skills Directory
CODEX_SKILLS_DIR="$HOME/.codex/skills/$SKILL_NAME"
mkdir -p "$HOME/.codex/skills"
if [ ! -d "$CODEX_SKILLS_DIR" ]; then
    echo "  [INSTALL] Linking to Codex ($CODEX_SKILLS_DIR)..."
    cp -r "$AGY_SKILLS_DIR" "$CODEX_SKILLS_DIR" 2>/dev/null || true
fi

echo ""
echo "✅ dr.joker installed successfully across all AI coding environments!"
echo "Usage in Antigravity / Claude / Codex:"
echo "  Prompt: 'Gunakan dr.joker untuk memprediksi ujian dari folder [awetan] dan [materi]'"
