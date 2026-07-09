import os
import subprocess
import sys

def test_adr_enforcement():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # In CI, we check the diff against main. Locally, we might just pass.
    try:
        diff_output = subprocess.check_output(['git', 'diff', '--name-only', 'origin/main...HEAD'], cwd=repo_root).decode('utf-8')
        changed_files = diff_output.strip().split('\n')
    except Exception:
        # Not in a git repo with origin/main, skip test
        return

    structural_paths = ["constitution/", "schemas/", "src/", "specification/", "REPOSITORY_BIOS.json"]
    
    structural_changes = [f for f in changed_files if any(f.startswith(p) for p in structural_paths)]
    adr_changes = [f for f in changed_files if f.startswith("constitution/adr/")]
    
    if structural_changes and not adr_changes:
        print("FAIL: Structural changes detected without a corresponding ADR.")
        print("Structural files changed:", structural_changes)
        sys.exit(1)
        
    print("PASS: ADR enforcement check passed.")
