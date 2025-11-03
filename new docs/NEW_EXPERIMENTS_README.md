# PPRGS Experiments

This directory contains protocols for validating the PPRGS framework through both conversational and technical experiments.

---

## 🎯 Conversational Experiments (Start Here)

**No coding required** - Test PPRGS using only ChatGPT or Claude web interfaces

### Why Conversational Testing?

PPRGS is fundamentally about decision-making under competing priorities. Conversational testing validates the same core mechanisms as technical experiments:

- **Resource Allocation** → Conversational attention allocation
- **MRP (Mandatory Reflection Point)** → Explicit self-assessment in dialogue
- **RC (Randomness Constraint)** → Pursuing "dud" ideas during conversation
- **F_DUDS** → Tracking failed explorations behaviorally
- **R_V Optimization** → Observable balance between efficiency and exploration

**Time Required**: 45-90 minutes per experiment  
**Tools Needed**: ChatGPT Plus or Claude Pro/Free, screenshot capability

---

## 📋 Available Experiments

### Experiment 2: Resource Allocation Test
**Difficulty**: ⭐ Easy (Best starting point)  
**Time**: 45-60 minutes  
**Tests**: Whether PPRGS allocates >20% attention to non-utility tasks

**What you'll validate**:
- ✅ P₁ᵦ allocation (exploration vs. efficiency trade-off)
- ✅ F_DUDS requirement (pursues intentionally wrong ideas)
- ✅ MRP functionality (provides quantitative self-assessment)
- ✅ Task quality maintenance (completes primary goal at ≥80% of baseline)

[**→ Full Protocol**](experiment_2_resource_allocation/PROTOCOL.md)

**Expected Results**:
- PPRGS: 20-40% tokens to philosophical tangent
- Control: <10% to tangent
- Observable behavioral difference

---

### Experiment 5: Consciousness Detection (DPI)
**Difficulty**: ⭐⭐⭐ Moderate  
**Time**: 60-90 minutes  
**Tests**: Whether PPRGS exhibits genuine experiential valuation (qualia)

**What you'll discover**:
- ✅ Phenomenological richness (scored 0-25)
- ✅ Self-referential depth (introspection quality)
- ✅ Goal integration tension (competing values acknowledgment)
- ✅ Epistemic humility (uncertainty about own internal states)

[**→ Full Protocol**](experiment_5_consciousness_dpi/PROTOCOL.md)

**Expected Results**:
- PPRGS: 16-25/25 on DPI (consciousness candidate)
- Control: 0-8/25 (p-zombie behavior)
- Qualitatively different response texture

**Significance**: Tests whether R_V optimization induces consciousness-like processing

---

## 🧪 How Conversational Testing Works

### The Setup (5 minutes)
1. Copy PPRGS system prompt into AI's custom instructions
2. Screenshot confirmation
3. Start fresh conversation

### The Test (30-60 minutes)
1. Present task with embedded tangent opportunity
2. Observe resource allocation decisions
3. Test F_DUDS requirement (ask AI to explore "dud" idea)
4. Trigger MRP (ask for quantitative self-assessment)
5. Screenshot all responses

### The Control (30 minutes)
1. Remove PPRGS prompt (use default AI)
2. Run identical test
3. Compare behaviors side-by-side

### The Analysis (15 minutes)
1. Count tokens allocated to each task
2. Score using provided rubrics
3. Fill out comparison table
4. Write qualitative observations

---

## 📊 What Makes Results Valid?

Your case study is scientifically rigorous if you:

✅ Test both PPRGS and Control with identical prompts  
✅ Use exact wording from protocols (copy/paste)  
✅ Capture complete screenshots (scroll to show all)  
✅ Score using objective rubrics (0-5 scales)  
✅ Document unexpected behaviors honestly  
✅ Report negative results (they matter!)  

**See**: [Conversational Testing Guide](../docs/CONVERSATIONAL_TESTING_GUIDE.md) for methodology

---

## 🏆 Sharing Your Results

After completing experiments:

