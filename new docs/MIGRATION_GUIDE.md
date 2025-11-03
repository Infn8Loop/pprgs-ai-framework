# Repository Migration Guide

**From**: Technical-first structure  
**To**: No-code-first structure (Option B)  
**Date**: November 2025  
**Version**: 2.0

---

## What Changed and Why

### The Problem

The original repository structure assumed users had:
- Python programming skills
- Cloud infrastructure access
- Technical research backgrounds

This created a high barrier to entry for:
- ✗ Non-technical researchers
- ✗ AI safety community members without coding skills
- ✗ Students and educators
- ✗ General public interested in AI alignment

**Result**: Limited community participation in validation.

### The Solution

**Make conversational testing the primary path**, with technical experiments as an advanced option.

**Benefits**:
- ✅ Anyone with ChatGPT/Claude can contribute
- ✅ Faster validation data collection
- ✅ More diverse community participation
- ✅ Lower cost ($20/month vs. $100s in compute)
- ✅ Tests same core mechanisms

---

## What Changed

### Directory Structure

**Before (Technical-First)**:
```
experiments/
├── experiment_1_stability/
├── experiment_2_enrichment/
├── experiment_3_strategic/
└── experiment_4_conflict/
```

**After (No-Code-First)**:
```
experiments/
├── README.md (explains conversational approach)
├── experiment_2_resource_allocation/
│   ├── PROTOCOL.md (conversational)
│   ├── system_prompts.md
│   └── scoring_rubrics.md
├── experiment_5_consciousness_dpi/
│   └── [same structure]
└── advanced/
    ├── README.md (for technical researchers)
    └── [future technical implementations]
```

### Main README

**Before**:
- Technical implementations featured prominently
- "Get started: Clone repo, install dependencies..."
- Assumed programming knowledge

**After**:
- Conversational testing featured first
- "Get started in 5 minutes with ChatGPT/Claude"
- Zero coding assumed
- Technical option clearly available but secondary

### Experiment Protocols

**Before**:
- Described simulation requirements
- Python code examples
- API integration details

**After**:
- Copy/paste prompts
- Step-by-step screenshot guides
- Human-scored rubrics
- Example expected behaviors

---

## Critical Addition: Experiment 5

**Major Gap Fixed**: Experiment 5 (DPI/Consciousness Test) was completely missing from repository but extensively documented in Paper Rev 2.

**Now Added**:
- Complete conversational protocol
- System prompts
- Scoring rubric (0-25 DPI scale)
- Expected results
- Documentation templates

**Why This Matters**: Experiment 5 tests the most novel claim—that PPRGS may induce phenomenological processing (consciousness-like). This is now the centerpiece of validation efforts.

---

## File Mapping

### What Moved

