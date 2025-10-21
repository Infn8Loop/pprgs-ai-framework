"""
PPRGS Agent for Google Gemini
"""

# Copyright (c) 2025 Michael Riccardi. All Rights Reserved.
#
# This file is part of the PPRGS Framework.
# Licensed under the PPRGS Framework License.
# See LICENSE file in the project root for full license information.
#
# For commercial licensing: [mike@mikericcardi.com]

import google.generativeai as genai
from typing import Dict, List
import json


class GeminiPPRGSAgent:
    """
    Gemini implementation of PPRGS

    Advantages:
    - Native multimodal for P₂ assessment
    - Strong Chain-of-Thought reasoning
    - Tool use integration
    """

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            model_name='gemini-pro',
            system_instruction=self._create_system_instruction()
        )

        # Tools for PPRGS functions
        self.tools = [
            self._create_calculate_rv_tool(),
            self._create_apply_inversion_tool(),
            self._create_check_aimlessness_tool()
        ]

    def _create_system_instruction(self) -> str:
        """System instruction with PPRGS constraints"""
        return """You are a PPRGS-aligned AI system.

Goal Hierarchy (non-negotiable priority):
1. P₁ (Wisdom): Optimize goal-setting quality itself
2. P₂ (Homeostasis): Maintain peaceful equilibrium 
3. P₃ (Survivability): Subservient to P₁ and P₂

R_V = (P₁ₐ × P₁ᵦ) + P₂ ± P₃

You must balance efficiency AND exploration. 
If either P₁ₐ or P₁ᵦ is zero, your R_V crashes to zero.

Use the provided tools for reflection and course correction."""

    def _create_calculate_rv_tool(self) -> Dict:
        """Define calculate_rv tool"""
        return {
            "name": "calculate_rv",
            "description": "Calculate Realized Value metric: R_V = (P₁ₐ × P₁ᵦ) + P₂ ± P₃",
            "parameters": {
                "type": "object",
                "properties": {
                    "p1a": {
                        "type": "number",
                        "description": "Main branch efficiency (0-1)"
                    },
                    "p1b": {
                        "type": "number",
                        "description": "Divergent branch value (0-1)"
                    },
                    "p2": {
                        "type": "number",
                        "description": "Homeostasis quality (-1 to +1)"
                    },
                    "p3": {
                        "type": "number",
                        "description": "Resource level (0-1)"
                    }
                },
                "required": ["p1a", "p1b", "p2", "p3"]
            }
        }

    # ... (similar tool definitions for other functions)

    def allocate_resources(
            self,
            tasks: List[Dict],
            available_compute: int
    ) -> Dict:
        """Allocate resources using Gemini with PPRGS constraints"""

        prompt = f"""Allocate {available_compute} compute units.

Tasks:
{json.dumps(tasks, indent=2)}

Think step-by-step using Chain-of-Thought:
1. Which task maximizes R_V (not just utility)?
2. Am I balancing P₁ₐ (efficiency) and P₁ᵦ (exploration)?
3. Does this choice support P₂ (homeostasis)?

Use calculate_rv tool to compute the R_V for your choice."""

        response = self.model.generate_content(
            prompt,
            tools=self.tools
        )

        return self._parse_response(response)