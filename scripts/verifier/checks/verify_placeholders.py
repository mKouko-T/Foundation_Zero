import os
import glob
import re
from scripts.verifier.framework import AuditCheck, Finding, Severity

class VerifyPlaceholders(AuditCheck):
    name = "Verify Placeholders (TODO/FIXME)"
    
    def run(self, repo_root: str) -> list[Finding]:
        findings = []
        
        # Banned paths (ERROR)
        permanent_paths = ["constitution", "governance", "playbooks", "kernel", "specification"]
        
        # Allowed paths (INFO)
        experimental_paths = ["experimental", "drafts", "prototypes", "scratch"]
        
        for filepath in glob.glob(os.path.join(repo_root, "**/*.*"), recursive=True):
            if ".git" in filepath or "node_modules" in filepath or "__pycache__" in filepath:
                continue
            if not filepath.endswith(('.md', '.py', '.json', '.txt')):
                continue
                
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                continue
                
            if "TODO" in content or "FIXME" in content or "[Insert here]" in content:
                # Determine severity based on path
                is_permanent = any(f"\\{p}\\" in filepath or f"/{p}/" in filepath for p in permanent_paths)
                is_experimental = any(f"\\{p}\\" in filepath or f"/{p}/" in filepath for p in experimental_paths)
                
                severity = Severity.ERROR if is_permanent else (Severity.INFO if is_experimental else Severity.WARNING)
                reason = "Placeholders found in permanent architecture." if severity == Severity.ERROR else "Placeholders tracked."
                
                findings.append(Finding(
                    severity=severity,
                    evidence="TODO/FIXME/[Insert here] pattern matched",
                    location=filepath,
                    reason=reason,
                    suggested_fix="Resolve the placeholder or move to experimental.",
                    confidence="High"
                ))
        return findings