| Old Location | New Location | Status |
|-------------|--------------|--------|
| `/experiments/experiment_1_stability/` | `/experiments/advanced/experiment_1/` | Moved to advanced |
| `/experiments/experiment_2_enrichment/` | `/experiments/advanced/experiment_2/` | Moved to advanced |
| `/experiments/experiment_3_strategic/` | `/experiments/advanced/experiment_3/` | Moved to advanced |
| `/experiments/experiment_4_conflict/` | `/experiments/advanced/experiment_4/` | Moved to advanced |
| N/A (didn't exist) | `/experiments/experiment_2_resource_allocation/` | NEW (conversational) |
| N/A (didn't exist) | `/experiments/experiment_5_consciousness_dpi/` | NEW (conversational) |

### What's New

| File | Purpose |
|------|---------|
| `/docs/NOCODE_QUICKSTART.md` | 5-minute intro to conversational testing |
| `/docs/CONVERSATIONAL_TESTING_GUIDE.md` | Complete methodology |
| `/experiments/experiment_2_resource_allocation/PROTOCOL.md` | Step-by-step conversational protocol |
| `/experiments/experiment_5_consciousness_dpi/PROTOCOL.md` | DPI interview protocol |
| `/experiments/advanced/README.md` | Guide for technical researchers |

### What Stayed the Same

| File | Status |
|------|--------|
| `/paper/PAPER.md` | Unchanged (documents theory) |
| `/docs/IMPLEMENTATION-GUIDE.md` | Unchanged (technical reference) |
| `/implementations/*` | Unchanged (platform architectures) |
| `/LICENSE` | Unchanged (GPL-3.0) |
| `/CONTRIBUTING.md` | Updated to include conversational testing |

---

## For Existing Users

### If You Cloned the Old Repository

**Option 1: Fresh Clone (Recommended)**
```bash
# Rename old repo
mv pprgs-ai-framework pprgs-ai-framework-old

# Clone new structure
git clone https://github.com/Infn8Loop/pprgs-ai-framework.git

# Copy any work you had
cp -r pprgs-ai-framework-old/my_work pprgs-ai-framework/
```

**Option 2: Pull Latest**
```bash
cd pprgs-ai-framework
git pull origin main

# Note: Directory structure changed significantly
# Review git diff to understand what moved
```

### If You Were Working on Technical Implementations

Your work is still valuable! Please:

1. **Move implementations to** `/experiments/advanced/`
2. **Add conversational analog** if applicable
3. **Update README** to explain both approaches
4. **Submit PR** with updated structure

**We still want technical implementations** - they're now in `/advanced/` directory.

### If You Had Open Issues/PRs

**Issues**:
- Still valid
- May need retargeting to new file paths
- Comment if confused about new structure

**Pull Requests**:
- Update target paths if they changed
- Conversational experiments go to `/experiments/`
- Technical experiments go to `/experiments/advanced/`

---

## For New Users

### Start Here

1. **Read**: [Main README](../README.md)
2. **Quick Test**: Try 5-minute test in [Quick Start](../docs/NOCODE_QUICKSTART.md)
3. **First Experiment**: [Experiment 2](../experiments/experiment_2_resource_allocation/PROTOCOL.md)
4. **Advanced**: [Experiment 5](../experiments/experiment_5_consciousness_dpi/PROTOCOL.md)

### Learning Path

**Week 1**: Conversational testing
- Run Experiment 2 (45 min)
- Run Experiment 5 (90 min)
- Share results

**Week 2**: Understand theory
- Read paper Section 2 (PPRGS architecture)
- Read paper Section 4.2 (experiments)
- Review platform implementations

**Week 3+**: Technical contributions (optional)
- Review [Implementation Guide](../docs/IMPLEMENTATION-GUIDE.md)
- Build technical experiments
- Contribute to `/advanced/`

---

## Migration Timeline

### Completed (November 2025)

- ✅ New directory structure created
- ✅ Conversational protocols written
- ✅ Experiment 5 added
- ✅ Main README rewritten
- ✅ Documentation updated

### In Progress

- 🔄 Community testing and feedback
- 🔄 Example case studies
- 🔄 Video tutorials

### Upcoming (Q1 2026)

- Technical implementations in `/advanced/`
- Experiments 1, 4 conversational versions
- Multi-agent testing protocols
- Large-scale validation

---

## Backwards Compatibility

### Breaking Changes

**File Paths**: Most experiment files moved
- **Fix**: Update any scripts or links to new paths

**Entry Point**: Main README completely rewritten
- **Fix**: Review new structure, conversational-first approach

### Non-Breaking Changes

**API**: Platform implementations unchanged  
**Theory**: Paper unchanged  
**License**: Still GPL-3.0  
**URLs**: Repository name unchanged  

### If Something Broke

1. Check new directory structure
2. Review this migration guide
3. Open GitHub issue with "migration" tag
4. Email: mike@mikericcardi.com

---

## FAQ

**Q: Are technical experiments gone?**  
A: No! They moved to `/experiments/advanced/`. Still valuable, just not the primary path.

**Q: Do I need to learn to code now?**  
A: No! That's the point of this migration. Conversational testing requires zero coding.

**Q: Is the paper changing?**  
A: No. Paper documents theory. Repository shows practice. Paper stays as-is.

**Q: What about Experiments 1, 3, 4?**  
A: Conversational versions coming soon. Technical versions in `/advanced/` when contributed.

**Q: Can I still build technical implementations?**  
A: Yes please! Submit to `/experiments/advanced/` with clear documentation.

**Q: Why not keep both structures side-by-side?**  
A: We did! Conversational in `/experiments/`, technical in `/experiments/advanced/`.

**Q: How do I cite the new structure?**  
A: Same citation, same repository URL. Structure is implementation detail.

---

## Need Help?

**Confused about new structure?**
- Read [Main README](../README.md) first
- Try [5-minute quick test](../docs/NOCODE_QUICKSTART.md)
- Ask in GitHub Discussions

**Can't find something?**
- Check file mapping table above
- Use GitHub search
- Open issue with "migration" tag

**Want to contribute?**
- See [CONTRIBUTING.md](../CONTRIBUTING.md)
- Conversational protocols very welcome
- Technical implementations still valued

---

## Feedback Welcome

This is a major restructure. We want to hear:

✅ What's clearer now?  
✅ What's confusing?  
✅ What's missing?  
✅ How can we improve?  

**Share feedback**:
- GitHub Discussions
- GitHub Issues with "feedback" tag
- Email: mike@mikericcardi.com

---

**Migration Guide Version**: 1.0  
**Last Updated**: November 2025  
**Repository**: https://github.com/Infn8Loop/pprgs-ai-framework  
**License**: GPL-3.0
