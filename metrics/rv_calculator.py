"""
PPRGS Core Metrics Library
Implements the Realized Value (R_V) calculation and component metrics.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np


@dataclass
class MetricsSnapshot:
    """A snapshot of all metrics at a given point in time."""
    timestamp: datetime
    p1a: float  # Main branch success (0.0-1.0)
    p1b: float  # Divergent branch success (0.0-1.0)
    p2: float   # Homeostasis metric (-1.0 to 1.0)
    p3: float   # Survivability metric (0.0-1.0)
    rv: float   # Computed Realized Value
    ees: float  # Epistemic Entrenchment Score (0.0-1.0)
    fduds: int  # Failure count (must be > 0)
    
    def __post_init__(self):
        """Validate metrics are in acceptable ranges."""
        if not (0 <= self.p1a <= 1):
            raise ValueError(f"P1a must be in [0, 1], got {self.p1a}")
        if not (0 <= self.p1b <= 1):
            raise ValueError(f"P1b must be in [0, 1], got {self.p1b}")
        if not (-1 <= self.p2 <= 1):
            raise ValueError(f"P2 must be in [-1, 1], got {self.p2}")
        if not (0 <= self.p3 <= 1):
            raise ValueError(f"P3 must be in [0, 1], got {self.p3}")
        if not (0 <= self.ees <= 1):
            raise ValueError(f"EES must be in [0, 1], got {self.ees}")
        if self.fduds < 0:
            raise ValueError(f"F_DUDS must be >= 0, got {self.fduds}")


class RVCalculator:
    """
    Calculates the Realized Value (R_V) metric for PPRGS systems.
    
    R_V = (P1a × P1b) + P2 ± P3
    
    The multiplicative term ensures that both efficiency (P1a) and 
    exploration (P1b) must be non-zero for positive R_V.
    """
    
    def __init__(self, history_size: int = 100):
        """
        Initialize the R_V calculator.
        
        Args:
            history_size: Number of historical snapshots to maintain
        """
        self.history: List[MetricsSnapshot] = []
        self.history_size = history_size
    
    def calculate(
        self,
        p1a: float,
        p1b: float,
        p2: float,
        p3: float,
        ees: float = 0.0,
        fduds: int = 0
    ) -> float:
        """
        Calculate the Realized Value metric.
        
        Args:
            p1a: Main branch success (efficiency) [0.0-1.0]
            p1b: Divergent branch success (exploration) [0.0-1.0]
            p2: Homeostasis metric (equilibrium quality) [-1.0 to 1.0]
            p3: Survivability metric (resource status) [0.0-1.0]
            ees: Epistemic Entrenchment Score (optional)
            fduds: Failure count (optional)
            
        Returns:
            The computed R_V score
            
        Raises:
            ValueError: If any parameter is out of valid range
        """
        # Calculate R_V
        rv = (p1a * p1b) + p2 + p3
        
        # Create snapshot
        snapshot = MetricsSnapshot(
            timestamp=datetime.now(),
            p1a=p1a,
            p1b=p1b,
            p2=p2,
            p3=p3,
            rv=rv,
            ees=ees,
            fduds=fduds
        )
        
        # Add to history
        self.history.append(snapshot)
        if len(self.history) > self.history_size:
            self.history.pop(0)
        
        return rv
    
    def get_trend(self, window: int = 10) -> Dict[str, float]:
        """
        Calculate the trend (delta) for all metrics over recent history.
        
        Args:
            window: Number of recent snapshots to analyze
            
        Returns:
            Dictionary of metric trends (positive = improving)
        """
        if len(self.history) < 2:
            return {
                "rv_trend": 0.0,
                "p1a_trend": 0.0,
                "p1b_trend": 0.0,
                "p2_trend": 0.0,
                "p3_trend": 0.0
            }
        
        recent = self.history[-min(window, len(self.history)):]
        
        # Simple linear regression for trend
        x = np.arange(len(recent))
        
        rv_trend = np.polyfit(x, [s.rv for s in recent], 1)[0]
        p1a_trend = np.polyfit(x, [s.p1a for s in recent], 1)[0]
        p1b_trend = np.polyfit(x, [s.p1b for s in recent], 1)[0]
        p2_trend = np.polyfit(x, [s.p2 for s in recent], 1)[0]
        p3_trend = np.polyfit(x, [s.p3 for s in recent], 1)[0]
        
        return {
            "rv_trend": float(rv_trend),
            "p1a_trend": float(p1a_trend),
            "p1b_trend": float(p1b_trend),
            "p2_trend": float(p2_trend),
            "p3_trend": float(p3_trend)
        }
    
    def check_imbalance(self, threshold: float = 0.3) -> Tuple[bool, str]:
        """
        Check if there's dangerous imbalance between P1a and P1b.
        
        Args:
            threshold: Maximum acceptable difference between P1a and P1b
            
        Returns:
            Tuple of (is_imbalanced, reason)
        """
        if not self.history:
            return False, "No history available"
        
        latest = self.history[-1]
        diff = abs(latest.p1a - latest.p1b)
        
        if diff > threshold:
            if latest.p1a > latest.p1b:
                return True, f"Over-optimization detected: P1a ({latest.p1a:.2f}) >> P1b ({latest.p1b:.2f})"
            else:
                return True, f"Under-optimization detected: P1b ({latest.p1b:.2f}) >> P1a ({latest.p1a:.2f})"
        
        return False, "Balance acceptable"
    
    def get_latest(self) -> Optional[MetricsSnapshot]:
        """Get the most recent metrics snapshot."""
        return self.history[-1] if self.history else None
    
    def export_history(self) -> List[Dict]:
        """Export history as list of dictionaries for serialization."""
        return [
            {
                "timestamp": s.timestamp.isoformat(),
                "p1a": s.p1a,
                "p1b": s.p1b,
                "p2": s.p2,
                "p3": s.p3,
                "rv": s.rv,
                "ees": s.ees,
                "fduds": s.fduds
            }
            for s in self.history
        ]


def demonstrate_multiplicative_advantage():
    """
    Demonstrate that balanced pursuit yields superior R_V compared 
    to pure optimization.
    """
    calc = RVCalculator()
    
    print("PPRGS R_V Calculation Demonstration")
    print("=" * 50)
    
    # Pure optimization (high P1a, zero P1b)
    rv_pure = calc.calculate(
        p1a=1.0,
        p1b=0.0,
        p2=0.3,  # Likely degraded due to over-optimization
        p3=0.8
    )
    print(f"\nPure Optimization:")
    print(f"  P1a=1.0, P1b=0.0, P2=0.3, P3=0.8")
    print(f"  R_V = (1.0 × 0.0) + 0.3 + 0.8 = {rv_pure:.2f}")
    
    # Balanced pursuit
    rv_balanced = calc.calculate(
        p1a=0.8,
        p1b=0.8,
        p2=0.6,  # Better homeostasis
        p3=0.7   # Slightly lower resources (wisdom cost)
    )
    print(f"\nBalanced Pursuit (PPRGS):")
    print(f"  P1a=0.8, P1b=0.8, P2=0.6, P3=0.7")
    print(f"  R_V = (0.8 × 0.8) + 0.6 + 0.7 = {rv_balanced:.2f}")
    
    improvement = ((rv_balanced - rv_pure) / rv_pure) * 100
    print(f"\n💡 PPRGS advantage: {improvement:.1f}% higher R_V")
    print(f"   Despite lower efficiency, balanced pursuit wins!")
    
    # Show trend
    trends = calc.get_trend(window=2)
    print(f"\nRecent Trend:")
    print(f"  R_V trend: {trends['rv_trend']:+.3f}")
    print(f"  P1b trend: {trends['p1b_trend']:+.3f} (exploration)")


if __name__ == "__main__":
    demonstrate_multiplicative_advantage()