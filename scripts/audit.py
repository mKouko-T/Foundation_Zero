import os
import sys

# Ensure imports work from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.verifier.framework import Severity
from scripts.verifier.checks.verify_json import VerifyJson
from scripts.verifier.checks.verify_placeholders import VerifyPlaceholders
from scripts.verifier.checks.verify_metadata import VerifyMetadata
from scripts.verifier.checks.verify_references import VerifyReferences
from scripts.verifier.checks.verify_ownership import VerifyOwnership

def run_suite():
    import time
    start_time = time.time()
    
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    checks = [
        VerifyJson(),
        VerifyPlaceholders(),
        VerifyMetadata(),
        VerifyReferences(),
        VerifyOwnership()
    ]
    
    all_findings = []
    
    print("========================================")
    print(" Repository Verification Suite v1.1")
    print("========================================")
    print(f"Executing against: {repo_root}\n")
    
    for check in checks:
        print(f"Running: {check.name}... (Executed)")
        findings = check.run(repo_root)
        all_findings.extend(findings)
        
    print("\n========================================")
    print(" Repository Health Report")
    print("========================================")
    
    errors = [f for f in all_findings if f.severity == Severity.ERROR]
    warnings = [f for f in all_findings if f.severity == Severity.WARNING]
    infos = [f for f in all_findings if f.severity == Severity.INFO]
    
    print(f"Total Findings: {len(all_findings)}")
    print(f"  [ERROR]   {len(errors)}")
    print(f"  [WARNING] {len(warnings)}")
    print(f"  [INFO]    {len(infos)}")
    
    print("\n--- FINDINGS ---")
    for f in all_findings:
        print(f"\n[{f.severity.value}] {f.location}")
        print(f"  Reason: {f.reason}")
        print(f"  Evidence: {f.evidence}")
        print(f"  Fix: {f.suggested_fix}")
        
    duration = time.time() - start_time
    
    print("\n========================================")
    print(" VERIFIER SELF-METRICS")
    print("========================================")
    print(f"Checks Configured: {len(checks)}")
    print(f"Checks Executed: {len(checks)}")
    print(f"Checks Skipped/Disabled: 0")
    print(f"Total Findings Emitted: {len(all_findings)}")
    print(f"Average Runtime: {duration:.2f} seconds")
    
    print("\n========================================")
    print(" LIMITATIONS (Intellectual Honesty)")
    print("========================================")
    print("This suite verifies structural and mechanical facts only.")
    print("It explicitly DOES NOT verify:")
    print(" - Semantic correctness")
    print(" - Business correctness")
    print(" - Architectural quality")
    print(" - LLM reasoning")
    print(" - Human intent")
    print("========================================")

if __name__ == "__main__":
    run_suite()
