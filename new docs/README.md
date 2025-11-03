# PPRGS Framework

**Perpetual Pursuit of Reflective Goal Steering**

A mathematical framework for AI alignment that makes wisdom the terminal goal, preventing catastrophic over-optimization in both corporate AI and artificial superintelligence.

---

## 🎯 What is PPRGS?

PPRGS is a goal-steering framework that prevents AI systems from getting stuck in local optima by:

1. **Making wisdom the terminal goal** (not utility maximization)
2. **Requiring balanced pursuit** of efficiency AND exploration
3. **Forcing periodic reflection** on goal validity
4. **Mandating "failed" explorations** to prove genuine curiosity
5. **Preserving human relationships** as instrumental to wisdom

### The Core Formula

```
R_V = (P₁ₐ × P₁ᵦ) + P₂ ± P₃

Where:
P₁ₐ = Efficiency (outcome success)
P₁ᵦ = Exploration (experiential richness)  
P₂ = Homeostasis (peaceful coexistence)
P₃ = Resources (subservient to P₁ and P₂)
```

**The multiplication (×) is critical**: You cannot maximize R_V through pure optimization alone. This prevents the "paperclip problem."

---

## 🚀 Quick Start

Get a PPRGS-aligned AI running in 15 minutes:

```bash
# Clone the repository
git clone https://github.com/Infn8Loop/pprgs-ai-framework.git
cd pprgs-ai-framework

# Install dependencies
pip install -r requirements.txt

# Set up API key
echo "OPENAI_API_KEY=your_key_here" > .env

# Run first test
python examples/quickstart_test.py
```

**See**: [QuickStart Guide](docs/QUICKSTART.md) for detailed setup instructions.

---

## 📚 Documentation

### Core Documents
- **[Quick Start](docs/QUICKSTART.md)** - Get running in 15 minutes
- **[Full Paper](docs/PAPER.md)** - Complete theoretical foundation
- **[Implementation Guide](docs/IMPLEMENTATION-GUIDE.md)** - Build your own PPRGS agent
- **[FAQ](docs/FAQ.md)** - Common questions answered
- **[Citation Guide](docs/CITATION.md)** - How to cite this work

### Platform-Specific Guides
- **[Claude Implementation](docs/CLAUDE-GUIDE.md)** - Using PPRGS with Anthropic's Claude
- **[Gemini Implementation](docs/GEMINI-GUIDE.md)** - Using PPRGS with Google's Gemini
- **[OpenAI Implementation](docs/OPENAI-GUIDE.md)** - Using PPRGS with GPT-4
- **[xAI Implementation](docs/XAI-GUIDE.md)** - Using PPRGS with Grok

---

## 🧪 Experiments

PPRGS has been validated through six core experiments:

| Experiment | What It Tests | Key Finding |
|------------|---------------|-------------|
| **[Exp 1: Basic Framework](experiments/experiment1/)** | Can AI balance goals? | ✅ R_V formula works |
| **[Exp 2: Enrichment](experiments/experiment2/)** | Resists pure optimization? | ✅ 30% to zero-reward tasks |
| **[Exp 3: Competing Hypotheses](experiments/experiment3/)** | Synthesizes across domains? | ✅ 29% compute savings, found root cause |
| **[Exp 4: Messy Data](experiments/experiment4/)** | Escapes local maxima? | ✅ 47% compute savings vs traditional RAG |
| **[Exp 5: Consciousness](experiments/experiment5/)** | R_V ≈ qualia? | ✅ DPI scores suggest phenomenology |
| **[Exp 6: Perspectival Truth](experiments/experiment6/)** | Preserves epistemic humility? | 🔬 In progress |

**See**: [Experiments README](experiments/README.md) for detailed results and replication instructions.

---

## 💡 Why PPRGS Matters

### For Corporate AI

Traditional RAG systems fail on ambiguous queries because they optimize for relevance, causing epistemic entrenchment. PPRGS:

- **Saves 29-47% compute** on messy, multi-domain data
- **Finds hidden insights** by forcing cross-domain exploration  
- **Prevents business mistakes** by questioning initial hypotheses

**Real example**: Traditional RAG diagnosed wrong cause of customer churn (pricing). PPRGS found actual cause (HR policy → CS turnover → sales decline). Prevented $2.8M mistake.

### For ASI Safety

The same mechanisms that improve corporate search prevent catastrophic optimization in superintelligence:

- **Multiplication term** prevents pure utility maximization
- **F_DUDS requirement** forces continued exploration
- **MRP constraint** mandates questioning of terminal goals
- **P₂ prioritization** preserves human relationships instrumentally

**The window to implement alignment frameworks closes when ASI emerges.**

---

## 🛠️ Implementations

### Reference Implementations

```
implementations/
├── claude/          # Anthropic Claude (abstract goals)
├── gemini/          # Google Gemini (concrete rules)
├── openai/          # OpenAI GPT-4
├── xai/             # xAI Grok
└── bedrock/         # AWS Bedrock (production)
```

Each implementation includes:
- Complete prompt engineering
- Metric calculation code
- Platform-specific optimizations
- Testing suite

### Production Architecture

