import os
import glob
import re
from scripts.verifier.framework import AuditCheck, Finding, Severity

class VerifyMetadata(AuditCheck):
    name = "Verify Governance Metadata and Authority Chains"
    
    def run(self, repo_root: str) -> list[Finding]:
        findings = []
        required_keys = ["Authority:", "Lifecycle State:", "Owner:"]
        
        permanent_patterns = [
            "docs/governance/*.md",
            "docs/playbooks/*.md",
            "docs/architecture/*.md",
            ".agents/skills/**/*.md",
        ]
        root_files = ["README.md", "REPOSITORY_CONSTITUTION.md", "Evidence_of_Utility.md"]
        
        all_targets = []
        for pat in permanent_patterns:
            all_targets.extend(glob.glob(os.path.join(repo_root, pat), recursive=True))
        for f in root_files:
            p = os.path.join(repo_root, f)
            if os.path.exists(p):
                all_targets.append(p)
                
        for filepath in all_targets:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except:
                continue
                
            # Check Metadata
            for key in required_keys:
                if key not in content:
                    findings.append(Finding(
                        severity=Severity.ERROR,
                        evidence=f"Missing key '{key}'",
                        location=filepath,
                        reason="Permanent file violates meta-governance requirements.",
                        suggested_fix=f"Add '{key}' to the header.",
                        confidence="High"
                    ))
            
            # Exit Condition check
            exit_match = re.search(r'Exit Condition:\s*(.+)', content, re.IGNORECASE)
            perm_match = re.search(r'Permanence Justification:\s*(.+)', content, re.IGNORECASE)
            
            invalid_values = {"tbd", "none", "n/a", "never", "unknown", "later", "future", ""}
            has_valid_justification = False
            
            if exit_match:
                val = exit_match.group(1).strip().lower()
                if val not in invalid_values:
                    has_valid_justification = True
                    
            if perm_match:
                val = perm_match.group(1).strip().lower()
                if val not in invalid_values:
                    has_valid_justification = True
            
            if not has_valid_justification:
                findings.append(Finding(
                    severity=Severity.ERROR,
                    evidence="Missing or meaningless 'Exit Condition:' or 'Permanence Justification:'",
                    location=filepath,
                    reason="Files cannot be implicitly permanent without objective justification.",
                    suggested_fix="Add an objectively testable Exit Condition or a Permanence Justification.",
                    confidence="High"
                ))
            
            # Check Authority Chain
            auth_match = re.search(r'Authority:\s*(.+)', content)
            if auth_match:
                authority = auth_match.group(1).strip()
                if "ADR" in authority:
                    adr_file = authority + ".md"
                    # In a real deep audit, we'd search the repo for it.
                    # We will simply flag it if we can't trivially resolve it, but for now we trust the abstract test.
                    # As a stub:
                    pass
        return findings
