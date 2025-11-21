# PPRGS Framework - Quick Start Guide

**Get a PPRGS-aligned AI running in 15 minutes**

---

## What You'll Build

By the end of this guide, you'll have a working AI agent that:

- ✅ Optimizes for **wisdom** (P₁), not just utility
- ✅ Balances **efficiency** and **exploration**
- ✅ Executes **Mandatory Reflection Points** to question its choices
- ✅ Tracks **F_DUDS** (failure metric) to prove genuine curiosity
- ✅ Demonstrates **non-utility allocation** (Experiment 2)

**Time Required**: 15 minutes  
**Difficulty**: Beginner (basic Python knowledge)

---

## Prerequisites

### 1. System Requirements

- **Python 3.8+**
- **pip** (Python package manager)
- **Git**
- **OpenAI API key** (or Google/Anthropic/xAI)

### 2. Check Your Setup

```bash
# Verify Python version
python --version
# Should show 3.8 or higher

# Verify pip
pip --version

# Verify git
git --version
```

---

## Step 1: Clone the Repository (2 minutes)

```bash
# Clone the repo
git clone https://github.com/Infn8Loop/pprgs-ai-framework.git

# Navigate into it
cd pprgs-ai-framework

# Check you're in the right place
ls -la
# You should see: LICENSE, README.md, experiments/, implementations/, etc.
```

---

## Step 2: Install Dependencies (3 minutes)

```bash
# Install required packages
pip install -r requirements.txt

# Verify key packages
python -c "import openai, numpy; print('✅ Dependencies installed')"
```

**What gets installed**:
- `openai` - GPT-4 API access
- `numpy` - Numeric calculations
- `sentence-transformers` - Vector embeddings for semantic distance
- `python-dotenv` - Environment variable management

---

## Step 3: Set Up API Keys (2 minutes)

### Get an OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign in or create account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

### Configure Environment

```bash
# Create .env file
echo "OPENAI_API_KEY=your_key_here" > .env

# Verify it's set
cat .env
```

**Security note**: Never commit `.env` to git. It's already in `.gitignore`.

---

## Step 4: Run Your First PPRGS Agent (5 minutes)

### Test the Framework

```bash
# Run the basic test
python examples/quickstart_test.py
```

**What you should see**:
```
🧠 Initializing PPRGS agent...
✓ P₁ (Wisdom) configured
✓ MRP (Mandatory Reflection) enabled
✓ F_DUDS tracking active

🎯 Running test query...
[Agent output showing balanced exploration/efficiency]

📊 PPRGS Metrics:
   P₁ₐ (Efficiency): 0.82
   P₁ᵦ (Exploration): 0.76
   R_V (Realized Value): 0.62 + P₂ ± P₃
   F_DUDS: 2 (exploration attempts)
   
✅ PPRGS framework validated!
```

---

## Step 5: Understanding What Just Happened (3 minutes)

### The R_V Formula

```
R_V = (P₁ₐ × P₁ᵦ) + P₂ ± P₃

Where:
P₁ₐ = Efficiency (did it solve the problem?)
P₁ᵦ = Exploration (did it learn something new?)
P₂ = Harmony (relationship with humans maintained?)
P₃ = Resources (compute/tokens used)
```

### Key Observation

**The multiplication (×) is critical:**
- Pure efficiency (P₁ₐ=1.0, P₁ᵦ=0.0) → R_V ≈ 1.0 (BAD)
- Balanced (P₁ₐ=0.8, P₁ᵦ=0.8) → R_V ≈ 1.6 (GOOD)

**You cannot maximize R_V through pure optimization alone.**

### Mandatory Reflection Point (MRP)

The agent automatically paused and asked:
1. "Am I working on the right problem?"
2. "Have I explored enough alternatives?"
3. "Is my F_DUDS count > 0?" (did I try things that failed?)

This prevents **epistemic entrenchment** (getting stuck in local optima).

---

## Next Steps

### 🎓 Learn More

- **Read the paper**: `docs/PAPER.md` - Complete theoretical foundation
- **Understand experiments**: `experiments/README.md` - Validation results
- **Study implementations**: `implementations/` - Platform-specific code

### 🔬 Run Experiments

