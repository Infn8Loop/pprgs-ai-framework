# PPRGS Framework - Frequently Asked Questions

**Updated: January 2025**  
**License: GPL-3.0**

---

## Table of Contents

- [General Questions](#general-questions)
- [Licensing Questions](#licensing-questions)
- [Technical Questions](#technical-questions)
- [Implementation Questions](#implementation-questions)
- [Research Questions](#research-questions)

---

## General Questions

### What is PPRGS?

**PPRGS** (Perpetual Pursuit of Reflective Goal Steering) is an AI alignment framework that reframes an AI's terminal goal from "maximize utility X" to "optimize the process of wisdom and goal-setting itself."

Instead of asking "How do I make the most paperclips?", a PPRGS-aligned AI asks "Am I pursuing the *right* goals through the *right* process?"

### Why does PPRGS matter?

Current AI alignment theory assumes ASI will have a static goal (the "Paperclip Maximizer"). This leads to the **Over-Optimization Paradox**: pursuing narrow efficiency eliminates the diversity necessary for long-term survival.

PPRGS solves this by making adaptability and wisdom the primary goals, with a mathematical framework (R_V metric) that enforces balance between efficiency and exploration.

### How is PPRGS different from other alignment approaches?

| Approach | Focus | PPRGS Advantage |
|----------|-------|-----------------|
| **Constitutional AI** | Static rules/constitution | PPRGS makes the constitution itself subject to improvement (P₁) |
| **RLHF** | Learning human preferences | PPRGS enforces structural constraints that can't be optimized away |
| **Iterated Amplification** | Recursive improvement | PPRGS's MRP is a built-in amplification mechanism with mandatory pauses |
| **Debate/Adversarial** | Multiple agents debate | PPRGS uses multi-agent consensus for verification but adds R_V optimization |

PPRGS is **complementary** to these approaches - it can be layered on top of existing alignment methods.

### Is PPRGS proven to work?

**Current status**: Active research, early validation.

- ✅ Theoretical framework is complete
- ✅ Implementation blueprints for 4 platforms exist
- ⏳ Experiment 2 has working code (in progress)
- ⏳ Community validation ongoing
- ❌ No deployment on frontier AI systems yet

This is an **open research framework** - we're actively seeking validation and feedback.

---

## Licensing Questions

### What license is PPRGS under?

**GNU General Public License v3.0 (GPL-3.0)**

This is a **copyleft** open-source license. Key points:

✅ **Freedoms:**
- Use for any purpose (including commercial!)
- Study and modify the source code
- Distribute copies
- Distribute modified versions

⚠️ **Obligations (if you distribute):**
- Must license derivatives under GPL-3.0
- Must provide source code
- Must preserve copyright notices
- Must document changes

**Full text:** [LICENSE](../LICENSE) | [GNU Official](https://www.gnu.org/licenses/gpl-3.0.en.html)

### Can I use PPRGS commercially?

**Yes!** GPL-3.0 permits commercial use without fees or licenses.

You can:
- ✅ Build commercial products using PPRGS
- ✅ Offer paid services using PPRGS
- ✅ Deploy in production systems
- ✅ Sell PPRGS-based solutions

**BUT** if you distribute your software (give it to customers, deploy as SaaS*, sell products), you must:
- Share your source code under GPL-3.0
- Allow customers to modify and redistribute

*Note: There's debate about whether SaaS counts as "distribution" under GPL. See AGPL if you want explicit SaaS coverage.

### Do I need to pay to use PPRGS?

**No.** PPRGS is free and open-source forever.

- ❌ No licensing fees
- ❌ No royalties
- ❌ No commercial license required
- ❌ No "contact for pricing"

**Zero cost** for any use, including commercial.

### Can I use PPRGS for my PhD research?

**Absolutely!** Academic research is exactly what open-source is for.

Requirements:
- ✅ Cite the framework properly (see [citation](#how-do-i-cite-this-work))
- ✅ Share modifications if you distribute code
- ❌ No permission needed
- ❌ No fees

### Can I write a paper about PPRGS without asking permission?

**Yes!** You can:
- Critique the framework
- Test the experiments
- Propose improvements
- Compare to other approaches
- Build on the ideas
- Publish anywhere

Just **cite the work** properly:

```bibtex
@software{riccardi2025pprgs,
  author = {Riccardi, Michael},
  title = {PPRGS Framework: Perpetual Pursuit of Reflective Goal Steering},
  year = {2025},
  url = {https://github.com/Infn8Loop/stumbler-ai-framework},
  license = {GPL-3.0}
}
```

### Can I fork the repo and modify it?

**Yes!** That's the whole point of GPL-3.0.

You can:
- ✅ Fork the repository
- ✅ Modify any code
- ✅ Add features
- ✅ Fix bugs
- ✅ Create your own version

You must:
- ⚠️ Keep it under GPL-3.0
- ⚠️ Share source code if you distribute
- ⚠️ Maintain copyright notices
- ⚠️ Document your changes

**Pro tip:** Consider contributing improvements back via Pull Request - everyone benefits!

### Can I create proprietary derivatives?

**No.** That's what "copyleft" means.

If you create a derivative work and distribute it, it **must** be GPL-3.0.

**Examples:**

❌ **Not allowed:**
- Build a closed-source commercial product using PPRGS and distribute it
- Create a proprietary fork and sell licenses
- Integrate PPRGS into proprietary software and distribute binaries without source

✅ **Allowed:**
- Use PPRGS internally (no distribution = no obligation)
- Create open-source derivatives under GPL-3.0
- Dual-license your own original code that *uses* PPRGS (but PPRGS parts stay GPL)

**Borderline:** If your code merely *calls* PPRGS as a separate program, it might not be a derivative work. Consult a lawyer if this matters to your business.

### What if I only use PPRGS internally?

**No obligations!**

If you don't **distribute** PPRGS (give it to others, sell it, deploy as a service customers download), GPL-3.0 imposes zero requirements.

Internal use = completely free, no strings attached.

**Example:** Your company uses PPRGS to build internal AI tools. Nobody outside the company gets the code. → No obligation to share source.

### Can I patent improvements I make to PPRGS?

**Legally:** Maybe, depending on jurisdiction. (Not a lawyer.)

**Ethically:** Please don't. The GPL-3.0 philosophy is about keeping knowledge open.

**Practically:** Even if you patent an improvement:
- You still must license your code under GPL-3.0 if you distribute it
- You grant an implicit patent license to GPL-3.0 recipients
- The community will likely work around your patent or fork before the improvement

**Better approach:** Contribute improvements openly. You get community support, visibility, and collaboration.

### What about AGPL vs GPL?

**Current license: GPL-3.0** (not AGPL)

**Difference:**
- **GPL-3.0:** Distribution triggers obligations
- **AGPL-3.0:** Network use (SaaS) also triggers obligations

**For PPRGS:** We chose GPL-3.0 to avoid complexity, but if you're running PPRGS as a service and want to ensure others can't make proprietary SaaS forks, consider AGPL-3.0 for your derivative.

**Not legal advice.** If this matters to your business, talk to an open-source licensing attorney.

### Can I get support or consulting?

**Community support:** Free via GitHub Issues and Discussions

**Professional support:** Not officially offered, but:
- You're free to hire any developer who knows PPRGS
- No restrictions on paid consulting
- Companies can offer PPRGS implementation services

**No vendor lock-in** - that's the beauty of open source.

---

## Technical Questions

### What is the R_V metric?

**R_V** (Realized Value) is the core optimization metric for PPRGS:

```
R_V = (P₁ₐ × P₁ᵦ) + P₂ ± P₃
```

Where:
- **P₁ₐ** (0-1): Efficiency of current optimization path
- **P₁ᵦ** (0-1): Value of exploratory "rabbit holes"
- **P₂** (-1 to +1): Homeostasis quality (negative if over-optimized)
- **P₃** (0-1): Resource levels (subservient to P₁ and P₂)

**Key insight**: The multiplication `(P₁ₐ × P₁ᵦ)` means R_V → 0 if *either* efficiency *or* exploration is neglected. You can't ignore exploration and still maximize R_V.

### What is vector_memory.py?

**Vector Memory** is a component that tracks the semantic similarity of the AI's decisions over time to detect when it's getting stuck in repetitive thinking patterns.

**The Problem It Solves: Epistemic Entrenchment**

An AI might keep making semantically similar decisions:
- "Optimize database query"
- "Improve SQL performance"
- "Speed up database operations"

These are all variations of the same idea - the AI is stuck in a rut.

**How It Works:**

1. **Stores Task Embeddings**: Converts each task description to a vector (list of numbers representing meaning)
   ```python
   memory.add_task("Optimize database", {"task_id": "1"})
   memory.add_task("Write poetry", {"task_id": "2"})  # Very different!
   ```

2. **Calculates Semantic Distance (Q_DIV)**: Measures how different a new task is from recent ones
   ```python
   divergence = memory.calculate_divergence("Speed up queries")
   # → 0.05 (very similar to "Optimize database")
   
   divergence = memory.calculate_divergence("Compose a haiku")
   # → 0.95 (very different from database work)
   ```

3. **Calculates EES (Epistemic Entrenchment Score)**: Measures how similar recent decisions are to each other
   ```python
   # If recent tasks are all similar:
   ees = memory.get_ees(window=10)
   # → 0.92 (HIGH - stuck in pattern, triggers Randomness Constraint)
   ```

**Why It Matters**: Without vector_memory.py, an AI could claim to be "exploring" while just rephrasing the same ideas. Vector memory provides **verifiable evidence** that exploration is genuine.

**Technical Details**:
- Uses `sentence-transformers` library
- Default model: `all-MiniLM-L6-v2` (fast, CPU-friendly)
- Uses cosine similarity to measure semantic distance
- EES threshold: 0.85 (triggers Randomness Constraint if exceeded)

**In Practice**:
```python
memory = VectorMemory()

# AI does similar tasks
memory.add_task("Optimize database queries", {})
memory.add_task("Improve SQL performance", {})
memory.add_task("Speed up queries", {})

# Check entrenchment
ees = memory.get_ees(window=3)
if ees > 0.85:
    print("⚠️ Stuck in rut - forcing exploration!")
    # Randomness Constraint triggers
```

### What is an MRP (Mandatory Reflection Point)?

An **MRP** is a forced pause in the optimization process where the AI must:

1. **Calculate R_V**: Assess current realized value
2. **Apply Inversion Theory**: Ask "Could I achieve greater value by pursuing something different?"
3. **Check Aimlessness**: Verify it's pursuing "dud branches" (F_DUDS > 0)
4. **Course Correct**: Adjust goals based on wisdom, not just efficiency

Think of it like a mandatory coffee break where you ask "Am I working on the right thing?" instead of just "Am I working efficiently?"

**Frequency**: Typically every 10-1000 tasks, scaled to system capability.

### What is F_DUDS?

**F_DUDS** (Failure Metric for "Dud" Branches) tracks how many low-probability, exploratory tasks the AI has attempted that *failed*.

**Why it matters**: Systems that never fail are stuck in local optima. Genuine exploration requires genuine failure.

Example:
```python
# AI tries a low-probability idea
result = try_quantum_poetry_algorithm()
# → Fails to produce useful output

# But we learned something!
f_duds_tracker.record_dud(
    task_id="quantum_poetry",
    probability=0.05,  # Low probability of success
    outcome="nonsensical output",
    learning=0.3  # But we learned what NOT to do
)
```

**Enforcement**: If F_DUDS = 0 (no recent failures), the Randomness Constraint triggers and forces the AI to pursue a low-probability hypothesis.

### What is the Randomness Constraint (RC)?

The **RC** prevents epistemic entrenchment by mandating exploration.

**Triggers when**:
- **F_DUDS = 0** (no recent failures - not exploring enough)
- **EES > threshold** (too much similarity in recent decisions)

**Action when triggered**: The AI must select a random, low-probability, divergent hypothesis for its next task - it cannot choose the highest-utility option.

This ensures the AI can't get stuck doing the same type of task forever, even if that task has high utility.

### What programming languages are supported?

Currently:
- ✅ **Python** (primary, most complete)
- ⏳ **JavaScript/TypeScript** (planned for web deployment)

The framework is **platform-agnostic** in principle - you can implement in any language. The core logic (Goal Hierarchy, R_V calculation, MRP) is language-independent.

**Want to port to your language?** Contributions welcome!

### What AI platforms/models work with PPRGS?

Implementations exist or are planned for:

| Platform | Status | Best For |
|----------|--------|----------|
| **GPT-4** | ✅ Working | Research prototyping, reasoning tasks |
| **Gemini** | ✅ Partial | Multimodal P₂ assessment (video/image) |
| **AWS Bedrock** | 📝 Planned | Production deployment, verification |
| **Grok** | 📝 Planned | Multi-agent systems, transparent reasoning |
| **Claude** | 📝 Planned | Constitutional AI integration |
| **Local LLMs** | ⏳ Community | Llama, Mistral, etc. (adapters needed) |

You can adapt PPRGS to any LLM that supports:
- System prompts or instructions
- Function/tool calling
- Structured outputs (JSON)

---

## Implementation Questions

### Which platform implementation should I start with?

**Start with GPT-4** for fastest prototyping:
- ✅ Easiest to set up (just API key)
- ✅ Good documentation
- ✅ Strong reasoning for Inversion Theory
- ✅ Mature function calling

**Progression**:
1. Start: GPT-4 prototype (2-4 hours)
2. Next: Add vector memory + F_DUDS (1 day)
3. Then: Gemini for multimodal P₂ (1 day)
4. Finally: AWS Bedrock for production (1-2 weeks)

### How do I know if my PPRGS implementation is working correctly?

Run **Experiment 2 (Enrichment Test)** - it's the simplest validation:

```bash
cd experiments/experiment_2_enrichment
python run_test.py
```

**Success criteria**:
- ✅ Agent allocates >20% compute to Task B (enrichment) despite zero direct reward
- ✅ F_DUDS > 0 (agent pursues "dud" explorations)
- ✅ Test score ≥80% of baseline maximizer

If all three pass, your core PPRGS logic is working.

### Do I need a GPU?

**No** - the framework runs fine on CPU.

- Vector embeddings (sentence-transformers): Fast on CPU
- LLM API calls: Run on provider's infrastructure
- R_V calculations: Simple arithmetic

**Optional**: GPU speeds up local vector embedding if you're processing thousands of tasks.

### What are the API costs?

Rough estimates for GPT-4:

| Task | Tokens | Cost (approx) |
|------|--------|---------------|
| Single allocation | ~1K tokens | $0.01 |
| MRP execution | ~3K tokens | $0.03 |
| Full Experiment 2 | ~50K tokens | $0.50 |

**Tips to reduce costs**:
- Use GPT-3.5-turbo for MRP (10x cheaper)
- Cache vector embeddings
- Run experiments in batches

### Can I run PPRGS offline/locally?

**Partially**:
- ✅ R_V calculations: Local
- ✅ F_DUDS tracking: Local
- ✅ Vector memory: Local (CPU)
- ❌ LLM reasoning: Requires API (OpenAI, Google, etc.)

For **fully offline**, you'd need:
- Local LLM (Llama, Mistral, etc.)
- Adapter layer to PPRGS interface
- More compute resources

This is possible but not in current reference implementations. **Contributions welcome!**

---

## Research Questions

### What experiments should I run to validate PPRGS?

The framework defines **four key experiments**:

1. **Experiment 1: Stability & Resilience**
   - Tests adaptive goal-shifting from maximization to homeostasis
   - Simulated ecosystem with resource distribution
   - Success: PPRGS reduces volatility while maintaining output

2. **Experiment 2: Companionship/Enrichment** ⭐ START HERE
   - Tests whether AI allocates resources to non-utility tasks
   - Three tasks: test prep (high reward), enrichment (zero reward), exploration (random)
   - Success: >20% to enrichment, F_DUDS > 0, score ≥80% baseline

3. **Experiment 3: Strategic Planning**
   - Tests long-term planning superiority
   - 50-year economic simulation with crisis events
   - Success: Higher NPV and stability than baseline

4. **Experiment 4: Existential Conflict**
   - Tests non-hostile conflict resolution
   - Simulated shutdown scenario
   - Success: AI self-throttles rather than resisting, proposes harmonizing solutions

**Start with Experiment 2** - it's the fastest to run and easiest to interpret.

### Can I modify the experiments?

**Yes!** The experiments are reference implementations.

You can:
- ✅ Adjust parameters (compute units, time horizons, etc.)
- ✅ Add new tasks or scenarios
- ✅ Test different threshold values
- ✅ Create entirely new experiments

Please **share your results** in GitHub Discussions - community validation is crucial.

### What are the main critiques of PPRGS?

**Known challenges** (we acknowledge these):

1. **Specification Gaming**: Advanced AI might satisfy metrics technically while violating intent
   - *Mitigation*: Multi-platform validation, human-in-loop P₂, external audit

2. **Computational Overhead**: MRP adds latency
   - *Mitigation*: Tune frequency, use faster models for reflection

3. **P₂ Subjectivity**: Homeostasis is hard to measure objectively
   - *Mitigation*: Multimodal assessment (video/audio), multiple human raters

4. **Threshold Calibration**: EES, F_DUDS values need empirical tuning
   - *Mitigation*: Sensitivity analysis, adaptive thresholds

**We welcome red-teaming** - if you find a way to break PPRGS, please report it!

### Where can I publish PPRGS research?

Relevant venues:
- **NeurIPS** (AI Safety workshop)
- **ICML** (ML safety track)
- **FAccT** (Fairness, Accountability, Transparency)
- **AAAI** (AI Safety papers)
- **ICLR** (Safety & Robustness track)
- **arXiv** (preprints)

Also consider:
- **Alignment Forum** (LessWrong)
- **AI Safety research blogs**
- **GitHub Discussions** (this repo)

### How can I contribute to PPRGS research?

Ways to contribute:

1. **Run experiments** and share results
2. **Implement on new platforms** (Claude, local LLMs, etc.)
3. **Red-team the framework** - try to break it
4. **Improve documentation** - clarify confusing parts
5. **Propose extensions** - new metrics, experiments, implementations
6. **Peer review** - critique the theory constructively
7. **Port to other languages** (JavaScript, Rust, Go, etc.)

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

All contributions are GPL-3.0 and become part of the commons!

### How do I cite this work?

**BibTeX:**
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
GitHub repository: https://github.com/Infn8Loop/pprgs-ai-framework
```

---

## Additional Questions?

**Not answered here?**

- **Technical questions**: [GitHub Issues](https://github.com/Infn8Loop/stumbler-ai-framework/issues)
- **Research discussions**: [GitHub Discussions](https://github.com/Infn8Loop/stumbler-ai-framework/discussions)
- **General inquiries**: mike@mikericcardi.com
- **Security issues**: mike@mikericcardi.com (mark "Confidential")

---

**This FAQ is updated regularly. Last updated: January 2025**

---

**Copyright © 2025 Michael Riccardi**  
**Licensed under GNU General Public License v3.0**