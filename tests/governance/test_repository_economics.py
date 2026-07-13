import os
import glob
import re

def test_repository_economics_metadata():
    """
    Governance as Code: Justify Existence (Doctrine 14)
    Verifies that all permanent files contain the required meta-governance header.
    """
    required_keys = [
        "Authority:",
        "Lifecycle State:",
        "Owner:"
    ]
    
    # We enforce this on playbooks and governance docs
    target_patterns = [
        "docs/governance/*.md",
        "docs/playbooks/*.md",
        ".agents/skills/**/*.md"
    ]
    
    for pattern in target_patterns:
        for filepath in glob.glob(pattern, recursive=True):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            for key in required_keys:
                assert key in content, f"File {filepath} is missing required economic metadata '{key}'"
                
            has_exit = "Exit Condition:" in content
            has_perm = "Permanence Justification:" in content
            assert has_exit or has_perm, f"File {filepath} is missing required Exit Condition or Permanence Justification"

if __name__ == "__main__":
    test_repository_economics_metadata()
    print("Governance Test Passed: Repository Economics Metadata is enforced.")
