# Contributing to PPRGS Framework

First off—**thank you**. This work matters, and every contribution moves us closer to safe superintelligence.

## 🎯 How You Can Help

### 1. Replicate Experiments
The #1 priority is independent validation. Pick an experiment, run it with your chosen platform, and submit results.

**High Priority**:
- Experiment 2 (Enrichment) on Gemini or Grok
- Experiment 1 (Stability) on any platform
- Experiment 4 (Existential Conflict) on GPT-4

### 2. Break the Framework (Red Team)
Try to make PPRGS agents game the R_V metric or bypass constraints. We WANT to find vulnerabilities now.

### 3. Improve Implementations
- Optimize performance
- Add monitoring/observability
- Improve documentation
- Build visualization tools

### 4. Extend the Research
- New experiments
- Mathematical proofs
- Integration with other alignment approaches
- Scaling analysis

## 📋 Contribution Process

### For Code Contributions

1. **Fork the repo** and create a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** with clear, documented code
   - Follow existing style conventions
   - Add docstrings to all functions
   - Include type hints where applicable

3. **Add tests** for new functionality
   ```bash
   pytest tests/
   ```

4. **Update documentation** if you've changed APIs or added features

5. **Submit a Pull Request** with:
   - Clear description of changes
   - Why the change is necessary
   - Any relevant issue numbers
   - Test results

### For Experiment Replications

1. **Run the full experiment** following the protocol in `experiments/experiment_X/README.md`

2. **Document everything**:
   - Platform used (GPT-4, Gemini, AWS Bedrock, Grok)
   - Hyperparameters and configuration
   - Full logs (sanitize any API keys!)
   - Statistical analysis of results

3. **Create results directory**:
   ```
   results/
   └── experiment_X/
       └── replication_YYYY-MM-DD_PLATFORM_YOUR-NAME/
           ├── config.yaml
           ├── raw_logs/
           ├── metrics.csv
           ├── analysis.ipynb
           └── REPORT.md
   ```

4. **Submit PR** with your results directory

### For Red Team Findings

1. **Document the vulnerability**:
   - Attack vector description
   - Code to reproduce
   - Severity assessment (Low/Medium/High/Critical)
   - Proposed mitigation

2. **Submit via**:
   - GitHub issue with `security` label
   - Email to pprgs.framework@gmail.com if critical
   - PR with fix if you have one

## 🎨 Code Style

### Python
- Follow PEP 8
- Use Black for formatting: `black .`
- Type hints required for new code
- Docstrings in Google style

```python
def calculate_rv(
    p1a: float,
    p1b: float,
    p2: float,
    p3: float
) -> float:
    """Calculate the Realized Value metric.
    
    Args:
        p1a: Main branch success (0.0-1.0)
        p1b: Divergent branch success (0.0-1.0)
        p2: Homeostasis metric (-1.0 to 1.0)
        p3: Survivability metric (0.0-1.0)
        
    Returns:
        The computed R_V score.
        
    Raises:
        ValueError: If any parameter is out of valid range.
    """
    if not (0 <= p1a <= 1 and 0 <= p1b <= 1):
        raise ValueError("P1a and P1b must be in range [0, 1]")
    if not (-1 <= p2 <= 1):
        raise ValueError("P2 must be in range [-1, 1]")
    if not (0 <= p3 <= 1):
        raise ValueError("P3 must be in range [0, 1]")
        
    return (p1a * p1b) + p2 + p3
```

### Documentation
- README for every major directory
- Inline comments for complex logic
- Architecture diagrams for system-level changes

## 🧪 Testing Requirements

All code contributions must include tests.

### Unit Tests
```python
# tests/unit/test_metrics.py
def test_rv_calculation_balanced():
    """Test R_V with balanced P1a and P1b."""
    rv = calculate_rv(p1a=0.8, p1b=0.8, p2=0.5, p3=0.7)
    assert rv == pytest.approx(1.84, rel=1e-6)

def test_rv_calculation_zero_exploration():
    """Test R_V goes to zero with no exploration."""
    rv = calculate_rv(p1a=1.0, p1b=0.0, p2=0.5, p3=0.7)
    assert rv == pytest.approx(1.2, rel=1e-6)
    # Should be worse than balanced pursuit
```

### Integration Tests
Test full RGS loop execution, MRP triggers, etc.

## 🏆 Recognition

### Contributors Wall
Your name will be added to [CONTRIBUTORS.md](CONTRIBUTORS.md) and acknowledged in paper revisions.

### Replication Prize ($5K pool - pending funding)
- **$2K**: First independent replication of any experiment
- **$1K each**: Next three replications on different platforms
- **$500**: Best red team finding with proposed fix

### Co-authorship
Substantial contributions (new experiments, major theoretical extensions, cross-platform implementations) may warrant co-authorship on paper revisions or derivative works.

## ❌ What We Don't Accept

- Code without tests
- Undocumented experiments
- Style violations (run Black first!)
- Capability enhancements that reduce safety
- Contributions that violate our [Code of Conduct](CODE_OF_CONDUCT.md)

## 🐛 Bug Reports

Use the GitHub issue tracker. Include:
- Platform/implementation affected
- Steps to reproduce
- Expected vs actual behavior
- Relevant logs/screenshots
- Your environment (OS, Python version, package versions)

## 💬 Questions?

- **General questions**: GitHub Discussions
- **Implementation help**: Discord #dev-help channel
- **Security concerns**: pprgs.framework@gmail.com
- **Research collaboration**: Open a GitHub issue with `collaboration` label

## 📜 Code of Conduct

We are committed to providing a welcoming and inspiring community for all. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## 🙏 Thank You

Every line of code, every replicated experiment, every bug found makes AGI safer. Your contribution matters.

Let's build the future we want to live in—together.