"""
dr.joker CLI - Command Line Interface for Autonomous Assessment Engine
"""

import os
import sys
import argparse
import json
from scripts.orchestrator import JokerOrchestrator

def main():
    parser = argparse.ArgumentParser(
        prog="dr-joker",
        description="dr.joker: Autonomous Zero-Touch Practical Exam Reverse-Engineering Swarm"
    )
    subparsers = parser.add_subparsers(dest="subcommand", help="Available subcommands")

    # 1. RUN (Default Full Pipeline)
    run_parser = subparsers.add_parser("run", help="Run full zero-touch assessment pipeline")
    run_parser.add_argument("--exam-dir", required=True, help="Directory containing past exam archives (awetan)")
    run_parser.add_argument("--module-dir", required=True, help="Directory containing curriculum modules (PPT/notes)")
    run_parser.add_argument("--output-dir", default="./output", help="Directory to save generated artifacts")
    run_parser.add_argument("--concurrency", type=int, default=8, help="Maximum worker subagent concurrency")

    # 2. SCAN
    scan_parser = subparsers.add_parser("scan", help="Scan files and discover physical variables")
    scan_parser.add_argument("--exam-dir", required=True, help="Directory containing past exam archives")
    scan_parser.add_argument("--module-dir", required=True, help="Directory containing curriculum modules")

    # 3. AUDIT
    audit_parser = subparsers.add_parser("audit", help="Audit past exam papers for Angka Mati")
    audit_parser.add_argument("--exam-dir", required=True, help="Directory containing past exam archives")
    audit_parser.add_argument("--output", default="./output/audit.json", help="Path to write audit JSON")

    args = parser.parse_args()

    if not args.subcommand or args.subcommand == "run":
        if not hasattr(args, "exam_dir") or not args.exam_dir:
            parser.print_help()
            sys.exit(1)
            
        print("\n🃏 [dr.joker] Launching Autonomous Assessment Engine...")
        orchestrator = JokerOrchestrator(
            exam_dir=args.exam_dir,
            module_dir=args.module_dir,
            output_dir=args.output_dir,
            max_concurrency=args.concurrency
        )
        report = orchestrator.run_full_pipeline()
        print(f"\n[dr.joker] Pipeline Completed Successfully!")
        print(f"  - Exam Files Detected   : {report['variables']['N_exam']}")
        print(f"  - Module Files Detected : {report['variables']['N_mod']}")
        print(f"  - Subagents Spawned     : {report['swarm_size']}")
        print(f"  - Report Artifact Saved : {os.path.join(args.output_dir, 'dr_joker_pipeline_report.json')}")

    elif args.subcommand == "scan":
        orchestrator = JokerOrchestrator(exam_dir=args.exam_dir, module_dir=args.module_dir)
        vars_res = orchestrator.scan_topology()
        print("\n🃏 [dr.joker] Physical Topology Discovered:")
        print(json.dumps(vars_res, indent=2))

    elif args.subcommand == "audit":
        orchestrator = JokerOrchestrator(exam_dir=args.exam_dir, module_dir=".")
        vars_res = orchestrator.scan_topology()
        print(f"\n🃏 [dr.joker] Audited {vars_res['N_exam']} exam files.")

if __name__ == "__main__":
    main()
