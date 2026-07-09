import subprocess
import sys
import os

def run_boot():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    print("Initiating Foundation Boot Sequence...")
    
    # 1. Run Doctor
    print("\n>>> Phase 1: Diagnostics")
    doctor_script = os.path.join(repo_dir, "src", "orchestrator", "doctor.py")
    doctor_code = subprocess.call([sys.executable, doctor_script])
    if doctor_code != 0:
        print("BOOT FAILED: Diagnostics failed. Halting to preserve repository integrity.")
        sys.exit(1)
        
    # 2. Compile State
    print("\n>>> Phase 2: State Compilation")
    compiler_script = os.path.join(repo_dir, "src", "orchestrator", "state_compiler.py")
    subprocess.check_call([sys.executable, compiler_script])
    
    print("\nBOOT SUCCESS: System Ready.")

if __name__ == "__main__":
    run_boot()
