# 🃏 dr.joker: Autonomous Practical Exam Reverse-Engineering & Station Prediction Swarm

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Supported Platforms](https://img.shields.io/badge/Platform-Antigravity%20%7C%20Claude%20%7C%20Codex%20%7C%20Cursor-blueviolet.svg)](#one-line-installers)
[![Autonomous Swarm](https://img.shields.io/badge/Architecture-Hierarchical%20Multi--Subagent-success.svg)](#swarm-architecture)

> **Zero-Touch Exam Intelligence.** You only provide two folders: your historical past exam files (*awetan*) and your curriculum modules (*PPT / notes / lab guides*). `dr.joker` calculates file topology, spawns an adversarial subagent swarm, resolves rubrics via 3-round debates, and generates 20 high-yield stations with fully reasoned Shift A, B, and C Alters.

---

## ⚡ One-Line Installers

Install `dr.joker` with a single command on your platform:

### 🪟 Windows (PowerShell) — Antigravity / Claude / Codex
```powershell
irm https://raw.githubusercontent.com/antigravity-community/dr-joker/main/install.ps1 | iex
```

### 🐧 Linux / macOS / WSL (Bash) — Antigravity / Claude / Codex
```bash
curl -fsSL https://raw.githubusercontent.com/antigravity-community/dr-joker/main/install.sh | bash
```

### 🤖 Claude Code Native
```bash
npx @anthropic-ai/claude-code skill add https://github.com/antigravity-community/dr-joker
```

### 📦 Manual Git Clone (Universal)
```bash
# For Google Antigravity
git clone https://github.com/antigravity-community/dr-joker.git ~/.gemini/skills/dr-joker

# For Claude Code
git clone https://github.com/antigravity-community/dr-joker.git ~/.claude/skills/dr-joker

# For OpenAI Codex
git clone https://github.com/antigravity-community/dr-joker.git ~/.codex/skills/dr-joker
```

---

## 🚀 How to Use

Once installed, simply invoke `dr.joker` in any conversation:

> *"Gunakan dr.joker untuk memprediksi ujian dari folder `./arsip_ujian` dan `./ppt_materi`"*

Or run the CLI directly from your terminal:

```bash
# Full automated zero-touch run
python scripts/cli.py run --exam-dir "./arsip_ujian" --module-dir "./ppt_materi" --output-dir "./hasil_prediksi"

# Scan variables and discover physical topology only
python scripts/cli.py scan --exam-dir "./arsip_ujian" --module-dir "./ppt_materi"
```

---

## 🧠 Core Architecture & Methodology

### 1. The Zero-Touch Principle
No manual tagging, no data conversion. The orchestrator automatically extracts text layers, identifies file formats, clusters topic graphs, and provisions the optimal number of parallel agents.

### 2. The 4 Variable Tiers
`dr.joker` discovers 4 real computable mathematical variable tiers:
* **Tier 1 (File Topology):** File counts ($N_{\text{mod}}$, $N_{\text{exam}}$), page volumes, token densities, and parallel worker pool size ($S_{\text{workers}} = \min(8, N_{\text{mod}})$).
* **Tier 2 (Assessment Dynamics):** Station time limit ($T_{\text{station}} = 60\text{s}$) enforcing strict word-budget filters.
* **Tier 3 (Curriculum Overlap):** Cross-module thematic density ($\rho_{\text{overlap}}$) and peer congener tree depth ($C_{\text{congener}}$).
* **Tier 4 (Station Scoring Formula):**
  $$P_i = 0.35 \cdot F_{\text{hist}}(i) + 0.25 \cdot R_{\text{due}}(i) + 0.25 \cdot I_{\text{curric}}(i) + 0.15 \cdot E_{\text{patho}}(i)$$

### 3. The 3-Round Adversarial Debate
* **Round 1 (Proposal):** Extractor Workers propose high-frequency curriculum concepts.
* **Round 2 (Antithesis):** Historical Auditor challenges unverified doses and checks past repetition.
* **Round 3 (Arbiter Ratification):** Enforces the **50:50 Cognitive Polarity Rule**:
  $$\text{Domain}(Sub\_a) \neq \text{Domain}(Sub\_b)$$
  Sub-a and Sub-b must never share the same cognitive domain (e.g., theory is paired with practical dose/prescription/red flag, never two memory recall questions).

### 4. The 3 Shift Alter Invariants
Examiners create alternative question cards (Alters) using strict operational constraints:
* **Shift A (Primary):** Landmark concept (Mechanism + Key Clinical Red Flag or Prescription).
* **Shift B (Posology Blindspot):** Same physical specimen on the table, question flipped to test dosage forms, ceiling doses, or interval latin syntax.
* **Shift C (Congener Swap):** Specimen swapped with a peer congener from the same lab tray; questions test contraindications in vulnerable populations.

---

## 📂 Repository Structure

```
dr-joker/
├── SKILL.md                          # Main Agent Skill Specification
├── README.md                         # Documentation & Installation Guide
├── install.sh                        # Bash One-Line Installer
├── install.ps1                       # PowerShell One-Line Installer
├── pyproject.toml                    # Python Package Configuration
├── scripts/
│   ├── __init__.py
│   ├── cli.py                        # Multi-command CLI tool
│   └── orchestrator.py               # Core swarm orchestrator engine
└── references/
    └── framework_specification.md    # Complete mathematical & algorithmic reference
```

---

## 📄 License
MIT License. Open for educational and medical student community use.
