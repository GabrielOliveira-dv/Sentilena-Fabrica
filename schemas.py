from dataclasses import dataclass
from typing import List
@dataclass
class MissionContract:
    objective: str
    allowed_inputs: List[str]
    allowed_outputs: List[str]
    forbidden_actions: List[str]
    stop_conditions: List[str]

@dataclass
class DossierRequirements:
    timeline: bool = True
    facts: bool = True
    hypotheses: bool = True
    gaps: bool = True
    confidence: bool = True
    next_action: bool = True
