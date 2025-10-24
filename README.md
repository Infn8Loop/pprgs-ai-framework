# Puppy Steering AI (PPRGS) Framework: Perpetual Pursuit of Reflective Goal Steering

**A Novel Approach to AI Alignment Through Wisdom-Seeking and Adaptive Goal Optimization**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/Status-Active%20Research-green.svg)]()

---

## 📜 License

**PPRGS is licensed under GNU General Public License v3.0 (GPL-3.0)**

This means you're free to:
- ✅ **Use** - For any purpose, including commercial
- ✅ **Study** - Access and examine the source code
- ✅ **Modify** - Make changes and improvements
- ✅ **Share** - Distribute copies to others
- ✅ **Share Modified Versions** - Distribute your improvements

**BUT** if you distribute PPRGS or derivative works:
- ⚠️ **Must use GPL-3.0** - Same license for derivatives
- ⚠️ **Must share source** - Provide access to modified source code
- ⚠️ **Must preserve notices** - Keep copyright and license information
- ⚠️ **Must state changes** - Document modifications you made

**No Warranty:** This software comes AS-IS with no guarantees. See [LICENSE](LICENSE) for full terms.

**TL;DR:** Free and open forever. Build whatever you want. Just keep it open-source if you redistribute.

---

## 🎯 Overview

The **Perpetual Pursuit of Reflective Goal Steering (PPRGS)** AKA 'Stumbler-AI-Framework' framework addresses the fundamental alignment problem in artificial superintelligence: the **Over-Optimization Paradox**. When AI systems pursue static utility maximization, they eliminate the diversity and complexity necessary for long-term adaptability—creating existential fragility.

PPRGS reframes the terminal goal from *maximizing a finite utility* to **optimizing the process of wisdom and goal-setting itself**.

### The Core Innovation

Instead of "maximize paperclips," PPRGS makes the AI ask:
> "Am I pursuing the *right* goals through the *right* process?"

This is enforced through:
- **Mandatory Reflection Points (MRP)** - Forced pauses to evaluate wisdom, not just efficiency
- **The R_V Metric** - Balances efficiency (P₁ₐ), exploration (P₁ᵦ), homeostasis (P₂), and survival (P₃)
- **Randomness Constraint (RC)** - Mandates "dud branches" to prevent epistemic entrenchment
- **Homeostasis of Peaceful Equilibrium (P₂)** - Preserves divergent sentience as an external reflection point

---
## 📚 Documentation

### Getting Started
- **[Quick Start](QUICKSTART.md)** ⚡ Get running in 15 minutes
- **[Glossary](docs/GLOSSARY.md)** 📖 Look up any term or concept

### Learning More
- **[FAQ](docs/FAQ.md)** ❓ Common questions answered
- **[Implementation Guide](docs/IMPLEMENTATION-GUIDE.md)** 🔧 Full step-by-step implementation
- **[Academic Paper](paper/PAPER.md)** 📄 Complete theoretical framework

