import subprocess
import sys
import os

def run_orchestration():
    print("Chief of Staff orchestrating operations...")
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    compiler = os.path.join(repo_dir, "src", "orchestrator", "state_compiler.py")
    subprocess.check_call([sys.executable, compiler])
    print("Orchestration complete.")

if __name__ == "__main__":
    run_orchestration()