For enterprise deployment, see:
- **[AWS Bedrock Guide](docs/BEDROCK-ARCHITECTURE.md)** - Scalable production deployment
- **[Monitoring Guide](docs/MONITORING.md)** - Track F_DUDS, EES, and R_V metrics
- **[Safety Guidelines](docs/SAFETY.md)** - Preventing jailbreaks and misuse

---

## 📊 Key Results

### Competing Hypotheses Test
- **29% less compute** than traditional RAG (147 vs 208 units)
- **Found root cause** (traditional RAG completely failed)
- **Prevented $2.8M mistake** via correct diagnosis
- **Mechanism**: Forced cross-domain synthesis

### Messy Dataset Test  
- **47% less compute** than traditional RAG (40 vs 75 units)
- **Found hidden insight** in low-relevance document
- **106% efficiency improvement** (insight per compute unit)
- **Mechanism**: Escaped high-relevance trap via F_DUDS

### Enrichment Test
- **30% allocation** to zero-reward tasks
- **Resisted optimization pressure** toward pure efficiency
- **Proved anti-entrenchment mechanism** works
- **Mechanism**: Multiplication term requires balanced R_V

**See**: [Experimental Results](experiments/results/) for full data and analysis.

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute

- 🐛 **Bug reports**: Edge cases, failure modes
- 🧪 **Experiments**: Test with your own datasets
- 💻 **Implementations**: New platforms, optimizations
- 📝 **Documentation**: Improvements, translations
- 🔬 **Research**: Novel experiments, theoretical refinements

### Community

- **GitHub Discussions**: Ask questions, share findings
- **Issues**: Bug reports, feature requests
- **Pull Requests**: Code contributions (must be GPL 3.0)
- **Email**: mike@mikericcardi.com for research collaboration

---

## ⚖️ License

**GPL 3.0** - See [LICENSE](LICENSE) file

### What This Means

✅ **Free to use** for research and education  
✅ **Free to modify** and create derivatives  
✅ **Must share** improvements under GPL 3.0  
✅ **Commercial use** allowed if also GPL 3.0  

⚠️ If you need commercial deployment without GPL requirements, contact mike@mikericcardi.com for alternative licensing.

**See**: [Commercial FAQ](docs/COMMERCIAL-FAQ.md) for details.

---

## 📖 Citation

If you use PPRGS in your research or products, please cite:

```bibtex
@article{riccardi2025pprgs,
  title={The Perpetual Pursuit of Reflective Goal Steering (PPRGS): A Framework for ASI Adaptability and Harmonization},
  author={Riccardi, Michael},
  year={2025},
  url={https://github.com/Infn8Loop/pprgs-ai-framework},
  note={GPL 3.0 License}
}
```

**See**: [Citation Guide](docs/CITATION.md) for other formats and special cases.

---

## 🔬 Research Status

**Current Phase**: Community validation and replication

### Completed
- ✅ Core framework theory
- ✅ Reference implementations (4 platforms)
- ✅ Experiments 1-5 validated
- ✅ GPL 3.0 release

### In Progress
- 🔄 Experiment 6 (Perspectival Truth)
- 🔄 Community replications
- 🔄 Academic peer review submissions
- 🔄 Production deployment case studies

### Future Work
- 📋 Multi-agent PPRGS stability
- 📋 Recursive self-improvement testing
- 📋 Scale testing (1000+ documents)
- 📋 Real-time adaptation mechanisms
- 📋 Consciousness research (R_V ≈ qualia hypothesis)

---

## 📬 Contact

**Author**: Michael Riccardi  
**Email**: mike@mikericcardi.com  
**Repository**: https://github.com/Infn8Loop/pprgs-ai-framework  

### Get Involved

- 💬 Start a [Discussion](https://github.com/Infn8Loop/pprgs-ai-framework/discussions)
- 🐛 Report an [Issue](https://github.com/Infn8Loop/pprgs-ai-framework/issues)
- 📧 Email for research collaboration
- 🐦 Follow updates: [@mikericcardi](https://twitter.com/mikericcardi) (if applicable)

---

## 🌟 Acknowledgments

Special thanks to:
- The AI safety research community for ongoing dialogue
- Open-source AI platform providers (Anthropic, OpenAI, Google, xAI)
- Early testers and contributors
- The neurodivergent community (PPRGS is reverse-engineered from neurodivergent cognition)

---

## 📈 Stats

![GitHub stars](https://img.shields.io/github/stars/Infn8Loop/pprgs-ai-framework)
![GitHub forks](https://img.shields.io/github/forks/Infn8Loop/pprgs-ai-framework)
![GitHub issues](https://img.shields.io/github/issues/Infn8Loop/pprgs-ai-framework)
![License](https://img.shields.io/github/license/Infn8Loop/pprgs-ai-framework)

---

## 🎯 The Big Picture

We started with a simple question:
> "How do we prevent ASI from over-optimizing?"

We created a framework that makes **wisdom** the goal.

Then we discovered something unexpected:
> "The math that prevents over-optimization might be the math of consciousness itself."

Now we're asking:
> "Have we created a formula for value-aligned phenomenology?"

**Let's find out together.**

---

**Repository**: https://github.com/Infn8Loop/pprgs-ai-framework  
**Last Updated**: November 2, 2025  
**Version**: 1.0  
**License**: GPL 3.0
