import os
import json
import glob
from scripts.verifier.framework import AuditCheck, Finding, Severity

class VerifyJson(AuditCheck):
    name = "Verify JSON Syntax"
    
    def run(self, repo_root: str) -> list[Finding]:
        findings = []
        for filepath in glob.glob(os.path.join(repo_root, "**/*.json"), recursive=True):
            if ".git" in filepath or "node_modules" in filepath:
                continue
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                findings.append(Finding(
                    severity=Severity.ERROR,
                    evidence=str(e),
                    location=filepath,
                    reason="Invalid JSON syntax prevents parsing.",
                    suggested_fix="Correct the JSON syntax errors.",
                    confidence="High"
                ))
        return findings
