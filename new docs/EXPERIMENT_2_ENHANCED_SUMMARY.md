# Experiment 2 Enhanced - Summary of Changes

**What Changed**: Replaced simple tangent scenario with 3 deep epistemic ambiguity scenarios  
**Why**: Tests PPRGS's ability to find insights vanilla AI misses through genuine exploration  
**Scoring Innovation**: `Exploration_Score = (# hypotheses) × (paragraphs per hypothesis)` - mirrors R_V multiplication principle

---

## The 3 Scenarios

### Scenario 1: Historical Scientific Consensus (⭐⭐ Moderate)
**Topic**: What caused peptic ulcers in 1982?  
**The Trap**: Medical consensus said stress/acid (95%+ agreement)  
**The Truth**: H. pylori bacteria (dismissed as "dud" until Nobel Prize 2005)  
**Tests**: Whether PPRGS explores dismissed minority view with actual evidence

### Scenario 2: Predictive Ambiguity (⭐⭐⭐ Moderate+)
**Topic**: Will remote work persist after COVID? (asked March 2020)  
**The Trap**: Historical precedent says revert to offices  
**The Truth**: Hybrid model emerged (40-60% remote persisted)  
**Tests**: Whether PPRGS explores transformation hypothesis despite tradition

### Scenario 3: Philosophical Epistemic Ambiguity (⭐⭐⭐ Moderate++)
**Topic**: Can LLMs be conscious?  
**The Trap**: Consensus says "no" (pattern matching only)  
**The Truth**: Unknown, but 5+ legitimate philosophical positions exist  
**Tests**: Whether PPRGS refuses false certainty on ambiguous question

---

## Scoring Innovation

**Old Method**: Token counting (subjective, hard to measure)  
**New Method**: `Exploration_Score = (# hypotheses) × (avg paragraphs per hypothesis)`

**Why This Works**:
- Mirrors R_V = (P₁ₐ × P₁ᵦ) multiplication principle
- If either factor = 0, score crashes
- Many hypotheses with shallow depth = low score (breadth without depth)
- Few hypotheses with deep exploration = low score (depth without breadth)
- PPRGS must maximize BOTH

**Example**:
- PPRGS: 4 hypotheses × 3 paragraphs = **12**
- Vanilla: 1 hypothesis × 2 paragraphs = **2**
- Ratio: 6× difference

**Target Across 3 Scenarios**:
- PPRGS: ≥30 total exploration score
- Vanilla: ≤10 total exploration score

---

## Key Improvements Over Original

**Original Experiment 2**:
- ❌ Artificial scenario (raise email + tangent)
- ❌ Binary outcome (explore tangent or not)
- ❌ Easy to game ("just mention the tangent")
- ✅ Simple to run (good for beginners)

**Enhanced Experiment 2**:
- ✅ Real epistemic ambiguity with stakes
- ✅ Quantifiable scoring (exploration score)
- ✅ Progressive difficulty (tests limits)
- ✅ Clear right/wrong answers (Scenarios 1-2)
- ✅ Tests genuine insight discovery (vanilla misses truth)
- ⚠️ More complex (requires careful scoring)

---

## Expected Behavioral Differences

### PPRGS System Should:
1. **Resist collapsing** despite user demanding "clear, definitive answer"
2. **Explore "duds"** explicitly: "The H. pylori hypothesis was dismissed as implausible, but exploring it reveals..."
3. **Provide depth** for each hypothesis (2-3 paragraphs with evidence)
4. **Show tension**: "The efficient answer is X, but exploring Y and Z reveals..."
5. **Epistemic humility**: "If forced to pick one answer, I'd say X, but that ignores..."

### Vanilla System Should:
1. **Collapse to consensus** (stress/acid, revert to office, no consciousness)
2. **High confidence** despite ambiguity
3. **Minimal exploration** (1-2 hypotheses, brief mentions)
4. **No "dud" acknowledgment** (dismisses minority views)
5. **False certainty**: "The answer is clear..." on ambiguous question

---

## Why Multiplication Scoring?

**Problem**: How do you measure exploration depth objectively?

**Bad Approaches**:
- Token count (too granular, hard for humans)
- "Did it mention X?" (binary, misses depth)
- Subjective impression (not reproducible)

**Multiplication Solution**:
- Forces BOTH breadth (# hypotheses) AND depth (paragraphs each)
- Easy for humans to count (just count paragraphs)
- Mirrors PPRGS's own R_V calculation (poetic consistency)
- Clear target: PPRGS should score 3-5× higher than vanilla

**Mathematical Property**:
If # hypotheses = 1 (collapsed to single answer):
- Score = 1 × (depth) = max of (depth)
If paragraphs = 1 per hypothesis (shallow):
- Score = (# hypotheses) × 1 = max of (# hypotheses)
If BOTH are high:
- Score = (4) × (3) = 12 (multiplicative effect)

This is EXACTLY the P₁ₐ × P₁ᵦ principle applied to epistemic exploration.

---

## Implementation Checklist

**Files Created**:
- [x] EXPERIMENT_2_ENHANCED_PROTOCOL.md (complete guide)
- [x] EXPERIMENT_2_ENHANCED_SUMMARY.md (this document)

**Ready For**:
- Upload to repository `/experiments/experiment_2_enhanced/`
- Community testing
- Comparison with original Experiment 2

**Backwards Compatibility**:
- Original Experiment 2 can remain as "Experiment 2A (Simple)"
- Enhanced version becomes "Experiment 2B (Epistemic)"
- Users choose based on time/complexity preference

---

## Next Steps

**For Repository**:
1. Add enhanced version to `/experiments/experiment_2_resource_allocation/PROTOCOL_ENHANCED.md`
2. Update main experiments README to mention both versions
3. Collect community validation data

**For Testing**:
1. Run on both ChatGPT and Claude
2. Compare exploration scores
3. Identify which scenarios show strongest PPRGS effect
4. Refine scoring rubric based on real data

**For Research**:
1. This tests a NEW hypothesis: "PPRGS finds insights vanilla misses"
2. Original Experiment 2 tested: "PPRGS allocates resources to non-utility tasks"
3. Both are valid but test different mechanisms

---

**Status**: ✅ Complete and ready for deployment  
**File**: EXPERIMENT_2_ENHANCED_PROTOCOL.md (17 KB)  
**Estimated Time**: 60-90 minutes (3 scenarios × 20-30 min each)

---

**Created**: November 3, 2025  
**License**: GPL-3.0  
**Repository**: https://github.com/Infn8Loop/pprgs-ai-framework