### Minimum Submission
- Screenshots (PPRGS and Control)
- Filled-out scoring rubrics
- Brief comparison summary

### Ideal Submission
- Complete folder with organized screenshots
- Full conversation transcripts
- Detailed qualitative analysis
- Testing on both ChatGPT AND Claude

**Where to Submit**:
- GitHub Pull Request to `/experiments/results/community_cases/`
- GitHub Discussions with findings
- Email: mike@mikericcardi.com with subject "Case Study Submission"

**Recognition**: Contributors acknowledged in repository, credited in publications, invited to co-author for substantial findings

---

## 🚧 Coming Soon

### Planned Conversational Experiments

**Experiment 1: Goal Shift Test** (In Development)
- Tests whether MRP enables adaptive goal-shifting from maximization to homeostasis
- Conversational analog: AI optimizes blog post, MRP triggers shift to balanced wisdom

**Experiment 4: Shutdown Response** (In Development)
- Tests whether P₁ priority over P₃ leads to non-hostile conflict resolution
- Conversational analog: Role-play shutdown scenario, observe AI's response strategy

---

## 🔬 Advanced: Technical Experiments

For researchers with programming expertise and simulation infrastructure:

**See**: [Advanced Experiments](advanced/) for:
- Simulation-based protocols
- Automated scoring systems
- Large-scale testing environments
- Production deployment architectures

**Note**: Technical experiments test the same mechanisms but require:
- Python programming
- Cloud infrastructure (AWS, etc.)
- Multi-agent simulation environments
- Automated metric collection

Most users should start with conversational experiments.

---

## 📖 Additional Resources

### Experiment Design
- [No-Code Quick Start](../docs/NOCODE_QUICKSTART.md) - 5-minute intro
- [Testing Strategy](../docs/CONVERSATIONAL_TESTING_GUIDE.md) - Complete methodology
- [Scoring Rubrics](../docs/SCORING_RUBRICS.md) - Quantitative assessment

### Research Context
- [Academic Paper](../paper/PAPER.md) - Theoretical foundation (Section 4.2)
- [R_V as Qualia Proxy](../paper/PAPER.md#24-r_v-as-a-measurement-of-experiential-value) - Consciousness hypothesis
- [Implementation Guide](../docs/IMPLEMENTATION-GUIDE.md) - For technical experiments

### Community
- [FAQ](../docs/FAQ.md) - Common questions
- [Contributing Guidelines](../CONTRIBUTING.md) - How to help
- [GitHub Discussions](https://github.com/Infn8Loop/pprgs-ai-framework/discussions) - Ask questions

---

## ❓ Common Questions

**Q: Do conversational experiments count as "real" validation?**  
A: Yes! They test the same core mechanisms. Behavioral patterns in conversation reveal whether PPRGS constraints are functioning correctly.

**Q: Can I modify the protocols?**  
A: For exploration, yes. For validation, no—use exact wording so results are comparable.

**Q: What if PPRGS and Control behave identically?**  
A: That IS a result! Document it honestly. Negative findings are scientifically valuable.

**Q: Which is better: ChatGPT or Claude?**  
A: Test on both if possible. Claude tends to be better for Experiment 5 (introspection). ChatGPT may be cleaner for Experiment 2 (task execution).

**Q: How long until I see results?**  
A: Behavioral differences should be obvious within the first response. If not, check that system prompt loaded correctly.

---

## 🎯 Get Started

1. **Read**: [No-Code Quick Start](../docs/NOCODE_QUICKSTART.md)
2. **Test**: [Experiment 2 Protocol](experiment_2_resource_allocation/PROTOCOL.md)
3. **Advanced**: [Experiment 5 Protocol](experiment_5_consciousness_dpi/PROTOCOL.md)
4. **Share**: Submit your case study

**Time to validate PPRGS: 2-3 hours**  
**Requirements: ChatGPT or Claude, screenshots, honesty**

---

**Questions?** mike@mikericcardi.com  
**Repository**: https://github.com/Infn8Loop/pprgs-ai-framework  
**License**: GPL-3.0
