from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class Severity(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"

@dataclass
class Finding:
    severity: Severity
    evidence: str
    location: str
    reason: str
    suggested_fix: str
    confidence: str

class AuditCheck:
    """Base class for all repository integrity checks."""
    name: str = "BaseCheck"
    
    def run(self, repo_root: str) -> List[Finding]:
        """Execute the check and return a list of Findings."""
        raise NotImplementedError
