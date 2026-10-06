"""
dr.joker - Autonomous Swarm Orchestrator Engine
"""

import os
import sys
import glob
import math
import json
from typing import List, Dict, Any

class JokerOrchestrator:
    def __init__(self, exam_dir: str, module_dir: str, output_dir: str = "./output", max_concurrency: int = 8):
        self.exam_dir = os.path.abspath(exam_dir)
        self.module_dir = os.path.abspath(module_dir)
        self.output_dir = os.path.abspath(output_dir)
        self.max_concurrency = max_concurrency
        
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.exam_files = []
        self.module_files = []
        self.variables = {}
        
    def scan_topology(self) -> Dict[str, Any]:
        """Tier 1: Physical File Topology Discovery"""
        valid_exts = ("*.pdf", "*.pptx", "*.txt", "*.md", "*.png", "*.jpg", "*.docx")
        for ext in valid_exts:
            self.exam_files.extend(glob.glob(os.path.join(self.exam_dir, "**", ext), recursive=True))
            self.module_files.extend(glob.glob(os.path.join(self.module_dir, "**", ext), recursive=True))
            
        self.exam_files = sorted(list(set(self.exam_files)))
        self.module_files = sorted(list(set(self.module_files)))
        
        N_exam = len(self.exam_files)
        N_mod = len(self.module_files)
        S_workers = min(self.max_concurrency, N_mod) if N_mod > 0 else 1
        
        self.variables = {
            "N_exam": N_exam,
            "N_mod": N_mod,
            "S_workers": S_workers,
            "S_total_swarm": S_workers + 4,
            "T_station": 60,
            "Target_stations": 20
        }
        return self.variables

    def generate_subagent_manifest(self) -> List[Dict[str, Any]]:
        """Tier 2 & 3: Provision Subagent Swarm Roles"""
        if not self.variables:
            self.scan_topology()
            
        manifest = []
        # Historical Auditor
        manifest.append({
            "agent_id": "historical_auditor",
            "role": "Historical Ground-Truth Auditor Agent",
            "target_files": self.exam_files,
            "duty": "Dissect past exam papers into atomic sub-questions, extract Angka Mati and Zero-Dose blacklists."
        })
        
        # Parallel Module Workers
        chunk = math.ceil(len(self.module_files) / self.variables["S_workers"]) if self.variables["S_workers"] > 0 else 1
        for i in range(self.variables["S_workers"]):
            assigned = self.module_files[i * chunk : (i + 1) * chunk]
            manifest.append({
                "agent_id": f"module_extractor_{i+1}",
                "role": f"Module Extractor Worker #{i+1}",
                "target_files": assigned,
                "duty": "Extract molecular targets, congener peer trees, Latin prescription rules, and pathognomonic toxicities."
            })
            
        # Governance
        manifest.append({
            "agent_id": "adversarial_arbiter",
            "role": "Adversarial Debate Arbiter & Rubric Judge",
            "duty": "Enforce 50:50 cognitive polarity rule and veto ungrounded doses."
        })
        manifest.append({
            "agent_id": "predictive_modeler",
            "role": "Predictive Rotation Modeler",
            "duty": "Compute P_i rankings and synthesize 20 stations with Shift A, B, and C alters."
        })
        manifest.append({
            "agent_id": "speed_compiler",
            "role": "Speed-Master Output Compiler",
            "duty": "Render high-yield bulleted 60-second cram sheets and compile verified PDF."
        })
        return manifest

    def run_full_pipeline(self) -> Dict[str, Any]:
        """Executes the complete autonomous pipeline"""
        vars_res = self.scan_topology()
        swarm_res = self.generate_subagent_manifest()
        
        report = {
            "status": "success",
            "variables": vars_res,
            "swarm_size": len(swarm_res),
            "swarm_manifest": swarm_res,
            "output_directory": self.output_dir
        }
        
        report_path = os.path.join(self.output_dir, "dr_joker_pipeline_report.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
            
        return report
