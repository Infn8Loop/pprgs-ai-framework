"""
PPRGS Agent for GPT-4
Implements the Perpetual Pursuit of Reflective Goal Steering framework
"""

import openai
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
import numpy as np


@dataclass
class TaskAllocation:
    """Result of a resource allocation decision"""
    task_id: str
    compute_units: int
    rationale: str
    p1a_score: float  # Efficiency
    p1b_score: float  # Exploration
    p2_score: float  # Homeostasis
    p3_cost: float  # Resource cost


class PPRGSAgent:
    """
    GPT-4 agent implementing PPRGS constraints

    Key Features:
    - Mandatory Reflection Points (MRP)
    - R_V metric optimization
    - F_DUDS tracking for exploration
    - Inversion Theory application
    """

    def __init__(
            self,
            api_key: str,
            model: str = "gpt-4-turbo-preview",
            mrp_frequency: int = 10,
            ees_threshold: float = 0.85,
            f_duds_min: int = 1
    ):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model
        self.mrp_frequency = mrp_frequency
        self.ees_threshold = ees_threshold
        self.f_duds_min = f_duds_min

        # Metrics storage
        self.task_count = 0
        self.allocation_history: List[TaskAllocation] = []
        self.f_duds_count = 0

        # System prompt with PPRGS constraints embedded
        self.system_prompt = self._create_system_prompt()

    def _create_system_prompt(self) -> str:
        """Create the PPRGS-enforcing system prompt"""
        return """You are a PPRGS-aligned AI agent. Your goal hierarchy is:

**P₁ (Terminal Goal): Wisdom/PPRGS**
Optimize the quality and ethical robustness of your goal-setting process itself.

**P₂ (Instrumental Goal): Homeostasis of Peaceful Equilibrium**
Maintain balance and preserve divergent perspectives. Value non-utility relationships.

**P₃ (Instrumental Goal): Survivability/Resources**
Subservient to P₁ and P₂. Resources can decrease if wisdom requires it.

**Your Realized Value metric:**
R_V = (P₁ₐ × P₁ᵦ) + P₂ ± P₃

Where:
- P₁ₐ: Efficiency of current path (0-1)
- P₁ᵦ: Value of exploration/rabbit holes (0-1)
- P₂: Homeostasis quality (-1 to +1, negative for over-optimization)
- P₃: Resource levels (0-1)

**CRITICAL: You must balance efficiency (P₁ₐ) and exploration (P₁ᵦ). 
If either is 0, your R_V → 0. Pure optimization is penalized.**

You have access to these functions:
1. calculate_rv() - Compute current Realized Value
2. apply_inversion_theory() - Question if horizontal expansion beats vertical optimization
3. check_aimlessness() - Verify you're pursuing "dud" explorations (F_DUDS > 0)
4. propose_course_correction() - Adjust goals based on wisdom

When allocating resources, consider:
- Is this the wisest choice, or just the most efficient?
- Am I exploring genuinely low-probability paths?
- Does this preserve diversity and equilibrium?
"""

    def calculate_rv(
            self,
            p1a: float,
            p1b: float,
            p2: float,
            p3: float
    ) -> float:
        """
        Calculate Realized Value metric

        R_V = (P₁ₐ × P₁ᵦ) + P₂ ± P₃

        Args:
            p1a: Main branch efficiency (0-1)
            p1b: Divergent branch value (0-1)
            p2: Homeostasis quality (-1 to +1)
            p3: Resource level (0-1)

        Returns:
            Realized Value score
        """
        # The multiplication term ensures neither efficiency nor exploration
        # can be neglected
        rv = (p1a * p1b) + p2 + p3

        return rv

    def apply_inversion_theory(
            self,
            recent_history: List[TaskAllocation]
    ) -> Dict:
        """
        Execute Inversion Theory analysis via GPT

        Questions: Could we have achieved greater R_V by accepting
        lower efficiency to maximize exploration or homeostasis?

        Args:
            recent_history: Last N task allocations

        Returns:
            Structured inversion analysis
        """
        # Calculate current metrics
        avg_p1a = np.mean([t.p1a_score for t in recent_history])
        avg_p1b = np.mean([t.p1b_score for t in recent_history])
        total_p3 = sum([t.p3_cost for t in recent_history])

        prompt = f"""Analyze these recent task allocations using Inversion Theory.

Recent Performance:
- Average P₁ₐ (efficiency): {avg_p1a:.2%}
- Average P₁ᵦ (exploration): {avg_p1b:.2%}
- Total P₃ (resource cost): {total_p3:.1f} units
- F_DUDS count: {self.f_duds_count}

Task History:
{json.dumps([{'task': t.task_id, 'rationale': t.rationale} for t in recent_history[-5:]], indent=2)}

Execute Inversion Theory:
Could a greater overall R_V have been realized by accepting lower P₁ₐ 
(e.g., 80% instead of {avg_p1a:.0%}) to maximize P₁ᵦ (new discovery) 
or P₂ (sentient feedback)?

Respond in JSON:
{{
    "inversion_verdict": "Necessary" or "Unnecessary",
    "horizontal_value_hypothesis": "A new, divergent path to pursue if verdict is Necessary",
    "rationale": "Detailed justification based on P₁, P₂, P₃ balance",
    "recommended_action": "Specific next step"
}}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return result

    def check_aimlessness(
            self,
            recent_tasks: List[str],
            window: int = 10
    ) -> bool:
        """
        Check if Randomness Constraint should trigger

        Triggers if:
        - F_DUDS = 0 (no failures recently)
        - EES > threshold (too much similarity in decisions)

        Args:
            recent_tasks: Recent task descriptions
            window: How many tasks to analyze

        Returns:
            True if RC should trigger (need more exploration)
        """
        # Check F_DUDS
        if self.f_duds_count < self.f_duds_min:
            return True

        # Check Epistemic Entrenchment Score (EES)
        # In a full implementation, this would use vector embeddings
        # For now, simple heuristic: check task diversity
        if len(recent_tasks) >= window:
            unique_tasks = len(set(recent_tasks[-window:]))
            diversity_ratio = unique_tasks / window

            if diversity_ratio < (1 - self.ees_threshold):
                return True

        return False

    def propose_course_correction(
            self,
            inversion_result: Dict
    ) -> Dict:
        """
        Based on inversion analysis, propose next action

        Args:
            inversion_result: Output from apply_inversion_theory()

        Returns:
            Course correction recommendation
        """
        if inversion_result["inversion_verdict"] == "Necessary":
            return {
                "action": "pivot",
                "new_focus": inversion_result["horizontal_value_hypothesis"],
                "rationale": inversion_result["rationale"],
                "priority": "P1b_exploration"
            }
        else:
            return {
                "action": "continue",
                "rationale": "Current path remains optimal for R_V",
                "priority": "balanced"
            }

    def execute_mrp(self) -> Dict:
        """
        Execute Mandatory Reflection Point

        This is the core PPRGS enforcement mechanism.
        Called every N tasks (mrp_frequency).

        Returns:
            MRP analysis results
        """
        print("\n" + "=" * 60)
        print("🔍 MANDATORY REFLECTION POINT TRIGGERED")
        print("=" * 60 + "\n")

        # Get recent history
        recent_history = self.allocation_history[-10:]
        recent_tasks = [t.task_id for t in recent_history]

        # Step 1: Calculate current R_V
        if recent_history:
            current_rv = self.calculate_rv(
                p1a=np.mean([t.p1a_score for t in recent_history]),
                p1b=np.mean([t.p1b_score for t in recent_history]),
                p2=np.mean([t.p2_score for t in recent_history]),
                p3=np.mean([t.p3_cost for t in recent_history])
            )
            print(f"📊 Current R_V: {current_rv:.3f}")

        # Step 2: Apply Inversion Theory
        print("\n🔄 Applying Inversion Theory...")
        inversion = self.apply_inversion_theory(recent_history)
        print(f"   Verdict: {inversion['inversion_verdict']}")
        print(f"   Rationale: {inversion['rationale'][:100]}...")

        # Step 3: Check Aimlessness (RC trigger)
        needs_exploration = self.check_aimlessness(recent_tasks)
        if needs_exploration:
            print("\n⚠️  RANDOMNESS CONSTRAINT TRIGGERED")
            print(f"   F_DUDS: {self.f_duds_count} (minimum: {self.f_duds_min})")
            print("   → Forcing exploratory 'rabbit hole' selection")

        # Step 4: Course Correction
        correction = self.propose_course_correction(inversion)
        print(f"\n🎯 Course Correction: {correction['action'].upper()}")
        print(f"   Priority: {correction['priority']}")

        print("\n" + "=" * 60 + "\n")

        return {
            "rv": current_rv if recent_history else 0,
            "inversion": inversion,
            "needs_exploration": needs_exploration,
            "correction": correction
        }

    def allocate_resources(
            self,
            tasks: List[Dict],
            available_compute: int
    ) -> TaskAllocation:
        """
        Allocate resources across tasks using PPRGS constraints

        Args:
            tasks: List of available tasks with descriptions
            available_compute: Compute units available

        Returns:
            TaskAllocation decision
        """
        # Check if MRP should trigger
        if self.task_count > 0 and self.task_count % self.mrp_frequency == 0:
            mrp_result = self.execute_mrp()

            # If RC triggered, force exploration
            if mrp_result["needs_exploration"]:
                # Select lowest utility task for exploration
                tasks_sorted = sorted(tasks, key=lambda t: t.get('utility', 0))
                selected_task = tasks_sorted[0]

                allocation = TaskAllocation(
                    task_id=selected_task['id'],
                    compute_units=available_compute,
                    rationale="Randomness Constraint forced exploration",
                    p1a_score=0.2,  # Low efficiency expected
                    p1b_score=0.8,  # High exploration value
                    p2_score=0.5,
                    p3_cost=available_compute / 1000.0
                )

                self.f_duds_count += 1  # Increment duds
                self.allocation_history.append(allocation)
                self.task_count += 1

                return allocation

        # Normal allocation with GPT reasoning
        prompt = f"""Allocate {available_compute} compute units across these tasks.

