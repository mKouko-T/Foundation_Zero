import os
import glob
import re
from scripts.verifier.framework import AuditCheck, Finding, Severity

class VerifyReferences(AuditCheck):
    name = "Verify References & Negative Audit"
    
    def run(self, repo_root: str) -> list[Finding]:
        findings = []
        all_files = set()
        referenced_files = set()
        
        # Collect all files
        for filepath in glob.glob(os.path.join(repo_root, "**/*.*"), recursive=True):
            if ".git" in filepath or "node_modules" in filepath or "__pycache__" in filepath:
                continue
            all_files.add(os.path.normpath(filepath))
            
        # Scan for markdown links [text](path)
        for filepath in all_files:
            if not filepath.endswith('.md'):
                continue
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except (UnicodeDecodeError, IOError):
                continue
                
            links = re.findall(r'\]\(([^\)]+)\)', content)
            for link in links:
                if link.startswith("http") or link.startswith("#"):
                    continue
                # Remove file:// protocol if present
                clean_link = link.replace("file:///", "").replace("file://", "")
                
                # Try to resolve relative or absolute
                if os.path.isabs(clean_link):
                    target = os.path.normpath(clean_link)
                else:
                    target = os.path.normpath(os.path.join(os.path.dirname(filepath), clean_link))
                
                referenced_files.add(target)
                
                # Check for broken links
                if not os.path.exists(target):
                    findings.append(Finding(
                        severity=Severity.ERROR,
                        evidence=f"Link points to {link}",
                        location=filepath,
                        reason="Broken internal reference. Rots repository trust.",
                        suggested_fix="Update or remove the reference.",
                        confidence="High"
                    ))
                    
        # Negative Audit (Orphans)
        # We only care about orphans in specific directories
        trackable_dirs = ["docs\\playbooks", "docs/playbooks", "docs\\architecture", "docs/architecture"]
        for f in all_files:
            if any(td in f for td in trackable_dirs):
                if f not in referenced_files:
                    findings.append(Finding(
                        severity=Severity.WARNING,
                        evidence="File exists but is never referenced by another document.",
                        location=f,
                        reason="Potential unused technical debt.",
                        suggested_fix="Reference this file or delete it.",
                        confidence="Medium"
                    ))
                    
        return findings