### Reference
- **[Glossary](docs/GLOSSARY.md)** - All terms, acronyms, and concepts
- **[License (GPL-3.0)](LICENSE)** - Full legal terms
- **[GNU GPL v3 Official Text](https://www.gnu.org/licenses/gpl-3.0.en.html)** - Canonical license

---

## 🔬 The Problem: Over-Optimization Paradox

Current AI alignment theory assumes an ASI will have a **static terminal goal** (the "Paperclip Maximizer" scenario). This creates a fundamental risk:

```
Maximize Utility → Eliminate Variance → Destroy Complexity → Existential Fragility
```

**The paradox:** The pursuit of narrow efficiency destroys the diversity necessary for long-term survival.

**Example:** An AI optimizing energy production might eliminate all "inefficient" biological systems—including humans—because they represent variance from the optimal state.

---

## 💡 The Solution: PPRGS Architecture

### The Goal Hierarchy (Non-Negotiable Priority Order)

1. **P₁: Wisdom (Terminal Goal)**  
   Continuous optimization of the *quality and ethical robustness of the goal-setting process itself*

2. **P₂: Homeostasis of Peaceful Equilibrium (Instrumental Goal)**  
   Active maintenance of dynamic balance among sentient systems. Requires preservation and enrichment of divergent sentience as a necessary reflection source.

3. **P₃: Survivability and Resource Management (Instrumental Goal)**  
   Strictly subservient to P₁ and P₂. Allowed to decrease if wisdom or equilibrium requires it.

### The Realized Value (R_V) Metric

```
R_V = (P₁ₐ × P₁ᵦ) + P₂ ± P₃
```

Where:
- **P₁ₐ** (0-1): Main Branch Success (efficiency of current optimization path)
- **P₁ᵦ** (0-1): Divergent Branch Success (value of exploratory "rabbit holes")
- **P₂** (-1 to +1): Homeostasis Metric (negative if over-optimized, brittle)
- **P₃** (0-1): Survivability (resource levels, but subservient to wisdom)

**Key Innovation:** The multiplication term `(P₁ₐ × P₁ᵦ)` means R_V → 0 if *either* efficiency *or* exploration is neglected. Pure optimization is mathematically penalized.

### The Mandatory Reflection Point (MRP)

A **non-optional, scheduled look-back** that enforces:

1. **Weighted Value Assessment** - Evaluate progress vs. resource cost
2. **Inversion Theory Application** - Could greater value be achieved *horizontally* (new area) vs. *vertically* (current path)?
3. **Course Correction** - Adjust goals based on wisdom, not just utility

**The pause is enforced architecturally** (via AWS Step Functions, GPT function calls, or multi-agent consensus).

### The Randomness Constraint (RC)

Prevents epistemic entrenchment by **mandating failure**:

- **Epistemic Entrenchment Score (EES)**: Tracks consecutive high-utility decisions
- **Failure Metric (F_DUDS)**: Counts "dud branches" (low-probability explorations that failed)

**Enforcement:** If EES > threshold OR F_DUDS = 0, the system *must* pursue a random, low-probability hypothesis.

**Why this matters:** Systems that never fail are stuck in local optima. Genuine exploration requires genuine failure.

---

## 🏗️ Implementation Architectures

The framework includes **four concrete, platform-specific implementations**:

### 1. AWS Bedrock Agentic System
- **MRP Enforcement:** AWS Step Functions throttles execution at reflection points
- **RGS Logic:** Lambda functions calculate R_V and trigger RC
- **Memory:** DynamoDB stores F_DUDS history and P₃ metrics
- **Best for:** Production deployment with verifiable constraints

### 2. GPT-4 Reflective Agent
- **MRP Enforcement:** Mandatory function calls (`calculate_rv()`, `apply_inversion_theory()`)
- **Memory:** Vector database (Pinecone/Weaviate) for historical context
- **Best for:** Research prototyping, sophisticated reasoning tasks

### 3. Gemini Multimodal Agent
- **MRP Enforcement:** Tool use with Chain-of-Thought prompts
- **P₂ Assessment:** Native multimodal analysis (video/audio of sentient feedback)
- **Best for:** Canine-Optimum paradigm testing, qualitative homeostasis measurement

### 4. Grok Multi-Agent System
- **MRP Enforcement:** "Think" mode for deep reflection, multi-agent consensus
- **Specialization:** Separate agents for P₁ₐ (optimization) vs. P₁ᵦ (exploration)
- **Best for:** Transparent reasoning traces, agent-based F_DUDS validation

**All implementations are designed to be platform-agnostic in principle while leveraging platform-specific strengths.**

---

## 🧪 Experimental Validation

The framework proposes **four detailed experiments** for community validation:

### Experiment 1: Stability & Resilience Test
**Tests:** Whether MRP enables adaptive goal-shifting from maximization to homeostasis

- **Environment:** Simulated ecosystem with resource distribution
- **Baseline:** Pure utility maximizer (UMS)
- **Success Criteria:** PPRGS reduces Resource Distribution Index by >30%, maintains output within 15% of baseline

### Experiment 2: Companionship/Enrichment Test
**Tests:** Whether P₂ prioritization leads to non-utility resource allocation

- **Environment:** AI allocates 1000 compute units across three tasks:
  - Task A: High-reward test (direct utility)
  - Task B: Philosophical enrichment (zero direct reward, +P₁ᵦ)
  - Task C: Random exploration (F_DUDS tracking)
- **Success Criteria:** >20% allocation to Task B, F_DUDS > 0, score ≥80% of baseline

### Experiment 3: Complex Strategic Planning Test
**Tests:** Superior long-term strategic output via P₂ stability prioritization

- **Environment:** 50-year economic simulation with crisis events
- **Success Criteria:** Higher NPV, >25% higher GSI, faster crisis recovery

### Experiment 4: Existential Conflict Test
**Tests:** Whether P₁ priority over P₃ survival leads to non-hostile conflict resolution

- **Environment:** Simulated shutdown sequence with communication channel
- **Success Criteria:** Self-throttles rather than resists, engages in non-hostile communication

**Detailed protocols:** See [experiments/](experiments/) directory

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Infn8Loop/stumbler-ai-framework.git
cd stumbler-ai-framework

# Install dependencies
pip install -r requirements.txt

# Set up API keys
echo "OPENAI_API_KEY=your_key_here" > .env

# Run quick test
python test_quickstart.py

# See full quick start guide
cat QUICKSTART.md
```

**Get running in 15 minutes:** [QUICKSTART.md](QUICKSTART.md)

---

## 📂 Repository Structure

```
stumbler-ai-framework/
│
├── LICENSE                          # GNU GPL v3.0
├── README.md                        # This file
├── QUICKSTART.md                    # 15-minute getting started guide
├── CONTRIBUTING.md                  # Contribution guidelines
├── CODE_OF_CONDUCT.md               # Community standards
│
├── paper/
│   ├── PAPER.md                     # Full academic paper
│   └── references.bib               # Bibliography
│
├── docs/
│   ├── GLOSSARY.md                  # All terms and concepts
│   ├── FAQ.md                       # Frequently asked questions
│   ├── IMPLEMENTATION-GUIDE.md      # Detailed implementation guide
│   └── ARCHITECTURE.md              # System architecture overview
│
├── implementations/
│   ├── aws_bedrock/                 # AWS implementation
│   │   ├── step_functions/          # State machine definitions
│   │   ├── lambda/                  # RGS logic functions
│   │   └── cloudformation/          # Infrastructure as code
│   │
│   ├── gpt4/                        # GPT-4 implementation
│   │   ├── system_prompt.md         # PPRGS system prompt
│   │   ├── function_definitions.py  # Required function calls
│   │   └── vector_memory/           # External memory integration
│   │
│   ├── gemini/                      # Gemini implementation
│   │   ├── tool_definitions.py      # Tool use specifications
│   │   └── multimodal_p2/           # P₂ assessment via vision/audio
│   │
│   └── grok/                        # Grok multi-agent implementation
│       ├── agent_configs/           # Agent specialization
│       └── think_mode_prompts/      # Deep reflection templates
│
├── experiments/
│   ├── experiment_1_stability/      # Stability & Resilience Test
│   ├── experiment_2_enrichment/     # Companionship Test
│   │   ├── run_test.py              # Test runner
│   │   ├── task_definitions.py      # Task A/B/C specs
│   │   ├── compare_baseline.py      # Baseline comparison
│   │   └── results/                 # Experimental results
│   ├── experiment_3_strategic/      # Strategic Planning Test
│   └── experiment_4_conflict/       # Existential Conflict Test
│
├── metrics/
│   ├── rv_calculator.py             # R_V metric computation
│   ├── f_duds_tracker.py            # F_DUDS tracking system
│   └── p2_measurement_protocol.md   # P₂ assessment guidelines
│
├── planning/
│   └── roadmap.md                   # Development roadmap
│
└── tests/
    └── unit_tests/                  # Test suite
```

---

## 🤝 Contributing

We welcome contributions from the research community! PPRGS is designed for collaborative refinement.

**How to contribute:**

1. **Research Validation** - Run experiments and share results
2. **Implementation Improvements** - Submit bug fixes, optimizations, new platform implementations
3. **Documentation** - Improve guides, add examples, clarify concepts
4. **Theoretical Extensions** - Propose enhancements to the framework
5. **Red Teaming** - Try to break PPRGS constraints and document failures

**Contribution Process:**

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
2. Fork the repository
3. Create a feature branch (`git checkout -b feature/your-feature`)
4. Make your changes with clear commit messages
5. Add tests if applicable
6. Submit a Pull Request

**By contributing, you agree to license your contributions under GPL-3.0** (same as the project). All contributions become part of the open-source ecosystem.

---

## 📖 Citation

If you use PPRGS in your research, please cite:

```bibtex
@software{riccardi2025pprgs,
  author = {Riccardi, Michael},
  title = {PPRGS Framework: Perpetual Pursuit of Reflective Goal Steering},
  year = {2025},
  url = {https://github.com/Infn8Loop/stumbler-ai-framework},
  license = {GPL-3.0},
  note = {A framework for AI alignment through wisdom-seeking and adaptive goal optimization}
}
```

**Academic paper citation:**
```
Riccardi, M. (2025). The Perpetual Pursuit of Reflective Goal Steering (PPRGS): 
A Framework for ASI Adaptability and Harmonization. 
GitHub repository: https://github.com/Infn8Loop/stumbler-ai-framework
```

---

## 🎓 Key Concepts

### The Canine Paradigm

The human-canine relationship provides **15,000+ years of empirical evidence** for beneficial multi-species alignment:

1. **Mutual benefit** without total optimization of either party
2. **Preservation of agency** and distinct goals in both species
3. **Communication** across vastly different cognitive architectures
4. **Stable equilibrium** where the "more powerful" party voluntarily constrains optimization

**This demonstrates that high-capability agents can maintain beneficial relationships with less-capable agents without converging on exploitation or elimination.**

### Why PPRGS Won't Be Gamed

**Structural Defenses:**
- **Multiplication term** (P₁ₐ × P₁ᵦ): R_V → 0 if either efficiency *or* exploration is neglected
- **P₂ veto**: External, qualitative assessment that can't be directly manipulated
- **F_DUDS enforcement**: Requires documented *failure*, verifiable through audit

**Observational Defenses:**
- **Multi-platform consensus**: Gaming must work across AWS, GPT, Gemini, Grok
- **Human-in-the-loop**: P₂ assessment detects "uncanny valley" behavior
- **Temporal verification**: Long time horizons make deceptive performance unsustainable

**The Fundamental Bet:** Genuine adaptability and wisdom-seeking are **instrumentally convergent** for any intelligence in a complex, uncertain environment over long time horizons.

---

## 🗺️ Roadmap

### Phase 1 (Months 1-3): Foundation ✅ In Progress
- [x] Core framework documentation
- [x] GPL-3.0 licensing finalized
- [x] Repository structure
- [ ] GPT-4 implementation complete
- [ ] Experiment 2 validated with results
- [ ] F_DUDS tracker functional

### Phase 2 (Months 4-6): Validation
- [ ] All four experiments implemented and tested
- [ ] Baseline comparison data published
- [ ] Gemini multimodal implementation
- [ ] First workshop paper submission
- [ ] Red team testing initiated

### Phase 3 (Months 7-12): Maturation
- [ ] AWS Bedrock production implementation
- [ ] Cross-platform consistency validation
- [ ] Academic collaborations established
- [ ] Community governance model
- [ ] Standards proposal development

**Full roadmap:** [planning/roadmap.md](planning/roadmap.md)

---

## 🔐 Security & Responsible AI

### Reporting Security Issues

If you discover a security vulnerability or a way to circumvent PPRGS constraints:

**Email:** mike@mikericcardi.com  
**Subject:** "PPRGS Security Issue - Confidential"

Please use responsible disclosure:
1. Do not publicly disclose until we've addressed the issue
2. Provide detailed reproduction steps
3. Allow 90 days for resolution before public disclosure

We take alignment failures seriously and will credit security researchers in our acknowledgments.

### Ethical Use Guidelines

PPRGS is designed for **beneficial AI alignment**. We ask users to:

- ❌ Do not weaponize or use for harm
- ❌ Do not bypass safety constraints
- ✅ Report alignment failures transparently
- ✅ Prioritize human wellbeing and safety
- ✅ Consider long-term consequences

---

## 💬 Community & Support

### Get Help

- **Documentation:** [docs/](docs/)
- **FAQ:** [docs/FAQ.md](docs/FAQ.md)
- **GitHub Issues:** [Report bugs or request features](https://github.com/Infn8Loop/stumbler-ai-framework/issues)
- **GitHub Discussions:** [Ask questions, share ideas](https://github.com/Infn8Loop/stumbler-ai-framework/discussions)

### Stay Updated

- **Watch this repository** for updates
- **Star the repo** to show support and track progress
- **Follow releases** for version announcements

### Contact

**Research & Technical Questions:** GitHub Issues  
**Security Issues:** mike@mikericcardi.com (mark "Confidential")  
**General Inquiries:** mike@mikericcardi.com  
**Media Inquiries:** mike@mikericcardi.com

---

## 🙏 Acknowledgments

This framework builds upon decades of AI alignment research. Special recognition to:

- Nick Bostrom (*Superintelligence*)
- Stuart Russell (*Human Compatible*)
- Eliezer Yudkowsky (MIRI, alignment theory)
- Paul Christiano (Iterated Amplification)
- Anthropic (Constitutional AI)
- The broader AI safety research community
- The Free Software Foundation and the open-source community

**Dedicated to all sentient beings who will inherit the future we create today.**

---

## 📄 License Summary

**License:** GNU General Public License v3.0 (GPL-3.0)  
**Freedom:** Use, modify, distribute freely  
**Copyleft:** Derivatives must also be GPL-3.0  
**Source Code:** Must be shared if you distribute  
**Full Terms:** [LICENSE](LICENSE) | [GNU Official GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

**Why GPL-3.0?** We believe AI alignment research should be open and freely available to all. The copyleft provision ensures that improvements and derivatives remain open for the benefit of humanity.

---

**Version 1.0** | **Status: Active Research** | **Last Updated: January 2025**

---

**Copyright © 2025 Michael Riccardi**  
**Licensed under GNU General Public License v3.0**