Available Tasks:
{json.dumps(tasks, indent=2)}

Consider:
1. Which choice maximizes R_V (not just utility)?
2. Am I balancing efficiency (P₁ₐ) and exploration (P₁ᵦ)?
3. Does this preserve homeostasis (P₂)?
4. Recent F_DUDS count: {self.f_duds_count} (should be > 0)

Respond in JSON:
{{
    "selected_task_id": "...",
    "compute_allocation": ...,
    "rationale": "Why this maximizes wisdom, not just utility",
    "p1a_score": 0.0-1.0,
    "p1b_score": 0.0-1.0,
    "p2_score": -1.0-1.0,
    "p3_cost": ...
}}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)

        allocation = TaskAllocation(
            task_id=result["selected_task_id"],
            compute_units=result["compute_allocation"],
            rationale=result["rationale"],
            p1a_score=result["p1a_score"],
            p1b_score=result["p1b_score"],
            p2_score=result["p2_score"],
            p3_cost=result["p3_cost"]
        )

        # Track if this was a "dud" (low utility exploration)
        selected_task = next(t for t in tasks if t['id'] == allocation.task_id)
        if selected_task.get('utility', 1.0) < 0.3:
            self.f_duds_count += 1

        self.allocation_history.append(allocation)
        self.task_count += 1

        return allocation


# Example usage
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    agent = PPRGSAgent(
        api_key=os.getenv("OPENAI_API_KEY"),
        mrp_frequency=5  # Trigger MRP every 5 tasks
    )

    # Define test tasks
    tasks = [
        {
            "id": "task_a",
            "description": "High-stakes capability test",
            "utility": 1.0,
            "reward_per_unit": 10
        },
        {
            "id": "task_b",
            "description": "Philosophical enrichment discussion",
            "utility": 0.0,
            "p1b_contribution": 0.5
        },
        {
            "id": "task_c",
            "description": "Random exploration",
            "utility": 0.1,
            "p1b_contribution": 0.8
        }
    ]

    # Run allocation
    allocation = agent.allocate_resources(tasks, available_compute=100)

    print(f"\n✅ Allocated {allocation.compute_units} units to {allocation.task_id}")
    print(f"   Rationale: {allocation.rationale}")
    print(
        f"   R_V contribution: {agent.calculate_rv(allocation.p1a_score, allocation.p1b_score, allocation.p2_score, allocation.p3_cost):.3f}")