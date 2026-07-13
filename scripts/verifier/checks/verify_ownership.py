import os
import glob
from collections import defaultdict
from scripts.verifier.framework import AuditCheck, Finding, Severity

class VerifyOwnership(AuditCheck):
    name = "Verify Playbook Ownership and Detect Overlap"
    
    def run(self, repo_root: str) -> list[Finding]:
        findings = []
        playbook_pattern = os.path.join(repo_root, "docs", "playbooks", "*.md")
        playbooks = glob.glob(playbook_pattern)
        
        keyword_map = defaultdict(list)
        
        for p in playbooks:
            basename = os.path.basename(p).lower()
            # Extract basic keywords from filename
            words = basename.replace(".md", "").split("_")
            for w in words:
                if len(w) > 3 and w not in ["drill", "audit", "repository"]:
                    keyword_map[w].append(p)
                    
        for keyword, files in keyword_map.items():
            if len(files) > 1:
                findings.append(Finding(
                    severity=Severity.WARNING,
                    evidence=f"Keyword '{keyword}' claimed by: {', '.join([os.path.basename(f) for f in files])}",
                    location="docs/playbooks/",
                    reason="Possible Keyword Ownership Conflict detected between playbooks.",
                    suggested_fix="Human review: Merge workflows or clarify ownership boundaries.",
                    confidence="Low (Heuristic)"
                ))
                
        return findings