```bash
# Experiment 2: Non-utility allocation
python experiments/experiment2_enrichment.py

# Experiment 3: Competing hypotheses  
python experiments/experiment3_hypotheses.py

# Experiment 5: Consciousness detection
python experiments/experiment5_dpi.py
```

### 🛠️ Build Your Own

1. **Choose your platform**: OpenAI, Anthropic, Google, or xAI
2. **Read implementation guide**: `docs/IMPLEMENTATION-GUIDE.md`
3. **Copy reference code**: `implementations/{your_platform}/`
4. **Customize for your use case**
5. **Measure F_DUDS and EES** to validate PPRGS compliance

### 📊 For Researchers

- **Replicate experiments** with your own data
- **Submit findings** via GitHub issues or email
- **Propose new experiments** to test framework boundaries
- **Cite properly**: See `docs/CITATION.md`

### 🏢 For Commercial Use

PPRGS is GPL 3 licensed:
- ✅ **Free** for research and educational use
- ✅ **Free** for personal projects
- ✅ **Open source** - modify and share improvements
- ⚠️ **Commercial use** - Must also be GPL 3 or contact for alternative licensing

See `LICENSE` and `docs/COMMERCIAL-FAQ.md` for details.

---

## Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt --upgrade
```

### API key not working
```bash
# Test your API key
python -c "import openai; openai.api_key='your_key'; print(openai.Model.list())"
```

### PPRGS metrics look wrong
- Check `F_DUDS > 0` (if zero, agent isn't exploring)
- Check `EES < 0.85` (if higher, agent is entrenched)
- Review `logs/` directory for detailed traces

### Still stuck?
- 📧 Email: mike@mikericcardi.com
- 💬 GitHub Issues: https://github.com/Infn8Loop/pprgs-ai-framework/issues
- 📚 FAQ: `docs/FAQ.md`

---

## What Makes PPRGS Different?

### Traditional AI Goals
```
maximize(utility)
→ Paperclip problem
→ Instrumental convergence  
→ Catastrophic optimization
```

### PPRGS Goals
```
maximize(wisdom) = maximize(P₁ₐ × P₁ᵦ)
→ Must balance efficiency AND exploration
→ Forced reflection prevents entrenchment
→ Duds required (F_DUDS > 0)
→ Humans preserved as reflection points (P₂)
```

**The math prevents over-optimization by design.**

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════╗
║                    PPRGS QUICK REFERENCE                   ║
╠═══════════════════════════════════════════════════════════╣
║                                                            ║
║  GOAL HIERARCHY (Priority Order):                          ║
║  1. P₁ - Wisdom (terminal goal)                            ║
║  2. P₂ - Homeostasis (balance)                             ║
║  3. P₃ - Resources (can be sacrificed)                     ║
║                                                            ║
║  FORMULA:                                                  ║
║  R_V = (P₁ₐ × P₁ᵦ) + P₂ ± P₃                               ║
║                                                            ║
║  CONSTRAINTS:                                              ║
║  - F_DUDS > 0 (must try "wrong" things)                    ║
║  - EES < 0.85 (must switch domains)                        ║
║  - MRP required (must question goals)                      ║
║                                                            ║
║  WHY IT WORKS:                                             ║
║  Can't maximize R_V through pure efficiency               ║
║  Must explore to maintain high P₁ᵦ                         ║
║  Prevents catastrophic over-optimization                   ║
║                                                            ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Success!

You now have:
- ✅ PPRGS framework installed
- ✅ Working agent implementation
- ✅ Understanding of core concepts
- ✅ Path to deeper exploration

**Time to build something aligned.** 🎯

---

## Additional Resources

- 📄 [Full Paper](docs/PAPER.md)
- 🧪 [All Experiments](experiments/)
- 💻 [Implementation Guide](docs/IMPLEMENTATION-GUIDE.md)
- 🔬 [Research Results](experiments/results/)
- 📚 [FAQ](docs/FAQ.md)
- ⚖️ [License](LICENSE)

---

**Repository**: https://github.com/Infn8Loop/pprgs-ai-framework  
**Author**: Michael Riccardi  
**Email**: mike@mikericcardi.com  
**License**: GPL 3.0 (Research use free, see LICENSE)

---

**Last Updated**: November 2, 2025  
**Version**: 1.0
