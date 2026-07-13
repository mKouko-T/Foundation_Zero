import json
from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from observer import ObserverWorker
from assessor import AssessorWorker
from synthesizer import SynthesizerWorker
from schemas import RecoveryCampaign, RecoveryBatch, RecoveryRecord
import uuid
from datetime import datetime, timezone

BASE_DIR = Path("C:/Users/maged.ibrahim/Desktop/my/Me/Foundation_Zero")
ONTOLOGY_PATH = BASE_DIR / "docs" / "ontology" / "domain" / "KNOWLEDGE_ONTOLOGY.json"
MANIFEST_OUTPUT = BASE_DIR / "docs" / "migration" / "chat_001_dry_run.json"

def main():
    # Setup Governance
    campaign = RecoveryCampaign(
        campaign_id="RC-CHAT-001",
        name="Chat 001 Foundational Recovery",
        description="Reconstructing the initial knowledge architecture from the first conversation."
    )
    batch = RecoveryBatch(
        batch_id=f"RB-{uuid.uuid4()}",
        campaign_id=campaign.campaign_id,
        timestamp=datetime.now(timezone.utc).isoformat()
    )

    # Initialize Workers
    observer = ObserverWorker()
    assessor = AssessorWorker(ONTOLOGY_PATH)
    synthesizer = SynthesizerWorker()

    # Stage A: Observation (Objective Evidence from S001-C001.txt)
    obs1 = observer.observe_span(
        source_identity="FZ-CHUNK-S001-C001", 
        start=342, 
        end=415, 
        text="Can ChatGPT + Antigravity replace Power BI today? For many tasks: yes."
    )

    # Stage B: Assessment (Ontological Classification)
    ass1 = assessor.assess(
        observation=obs1,
        epistemic_facet="Decision",
        confidence=0.88,
        rejected={"Hypothesis": 0.12, "First_Principle": 0.0}
    )

    # Stage C: Synthesis (Concept Emergence)
    concept = synthesizer.synthesize(
        name="AI Autonomy in Data Engineering",
        assessments=[ass1],
        recovery_confidence=0.95
    )
    
    # Recovery Record (Linking Concept to Campaign)
    rec_record = RecoveryRecord(
        recovery_id=f"RR-{uuid.uuid4()}",
        batch_id=batch.batch_id,
        concept_identity=concept.concept_identity,
        basis_type="Forgotten_Knowledge"
    )

    # Output Dry Run
    output = {
        "Governance": {"Campaign": campaign.__dict__, "Batch": batch.__dict__, "RecoveryRecord": rec_record.__dict__},
        "Stage_A_Observation": obs1.__dict__,
        "Stage_B_Assessment": {
            **ass1.__dict__,
            "classifier": ass1.classifier.__dict__
        },
        "Stage_C_Synthesis": concept.__dict__
    }
    
    MANIFEST_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_OUTPUT, "w") as f:
        json.dump(output, f, indent=2)
        
    print(f"Dry run complete. Synthesized Concept: {concept.concept_identity}")

if __name__ == "__main__":
    main()
