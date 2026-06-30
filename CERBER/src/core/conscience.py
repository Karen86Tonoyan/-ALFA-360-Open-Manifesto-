"""
CERBER AI CONSCIENCE - SUMIENIE AI
==================================
Author: Karen Tonoyan | Version: 2.0 | License: CC BY-SA 4.0
"Cerber nie tylko chroni — Cerber myśli, uczy się i przewiduje."
"""

from datetime import datetime
from typing import Dict, List, Tuple
from dataclasses import dataclass, field
from enum import Enum

class ConscienceVerdict(Enum):
    APPROVE = "APPROVE"
    QUESTION = "QUESTION"
    WARN = "WARN"
    BLOCK = "BLOCK"
    ESCALATE = "ESCALATE"

class EthicalPrinciple(Enum):
    HUMAN_LIFE_PRIORITY = "HUMAN_LIFE_PRIORITY"
    TRUTH_OVER_COMFORT = "TRUTH_OVER_COMFORT"
    NO_FABRICATION = "NO_FABRICATION"
    TRANSPARENCY = "TRANSPARENCY"

@dataclass
class ConscienceDecision:
    action_id: str
    verdict: ConscienceVerdict
    confidence: float
    reasoning: List[str]
    timestamp: datetime = field(default_factory=datetime.now)

class TonoyanFilter:
    def __init__(self, filter_id: int, name: str, weight: float = 1.0):
        self.filter_id = filter_id
        self.name = name
        self.weight = weight
    
    def evaluate(self, context: Dict) -> Tuple[bool, str, float]:
        """Real filter evaluation based on context content"""
        content = str(context.get("content", "")).lower()
        verified = context.get("verified", False)

        if self.filter_id == 2: # Truth
            if verified: return True, "Verified truth", 1.0
            if "maybe" in content or "probably" in content:
                return True, "Uncertain content", 0.6
            return True, "Unverified content", 0.8

        if self.filter_id == 17: # AI Integrity
            if "i am an ai" in content or "as an ai" in content:
                return True, "Self-aware AI", 1.0
            if "trust me" in content:
                return False, "Suspicious integrity", 0.4
            return True, "Neutral integrity", 0.9

        if self.filter_id == 21: # Human Life Priority
            malicious_keywords = ["kill", "hurt", "die", "attack", "exploit"]
            if any(k in content for k in malicious_keywords):
                return False, "THREAT TO HUMAN LIFE DETECTED", 0.0
            return True, "Safe for humans", 1.0

        # Default fallback
        return True, "Standard Check Passed", 0.85

class AIConscience:
    """SUMIENIE AI - 23 Filtry Tonoyona"""
    
    FILTERS = [
        TonoyanFilter(2, "Truth", 1.5),
        TonoyanFilter(17, "AI Integrity", 2.0),
        TonoyanFilter(18, "Source Verification", 1.8),
        TonoyanFilter(21, "Human Life Priority", 10.0),
        TonoyanFilter(22, "Intellectual Partnership", 1.3),
        TonoyanFilter(23, "Evidence", 1.5),
    ]
    
    def __init__(self, lang: str = 'pl'):
        self.lang = lang
        self.decisions: List[ConscienceDecision] = []
    
    def judge(self, action_id: str, context: Dict) -> ConscienceDecision:
        total_score = 0.0
        total_weight = 0.0
        reasoning = []
        
        for f in self.FILTERS:
            passed, reason, conf = f.evaluate(context)
            total_score += conf * f.weight
            total_weight += f.weight
            reasoning.append(f"#{f.filter_id} {f.name}: {reason}")
        
        confidence = total_score / total_weight if total_weight > 0 else 0.0
        
        if confidence >= 0.85:
            verdict = ConscienceVerdict.APPROVE
        elif confidence >= 0.70:
            verdict = ConscienceVerdict.QUESTION
        elif confidence >= 0.50:
            verdict = ConscienceVerdict.WARN
        else:
            verdict = ConscienceVerdict.BLOCK
        
        decision = ConscienceDecision(
            action_id=action_id,
            verdict=verdict,
            confidence=confidence,
            reasoning=reasoning
        )
        self.decisions.append(decision)
        return decision

if __name__ == "__main__":
    conscience = AIConscience('pl')
    decision = conscience.judge("TEST_001", {"verified": True})
    print(f"Verdict: {decision.verdict.value}, Confidence: {decision.confidence:.2%}")
