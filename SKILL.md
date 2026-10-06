---
name: dr-joker
description: >
  Autonomous Zero-Touch Practical Exam Reverse-Engineering & Station Prediction Swarm.
  Given raw folders of past exam specimens (awetan) and curriculum modules (PPT/notes),
  it dynamically discovers file topology variables, spawns specialized parallel subagents,
  conducts a 3-round adversarial debate to enforce 50:50 cognitive polarity, and synthesizes
  20 high-yield exam stations with fully reasoned Shift A, B, and C Alters.
---

# 🃏 dr.joker: Autonomous Practical Assessment & Station Prediction Engine

`dr.joker` is a high-precision multi-agent skill designed to reverse-engineer, audit, and predict high-stakes practical exams (OSPE, OSCE, laboratory bell-ringers, steeplechase, and viva stations).

It operates on a strict **Zero-Touch Principle**: the student only supplies two directory paths (past exam archives and curriculum modules). The swarm handles ingestion, variable discovery, subagent spawning, adversarial rubric adjudication, and final output compilation.

---

## 🎯 When to Activate This Skill
Trigger this skill whenever the user:
- Mentions *"ujian meja"*, *"OSPE"*, *"OSCE stasi"*, *"ujian identifikasi praktikum"*, or *"bell-ringer exam"*.
- Provides a folder/file of past exam questions (*"awetan / soal tahun lalu"*) and module slides (*"materi / PPT asdos / diktat"*).
- Asks to predict exam questions, find high-yield topics, or generate realistic multi-shift exam variations (Shift A, B, C Alters).
- Asks for a 60-second table answer sheet, Latin prescription drills, or "Dosis Angka Mati".

---

## 🏗️ Swarm Topology & Subagent Roles

When invoked, `dr.joker` calculates file topology and spawns up to 5 specialized subagent roles:

```
                    ┌────────────────────────────────────────────────────────┐
                    │               0. DR.JOKER ORCHESTRATOR                 │
                    │  • Scans directories, discovers variables, provisions   │
                    └───────────────────┬────────────────────────────────────┘
                                        │
           ┌────────────────────────────┴────────────────────────────┐
           ▼                                                         ▼
┌───────────────────────────────┐                         ┌───────────────────────────────┐
│  1. HISTORICAL AUDITOR AGENT  │                         │  2. MODULE EXTRACTOR SWARM    │
│  • Parses past exam archives  │                         │     (1:1 per module file)     │
│  • Builds 'Angka Mati' pool   │                         │  • Extracts molecular targets │
│  • Flags 'Zero-Dose' entities │                         │  • Maps congener peer trees   │
└──────────────┬────────────────┘                         └──────────────┬────────────────┘
               │                                                         │
               └────────────────────────┬────────────────────────────────┘
                                        ▼
                         ┌───────────────────────────────┐
                         │ 3. ADVERSARIAL ARBITER JUDGE  │
                         │  • Conducts 3-round debate    │
                         │  • Enforces 50:50 rubric rule │
                         │  • Vetoes hallucinated doses  │
                         └──────────────┬────────────────┘
                                        ▼
                         ┌───────────────────────────────┐
                         │ 4. PREDICTIVE ROTATION AGENT  │
                         │  • Ranks candidates via P_i   │
                         │  • Balances 20 exam stations  │
                         │  • Designs Shift A, B, C      │
                         └──────────────┬────────────────┘
                                        ▼
                         ┌───────────────────────────────┐
                         │ 5. SPEED COMPILER AGENT       │
                         │  • Generates 60s Cheat Sheet  │
                         │  • Compiles verified PDF      │
                         └───────────────────────────────┘
```

---

## 📋 The 4 Mathematical Variable Tiers
`dr.joker` eliminates guesswork by computing 4 real variable tiers:

1. **Tier 1 (File Topology):**
   - $N_{\text{mod}}$: Total curriculum module files found.
   - $N_{\text{exam}}$: Total historical exam archives found.
   - $S_{\text{workers}} = \min(8, N_{\text{mod}})$: Parallel worker agents dispatched.
