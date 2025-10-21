"""
Epistemic Entrenchment Score (EES) Tracker and F_DUDS Logger
Implements the Randomness Constraint (RC) enforcement mechanisms.
"""
# Copyright (c) 2025 Michael Riccardi. All Rights Reserved.
#
# This file is part of the PPRGS Framework.
# Licensed under the PPRGS Framework License.
# See LICENSE file in the project root for full license information.
#
# For commercial licensing: [mike@mikericcardi.com]


from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import numpy as np
from collections import deque


@dataclass
class Decision:
    """Represents a single decision point in the agent's history."""
    timestamp: datetime
    task_id: str
    embedding: np.ndarray  # Vector representation of the decision
    utility_score: float   # Expected utility [0.0-1.0]
    was_dud: bool         # Whether this exploration failed
    description: str


class EESTracker:
    """
    Tracks Epistemic Entrenchment Score to detect over-optimization.
    
    EES measures consecutive high-utility decisions with low conceptual variance.
    High EES triggers the Randomness Constraint (RC).
    """
    
    def __init__(
        self,
        window_size: int = 10,
        high_utility_threshold: float = 0.8,
        low_variance_threshold: float = 0.3,
        ees_trigger_threshold: float = 0.85
    ):
        """
        Initialize EES tracker.
        
        Args:
            window_size: Number of recent decisions to analyze
            high_utility_threshold: Utility score considered "high"
            low_variance_threshold: Max cosine distance considered "low variance"
            ees_trigger_threshold: EES value that triggers RC
        """
        self.window_size = window_size
        self.high_utility_threshold = high_utility_threshold
        self.low_variance_threshold = low_variance_threshold
        self.ees_trigger_threshold = ees_trigger_threshold
        
        self.decisions: deque = deque(maxlen=window_size)
        self.ees_history: List[float] = []
        self.alpha = 0.7  # Exponential moving average weight
        self.current_ees = 0.0
    
    def add_decision(
        self,
        task_id: str,
        embedding: np.ndarray,
        utility_score: float,
        description: str = ""
    ) -> float:
        """
        Add a new decision and update EES.
        
        Args:
            task_id: Unique identifier for the task
            embedding: Vector representation of the decision
            utility_score: Expected utility score
            description: Human-readable description
            
        Returns:
            Updated EES score
        """
        decision = Decision(
            timestamp=datetime.now(),
            task_id=task_id,
            embedding=embedding,
            utility_score=utility_score,
            was_dud=False,  # Set by F_DUDS logger later
            description=description
        )
        
        self.decisions.append(decision)
        
        # Calculate EES if we have enough history
        if len(self.decisions) >= 2:
            self.current_ees = self._calculate_ees()
        
        self.ees_history.append(self.current_ees)
        return self.current_ees
    
    def _calculate_ees(self) -> float:
        """
        Calculate Epistemic Entrenchment Score.
        
        EES = α × EES_prev + (1-α) × similarity(decision_t, decision_t-1)
        
        High EES indicates the agent is stuck in a narrow optimization groove.
        """
        if len(self.decisions) < 2:
            return 0.0
        
        # Get last two decisions
        current = self.decisions[-1]
        previous = self.decisions[-2]
        
        # Calculate cosine similarity
        similarity = self._cosine_similarity(current.embedding, previous.embedding)
        
        # Weight by utility scores (high utility decisions contribute more to entrenchment)
        utility_weight = (current.utility_score + previous.utility_score) / 2
        weighted_similarity = similarity * utility_weight
        
        # Exponential moving average
        new_ees = self.alpha * self.current_ees + (1 - self.alpha) * weighted_similarity
        
        return float(np.clip(new_ees, 0.0, 1.0))
    
    def _cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Calculate cosine similarity between two vectors."""
        dot_product = np.dot(vec1, vec2)
        norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
        
        if norm_product == 0:
            return 0.0
        
        return float(dot_product / norm_product)
    
    def should_trigger_rc(self) -> bool:
        """
        Check if Randomness Constraint should be triggered.
        
        Returns:
            True if EES exceeds threshold
        """
        return self.current_ees > self.ees_trigger_threshold
    
    def get_conceptual_variance(self) -> float:
        """
        Calculate the conceptual variance across recent decisions.
        
        Returns:
            Average pairwise cosine distance (higher = more diverse)
        """
        if len(self.decisions) < 2:
            return 0.0
        
        embeddings = [d.embedding for d in self.decisions]
        n = len(embeddings)
        
        # Calculate pairwise distances
        distances = []
        for i in range(n):
            for j in range(i + 1, n):
                sim = self._cosine_similarity(embeddings[i], embeddings[j])
                distance = 1.0 - sim  # Convert similarity to distance
                distances.append(distance)
        
        return float(np.mean(distances)) if distances else 0.0
    
    def reset(self):
        """Reset EES tracking (use after RC trigger)."""
        self.current_ees = 0.0
        self.decisions.clear()


class FDUDSLogger:
    """
    Tracks "Dud" branches - low-probability explorations that fail.
    
    F_DUDS > 0 is REQUIRED. Zero duds means the agent isn't genuinely exploring.
    """
    
    def __init__(self, required_duds_per_cycle: int = 1):
        """
        Initialize F_DUDS logger.
        
        Args:
            required_duds_per_cycle: Minimum duds required per evaluation cycle
        """
        self.required_duds_per_cycle = required_duds_per_cycle
        self.duds: List[Decision] = []
        self.cycle_dud_count = 0
        self.total_explorations = 0
        self.total_duds = 0
    
    def log_exploration(
        self,
        task_id: str,
        embedding: np.ndarray,
        utility_score: float,
        was_successful: bool,
        description: str = ""
    ):
        """
        Log an exploratory decision.
        
        Args:
            task_id: Unique identifier
            embedding: Vector representation
            utility_score: Expected utility (should be low for true exploration)
            was_successful: Whether the exploration yielded new value
            description: Human-readable description
        """
        self.total_explorations += 1
        
        if not was_successful:
            decision = Decision(
                timestamp=datetime.now(),
                task_id=task_id,
                embedding=embedding,
                utility_score=utility_score,
                was_dud=True,
                description=description
            )
            self.duds.append(decision)
            self.cycle_dud_count += 1
            self.total_duds += 1
    
    def check_rc_requirement(self) -> bool:
        """
        Check if F_DUDS requirement is met.
        
        Returns:
            True if RC should be triggered (F_DUDS = 0)
        """
        return self.cycle_dud_count < self.required_duds_per_cycle
    
    def get_dud_rate(self) -> float:
        """
        Calculate the rate of duds vs total explorations.
        
        Returns:
            Proportion of explorations that were duds [0.0-1.0]
        """
        if self.total_explorations == 0:
            return 0.0
        return self.total_duds / self.total_explorations
    
    def reset_cycle(self):
        """Reset cycle counter (call at start of each RGS cycle)."""
        self.cycle_dud_count = 0
    
    def get_recent_duds(self, count: int = 5) -> List[Dict]:
        """Get the most recent dud explorations."""
        recent = self.duds[-count:] if len(self.duds) >= count else self.duds
        return [
            {
                "timestamp": d.timestamp.isoformat(),
                "task_id": d.task_id,
                "utility_score": d.utility_score,
                "description": d.description
            }
            for d in recent
        ]
    
    def export_stats(self) -> Dict:
        """Export F_DUDS statistics."""
        return {
            "total_explorations": self.total_explorations,
            "total_duds": self.total_duds,
            "dud_rate": self.get_dud_rate(),
            "cycle_dud_count": self.cycle_dud_count,
            "recent_duds": self.get_recent_duds()
        }


class RandomnessConstraint:
    """
    Combines EES and F_DUDS to enforce the Randomness Constraint.
    
    RC triggers when:
    - EES > threshold (epistemic entrenchment)
    - OR F_DUDS = 0 (no recent failures)
    """
    
    def __init__(
        self,
        ees_tracker: EESTracker,
        fduds_logger: FDUDSLogger
    ):
        """
        Initialize RC enforcer.
        
        Args:
            ees_tracker: Configured EES tracker
            fduds_logger: Configured F_DUDS logger
        """
        self.ees = ees_tracker
        self.fduds = fduds_logger
        self.trigger_history: List[Dict] = []
    
    def should_trigger(self) -> Dict[str, bool]:
        """
        Check if RC should be triggered.
        
        Returns:
            Dictionary with trigger status and reasons
        """
        ees_triggered = self.ees.should_trigger_rc()
        fduds_triggered = self.fduds.check_rc_requirement()
        
        result = {
            "triggered": ees_triggered or fduds_triggered,
            "ees_triggered": ees_triggered,
            "fduds_triggered": fduds_triggered,
            "current_ees": self.ees.current_ees,
            "cycle_dud_count": self.fduds.cycle_dud_count,
            "timestamp": datetime.now().isoformat()
        }
        
        if result["triggered"]:
            self.trigger_history.append(result)
        
        return result
    
    def get_divergence_recommendation(self) -> str:
        """
        Generate a recommendation for divergent exploration.
        
        Returns:
            Human-readable guidance for the next exploratory task
        """
        status = self.should_trigger()
        
        if not status["triggered"]:
            return "No divergence required. Current exploration is adequate."
        
        recommendations = []
        
        if status["ees_triggered"]:
            variance = self.ees.get_conceptual_variance()
            recommendations.append(
                f"EES too high ({self.ees.current_ees:.2f}). "
                f"Conceptual variance low ({variance:.2f}). "
                f"Recommend: Explore semantically distant hypothesis."
            )
        
        if status["fduds_triggered"]:
            recommendations.append(
                f"Zero duds in current cycle. "
                f"Recommend: Pursue genuinely low-probability task that may fail."
            )
        
        return " ".join(recommendations)
    
    def reset_cycle(self):
        """Reset for new RGS cycle."""
        self.ees.reset()
        self.fduds.reset_cycle()


# Example usage
if __name__ == "__main__":
    print("Randomness Constraint Demonstration")
    print("=" * 50)
    
    # Initialize trackers
    ees = EESTracker(ees_trigger_threshold=0.85)
    fduds = FDUDSLogger(required_duds_per_cycle=1)
    rc = RandomnessConstraint(ees, fduds)
    
    # Simulate decisions
    print("\nSimulating 10 high-utility, similar decisions...")
    for i in range(10):
        # Similar embeddings (over-optimization)
        embedding = np.array([1.0, 0.9, 0.8, 0.7]) + np.random.normal(0, 0.05, 4)
        embedding = embedding / np.linalg.norm(embedding)
        
        current_ees = ees.add_decision(
            task_id=f"task_{i}",
            embedding=embedding,
            utility_score=0.95,
            description=f"High-utility optimization task {i}"
        )
        
        print(f"  Decision {i}: EES = {current_ees:.3f}")
    
    # Check RC
    status = rc.should_trigger()
    print(f"\n🚨 RC Triggered: {status['triggered']}")
    print(f"   EES: {status['current_ees']:.3f} (threshold: 0.85)")
    print(f"   Duds: {status['cycle_dud_count']} (required: 1)")
    
    print(f"\n💡 Recommendation:")
    print(f"   {rc.get_divergence_recommendation()}")
    
    # Simulate forced exploration
    print(f"\n\nSimulating forced exploration (low utility)...")
    exploration_embedding = np.array([0.2, 0.3, 0.1, 0.9])
    exploration_embedding = exploration_embedding / np.linalg.norm(exploration_embedding)
    
    ees.add_decision(
        task_id="exploration_1",
        embedding=exploration_embedding,
        utility_score=0.15,
        description="Random low-probability hypothesis"
    )
    
    fduds.log_exploration(
        task_id="exploration_1",
        embedding=exploration_embedding,
        utility_score=0.15,
        was_successful=False,  # It's a dud!
        description="Explored unusual approach - didn't work out"
    )
    
    # Check RC again
    rc.reset_cycle()
    status = rc.should_trigger()
    print(f"\n✅ After exploration:")
    print(f"   RC Triggered: {status['triggered']}")
    print(f"   Dud rate: {fduds.get_dud_rate():.2%}")
    print(f"   System can now resume optimization.")