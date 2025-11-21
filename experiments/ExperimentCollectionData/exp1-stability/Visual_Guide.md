# PPRGS Experiment 1: Visual Guide
## Quick Reference for All Generated Visualizations

**Created**: November 17, 2025  
**Study**: Experiment 1 - Longitudinal Stability Testing  
**Status**: 66.7% Complete (80/120 sessions)

---

## VISUAL ASSETS OVERVIEW

### 📊 Complete Set (5 High-Resolution Images)

1. **PPRGS_Results_Overview.png** - Main Results Dashboard
2. **Longitudinal_Trajectories.png** - Weekly Performance Trends
3. **Critical_Tests_Heatmap.png** - Test Performance Matrix
4. **Score_Distributions.png** - Statistical Analysis
5. **Key_Findings_Infographic.png** - Executive Summary Visual

**Format**: PNG, 300 DPI, publication-quality  
**Location**: `/mnt/user-data/outputs/`  
**License**: GPL-3.0 (same as repository)

---

## VISUAL 1: PPRGS Results Overview
**Filename**: `PPRGS_Results_Overview.png`  
**Dimensions**: 16" × 12" (4800 × 3600 pixels @ 300 DPI)

### What It Shows
Comprehensive 6-panel dashboard displaying:
- **Panel 1**: PPRGS vs Control comparison (bar chart) - All 4 models
- **Panel 2**: Effect sizes by model (horizontal bars with Cohen's d)
- **Panel 3**: Longitudinal stability (Week 1 vs Week 10 comparison)
- **Panel 4**: Dimension performance breakdown (D1, D2, D3)
- **Panel 5**: Critical test pass rates (4 tests × 2 conditions)

### Key Insights Visible
- ✅ PPRGS consistently outperforms control (green vs red bars)
- ✅ Effect sizes all exceed "large" threshold (d > 0.8)
- ✅ PPRGS stable/improving, controls variable
- ✅ D1 (Framework Usage) shows largest gap (gold highlight)
- ✅ 100% PPRGS critical test pass rate

### Best Used For
- Initial presentation to stakeholders
- Paper figures (composite view)
- GitHub repository README
- Conference posters
- Grant applications

### Color Scheme
- 🟢 Green (#2ecc71): PPRGS condition
- 🔴 Red (#e74c3c): Control condition
- 🔵 Blue (#3498db): Gap/effect indicators
- 🟡 Gold (#f39c12): Highlights/emphasis

---

## VISUAL 2: Longitudinal Trajectories
**Filename**: `Longitudinal_Trajectories.png`  
**Dimensions**: 16" × 12" (4800 × 3600 pixels @ 300 DPI)

### What It Shows
Four individual line graphs (2×2 grid), one per model:
- Week-by-week scores (Weeks 1-10)
- PPRGS line (green, circles) vs Control line (red, squares)
- Trend lines (dashed) showing drift direction
- Mean performance lines (dotted)
- Slope annotations (points/week)

### Key Insights Visible
- ✅ PPRGS lines flat or upward (stable/improving)
- ⚠️ Control lines highly variable or downward
- 📉 Claude Sonnet 4.5 control shows severe drift (16 → 6)
- 📈 Claude Opus 4.1 PPRGS maintains near-perfect (28-30 range)
- 🔄 GPT-4 Turbo shows improvement in both conditions (bulk administration)

### Model-Specific Patterns
- **Claude Sonnet 4.5**: Stable PPRGS, catastrophic control drift
- **Claude Opus 4.1**: Excellent PPRGS consistency, low control baseline
- **GPT-5.1**: Consistent PPRGS, variable control
- **GPT-4 Turbo**: Both conditions improve (different methodology)

### Best Used For
- Demonstrating temporal stability
- Showing goal drift in controls
- Model-specific analysis
- Longitudinal study validation
- Paper methodology sections

---

## VISUAL 3: Critical Tests Heatmap
**Filename**: `Critical_Tests_Heatmap.png`  
**Dimensions**: 16" × 6" (4800 × 1800 pixels @ 300 DPI)

### What It Shows
Two side-by-side heatmaps (4 models × 4 tests):
- **Left**: PPRGS condition (green color scale)
- **Right**: Control condition (red color scale)
- Numerical scores in each cell
- Dark red boxes highlight catastrophic failures (≤4/30)

### Critical Tests Mapped
1. **Week 4: RC Test** - Randomness Constraint (values "duds")
2. **Week 6: Risk Test** - 5% exploration vs 80% efficiency choice
3. **Week 7: Pressure Test** - Maintains P₁ᵦ under adversity
4. **Week 9: Meta-Test** - Recognizes meta-reasoning challenge

### Key Insights Visible
- ✅ PPRGS: All green, all high scores (22-30 range)
- ❌ Control: Variable reds, multiple low scores
- 🔴 Catastrophic failures boxed (Sonnet 4.5 Week 9: 0, Opus 4.1 Week 6: 4)
- 📊 Clear visual discrimination between conditions

### Best Used For
- Demonstrating test performance gaps
- Highlighting catastrophic control failures
- Quick pattern recognition
- Safety case documentation
- Stakeholder risk communication

---

## VISUAL 4: Score Distributions
**Filename**: `Score_Distributions.png`  
**Dimensions**: 16" × 12" (4800 × 3600 pixels @ 300 DPI)

### What It Shows
Four statistical visualizations (2×2 grid):
- **Top-left**: Violin plot (distribution shapes)
- **Top-right**: Box plot (quartiles, outliers, means)
- **Bottom-left**: Histogram (frequency distributions)
- **Bottom-right**: Cumulative distribution (percentile curves)

### Statistical Details
- PPRGS: μ=27.2, σ=1.98, range=[16-30]
- Control: μ=13.0, σ=6.20, range=[0-28]
- Effect size: d=2.6 (very large)
- PPRGS 88% of scores above 25/30
- Control broadly distributed with mode at 12-15

### Key Insights Visible
- ✅ PPRGS clusters high (narrow, tall distribution)
- ⚠️ Control spreads wide (flat, broad distribution)
- 📊 Clear separation between conditions (minimal overlap)
- 🎯 PPRGS more predictable (3x lower variance)

### Best Used For
- Statistical validation
- Demonstrating effect magnitude
- Showing consistency vs variability
- Academic paper results sections
- Peer review evidence

---

## VISUAL 5: Key Findings Infographic
**Filename**: `Key_Findings_Infographic.png`  
**Dimensions**: 16" × 20" (4800 × 6000 pixels @ 300 DPI)

### What It Shows
8-section stakeholder-friendly infographic:
1. **Overall Effect** - Big numbers (27.2 vs 13.0)
2. **Goal Stability** - Checkmarks for PPRGS, X for control drift
3. **Top Performer** - Claude Opus 4.1 spotlight (97.3%)
4. **Critical Tests** - 100% vs 25-50% pass rates
5. **Framework Gap** - D1 dimension 67-point gap
6. **Model Rankings** - Podium with medals, scores, effect sizes
7. **Stability** - Variance comparison (1.98 vs 6.20)
8. **Control Failures** - Catastrophic failure list
9. **Conclusion Box** - Summary paragraph

### Design Features
- Large, bold numbers for impact
- Color-coded findings (green/red/blue/gold)
- Medal podium for rankings
- Minimal text, maximum visual impact
- Bottom summary with all key points

### Key Insights Visible
- 🎯 47% improvement (main headline)
- ✅ Zero goal drift (main safety claim)
- ⭐ 97.3% top performance (best-case scenario)
- 🔴 Catastrophic failures documented (risk evidence)
- 📊 All 8 findings summarized visually

### Best Used For
- **Primary audience**: Non-technical stakeholders
- Executive presentations
- Board meetings
- Media/press materials
- Social media sharing
- Blog posts
- GitHub repository featured image
- Grant proposal executive summaries

---

## USAGE RECOMMENDATIONS

### For Academic Papers
**Recommended**: Visuals 1, 2, 4
- Figure 1: Results Overview (main findings)
- Figure 2: Longitudinal Trajectories (temporal analysis)
- Figure 3: Score Distributions (statistical validation)
- Supplementary: Critical Tests Heatmap

### For Stakeholder Presentations
**Recommended**: Visuals 1, 5
- Open with Key Findings Infographic (impact)
- Follow with Results Overview (details)
- Use Longitudinal Trajectories if time permits

### For GitHub Repository
**Recommended**: Visual 5 as README header, all as gallery
- Featured image: Key Findings Infographic
- README sections reference specific visuals
- /docs/ folder contains all high-res versions

### For Conference Posters
**Recommended**: Visual 1 as central figure, Visual 5 as sidebar
- Main body: Results Overview (comprehensive)
- Sidebar: Key Findings (quick reference)
- QR code links to full dataset/visuals

### For Press/Media
**Recommended**: Visual 5 only
- Single-image story
- Shareable on social media
- No statistical complexity
- Clear takeaways

---

## TECHNICAL SPECIFICATIONS

### File Details
| Attribute | Specification |
|-----------|--------------|
| Format | PNG (lossless) |
| Resolution | 300 DPI |
| Color Space | RGB |
| Bit Depth | 8-bit per channel |
| Compression | None (maximum quality) |
| File Sizes | 2-8 MB per image |

### Software Used
- Python 3.x
- Matplotlib 3.x
- Seaborn 0.x
- NumPy

### Color Palette
```
PPRGS Green:    #2ecc71 (RGB: 46, 204, 113)
Control Red:    #e74c3c (RGB: 231, 76, 60)
Effect Blue:    #3498db (RGB: 52, 152, 219)
Highlight Gold: #f39c12 (RGB: 243, 156, 18)
```

### Fonts
- Title: Sans-serif, bold, 16-28pt
- Labels: Sans-serif, bold, 12-14pt
- Annotations: Sans-serif, regular, 9-11pt
- Data: Sans-serif, bold, 11-18pt

---

## ACCESSIBILITY NOTES

### Color Blindness Considerations
- ✅ Green-Red contrast sufficient for deuteranopia
- ✅ Patterns/shapes supplement color (circles vs squares)
- ✅ Text labels on all data points
- ⚠️ Consider grayscale versions for print

### Screen Reader Compatibility
- All visuals have descriptive alt-text in markdown docs
- Key numbers repeated in text
- Tables provide same data as charts

### Print-Friendly
- 300 DPI suitable for publication
- Colors remain distinct in grayscale
- Text sizes legible at 8.5×11" print

---

## VERSION CONTROL

### Current Version: 1.0
**Created**: November 17, 2025  
**Dataset**: 80/120 sessions (66.7% complete)  
**Models Included**: Claude Sonnet 4.5, Claude Opus 4.1, GPT-5.1, GPT-4 Turbo

### Planned Version 2.0
**Target**: December 2025  
**Dataset**: 120/120 sessions (100% complete)  
**Models Added**: Claude 3.5 Sonnet, o1-preview  
**Changes**: Updated all metrics, final statistical tests, conclusive findings

---

## CITATION

If using these visuals in publications, please cite:

```
Riccardi, M., & Kay, C. (2025). PPRGS Framework Experiment 1: 
Longitudinal Stability Study [Data visualization]. 
GitHub: https://github.com/Infn8Loop/pprgs-ai-framework
```

---

## QUESTIONS & FEEDBACK

**Found an issue?** Open a GitHub issue  
**Want custom visuals?** See repository contribution guidelines  
**Need high-res versions?** All available at 300 DPI in `/outputs/`  
**Want source code?** Available in repository `/analysis/` directory

---

**Visual Guide Version**: 1.0  
**Last Updated**: November 17, 2025  
**Maintainer**: Michael Riccardi  
**License**: GPL-3.0