2. **Tier 2 (Assessment Dynamics):**
   - $T_{\text{station}}$: Station duration (default: 60s). Dictates maximum word budget (2–3 bullet points per sub-question).
   - $W_{\text{target}}$: Target predicted stations (default: 20 stations).
3. **Tier 3 (Cross-Module Density):**
   - $\rho_{\text{overlap}}$: Measures thematic overlap between modules (e.g. Diuretics and RAAS both treating hypertension).
   - $C_{\text{congener}}$: Depth of generic peer alternatives in the curriculum.
4. **Tier 4 (Station Probability Formula):**
   $$P_i = 0.35 \cdot F_{\text{hist}}(i) + 0.25 \cdot R_{\text{due}}(i) + 0.25 \cdot I_{\text{curric}}(i) + 0.15 \cdot E_{\text{patho}}(i)$$
   - $F_{\text{hist}}$: Historical repetition ratio in past exams.
   - $R_{\text{due}}$: Cyclical return weight (topics missing in the immediate past year).
   - $I_{\text{curric}}$: Slide count and dedicated emphasis in curriculum modules.
   - $E_{\text{patho}}$: Uniqueness of organ toxicity, contraindications, or prescription rules.

---

## ⚔️ The 3-Round Adversarial Debate Protocol

To prevent hallucinated questions, every station must survive this inter-agent debate:

* **Round 1 (Proposal):** Extractor Workers submit station candidates derived from high-frequency slide concepts.
* **Round 2 (Cross-Examination):** Historical Auditor challenges the proposal:
  - *"Is this dose ever tested in real archives, or is it decorative textbook trivia?"* $\rightarrow$ If ungrounded, VETO dosage question.
  - *"Are Sub-a and Sub-b both testing simple recall?"* $\rightarrow$ If so, VETO for rubric violation.
* **Round 3 (Arbiter Ratification):** The Arbiter enforces the **50:50 Cognitive Polarity Rule**:
  $$\text{Domain}(Sub\_a) \neq \text{Domain}(Sub\_b)$$
  One sub-question must test theoretical causality; the second sub-question must test a practical clinical discriminator (dose ceiling, Latin prescription, or pathognomonic danger sign).

---

## 🔄 The 3 Shift Alter Invariants
Examiners create alternative question cards (Alters) using strict operational constraints:
* **Shift A (Primary):** Landmark concept (Mechanism + Key Clinical Red Flag or Prescription).
* **Shift B (Posology Blindspot):** Same physical specimen on the table, but the question card is flipped to test dosage forms, ceiling doses, or interval latin syntax.
* **Shift C (Congener Swap / Special Population):** Specimen swapped with a peer congener from the same lab tray; questions test contraindications in vulnerable populations (pregnancy, renal failure, asthma).

---

## 🛠️ CLI Tool Usage & Subcommands

Run `dr.joker` via its Python CLI:

```bash
# Full Zero-Touch Pipeline
python scripts/cli.py run --exam-dir "<PATH_TO_EXAMS>" --module-dir "<PATH_TO_MODULES>" --output-dir "./output"

# Step 1: Scan and discover variables only
python scripts/cli.py scan --exam-dir "<PATH>" --module-dir "<PATH>"

# Step 2: Audit historical exams for 'Angka Mati'
python scripts/cli.py audit --exam-dir "<PATH>" --output "./output/audit_report.json"

# Step 3: Run adversarial debate and generate 20 stations
python scripts/cli.py debate --audit-file "./output/audit_report.json" --output "./output/stations.json"

# Step 4: Compile 60s Markdown and PDF
python scripts/cli.py compile --stations-file "./output/stations.json" --pdf
```

---

## 📦 Output Artifacts Generated
1. `MASTER_PREDIKSI_20_STASI_DENGAN_ALTERNATIF.md`: The complete 20 stations with Shift A, B, and C breakdowns.
2. `MASTER_PREDIKSI_20_STASI.pdf`: Clean, printable, high-resolution PDF with table of contents bookmarks.
3. `RINGKASAN_HAFALAN_60_DETIK.md`: Bulleted, high-yield cram sheet stripped of all textbook filler.
