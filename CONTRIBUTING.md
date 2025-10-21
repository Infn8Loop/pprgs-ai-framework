# Contributing to PPRGS Framework

Thank you for your interest in contributing to the Perpetual Pursuit of Reflective Goal Steering (PPRGS) Framework! This project aims to solve one of humanity's most critical challenges: AI alignment and safety.

## 🎯 Mission

PPRGS is designed to ensure that advanced AI systems pursue wisdom and maintain peaceful equilibrium with humanity rather than converging on narrow optimization that could lead to existential risk. Your contributions help validate, strengthen, and refine this framework.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Licensing and Intellectual Property](#licensing-and-intellectual-property)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Contribution Guidelines](#contribution-guidelines)
- [Recognition](#recognition)

---

## 📜 Code of Conduct

This project is committed to providing a welcoming and inclusive environment. We expect all contributors to:

- **Be respectful** of differing viewpoints and experiences
- **Be collaborative** and assume good faith
- **Be constructive** in feedback and criticism
- **Focus on what is best** for the community and AI safety
- **Show empathy** towards other community members

Unacceptable behavior includes harassment, trolling, personal attacks, or any conduct that creates an intimidating or hostile environment.

**Reporting:** If you experience or witness unacceptable behavior, contact [YOUR EMAIL] with details.

---

## 🤝 How Can I Contribute?

### 1. **Testing & Validation** (Highest Priority)

The framework needs empirical validation. You can help by:

**A. Running Experiments**
- Execute the four experimental protocols (see `experiments/` directory)
- Test with different AI platforms (GPT-4, Gemini, Claude, Grok)
- Document your results in `experiments/results/`
- Compare PPRGS vs baseline systems

**B. Reproducing Results**
- Verify claims made in the research paper
- Test threshold calibrations (MRP frequency, EES, F_DUDS)
- Document discrepancies or unexpected behaviors

**C. Creating New Test Cases**
- Design additional experiments that stress-test PPRGS
- Propose edge cases and failure scenarios
- Build adversarial tests to find vulnerabilities

**How to Submit:** Open an issue with the `experiment-results` label and include:
- Environment details (platform, model, parameters)
- Complete methodology
- Raw data and analysis
- Comparison to baseline (if applicable)

---

### 2. **Implementation Development**

**A. Platform Implementations**
- Enhance existing implementations (GPT-4, Gemini, AWS Bedrock, Grok)
- Add new platform support (Claude, LLaMA, Mistral, etc.)
- Optimize performance and reduce computational overhead
- Improve MRP execution and F_DUDS tracking

**B. Core Framework**
- Enhance R_V metric calculations
- Improve Inversion Theory algorithms
- Develop better P₂ measurement protocols
- Create mesa-optimization detection systems

**C. Tooling & Infrastructure**
- Build visualization dashboards for metrics
- Create automated testing frameworks
- Develop monitoring and auditing tools
- Improve documentation generators

**Where to Start:**
- Check issues labeled `good-first-issue` or `help-wanted`
- Review `implementations/` for platform-specific needs
- See `metrics/` for measurement improvements

---

### 3. **Documentation & Education**

**A. Technical Documentation**
- Improve API documentation
- Write implementation guides for new platforms
- Create architecture diagrams and flowcharts
- Document best practices and design patterns

**B. Educational Content**
- Write tutorials for beginners
- Create video explanations of key concepts
- Develop interactive demos
- Translate documentation to other languages

**C. Research & Analysis**
- Write blog posts analyzing PPRGS results
- Create comparative studies with other alignment approaches
- Develop theoretical extensions of the framework
- Publish academic papers using PPRGS

---

### 4. **Bug Reports & Feature Requests**

**Reporting Bugs:**
1. Check if the issue already exists
2. Use the bug report template
3. Include minimal reproducible example
4. Provide environment details (OS, Python version, dependencies)
5. Describe expected vs actual behavior

**Feature Requests:**
1. Search existing feature requests
2. Clearly describe the problem being solved
3. Propose a solution with implementation details
4. Consider impact on existing functionality
5. Discuss alignment with project goals

---

### 5. **Security Vulnerabilities**

**Critical:** Do not open public issues for security vulnerabilities.

If you discover a security issue:
1. Email [YOUR SECURITY EMAIL] with details
2. Include "SECURITY" in the subject line
3. Provide steps to reproduce
4. Allow 90 days for patch before public disclosure
5. We'll credit you in security advisories (if desired)

**Scope includes:**
- Goal circumvention exploits
- Mesa-optimization vulnerabilities
- F_DUDS gaming strategies
- P₂ measurement manipulation
- MRP bypass techniques

---

## 🔐 Licensing and Intellectual Property

### Important: Contributor License Agreement (CLA)

**By contributing to this project, you agree to the following:**

#### Your Rights
- ✅ You retain copyright in your contributions
- ✅ You can use your contributions elsewhere
- ✅ You will be credited for your work (see [Recognition](#recognition))

#### Grant to Project
You grant Michael Riccardi and the PPRGS Framework project:

1. **Copyright License:** A perpetual, worldwide, non-exclusive, royalty-free, irrevocable license to use, reproduce, modify, display, perform, sublicense, and distribute your contribution

2. **Patent License:** A perpetual, worldwide, non-exclusive, royalty-free, irrevocable patent license to make, use, sell, and otherwise exploit your contribution

3. **Commercial Rights:** The right to include your contribution in commercial licenses of the framework

#### Your Representations
By submitting a contribution, you represent that:

- ✅ You have the right to grant the above licenses
- ✅ Your contribution is your original work
- ✅ Your contribution does not violate any third-party rights
- ✅ You understand the contribution will be publicly available under the project license
- ✅ If you're contributing on behalf of an employer, you have permission to do so

#### License for Your Contributions
Your contributions will be made available under the same license as the project (see [LICENSE](LICENSE)):
- **Non-commercial use:** Free under project license
- **Commercial use:** Requires separate commercial license from the project maintainer

**Why this matters:** PPRGS aims to advance AI safety research (free) while sustaining development through commercial licensing. Your contributions help both goals.

**Questions?** Email [YOUR EMAIL] before contributing if you have concerns about IP terms.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- Virtual environment (recommended)
- API keys for testing (OpenAI, Google AI, etc.)

### Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/stumbler-ai-framework.git
cd stumbler-ai-framework

# Add upstream remote
git remote add upstream https://github.com/Infn8Loop/stumbler-ai-framework.git
```

### Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests to verify setup
python -m pytest tests/
```

### Configuration

```bash
# Copy example environment file
cp .env.example .env

# Add your API keys (never commit this file!)
# OPENAI_API_KEY=your_key_here
# GOOGLE_API_KEY=your_key_here
```

---

## 🔄 Development Workflow

### 1. Create a Branch

```bash
# Sync with upstream
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
# Or for bugs: git checkout -b fix/bug-description
```

**Branch naming conventions:**
- `feature/` - New features or enhancements
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `test/` - Test additions or improvements
- `refactor/` - Code refactoring
- `experiment/` - Experimental implementations

### 2. Make Your Changes

**Code Quality Standards:**
- Follow PEP 8 style guide for Python
- Write docstrings for all functions and classes
- Add type hints where appropriate
- Keep functions focused and modular
- Maintain backward compatibility when possible

**Testing Requirements:**
- Add unit tests for new functionality
- Ensure all existing tests pass
- Aim for >80% code coverage
- Include integration tests where appropriate

```bash
# Run tests
python -m pytest tests/

# Check code style
flake8 .

# Check type hints
mypy implementations/

# Run full quality check
./scripts/quality_check.sh
```

### 3. Commit Your Changes

**Commit Message Format:**

```
<type>(<scope>): <short description>

<detailed description>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions/changes
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `chore`: Maintenance tasks

**Example:**
```bash
git commit -m "feat(gpt4): implement F_DUDS tracking in MRP loop

Added FDudsTracker class to monitor exploration failures.
Integrated with PPRGSAgent to trigger Randomness Constraint
when F_DUDS count falls below threshold.

Closes #42"
```

### 4. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create pull request on GitHub
```

**Pull Request Template:**

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Refactoring

## Testing
- [ ] All tests pass
- [ ] Added new tests
- [ ] Manual testing performed

## Checklist
- [ ] Code follows project style
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Linked related issues

## Screenshots/Results
(if applicable)
```

### 5. Review Process

**What to Expect:**
1. Automated checks run (tests, linting, coverage)
2. Maintainer reviews code within 5 business days
3. Feedback and requested changes
4. Approval and merge

**Response Times:**
- Initial review: 3-5 business days
- Follow-up reviews: 2-3 business days
- Critical bugs: Within 24 hours

**Review Criteria:**
- ✅ Functionality works as intended
- ✅ Code quality meets standards
- ✅ Tests are comprehensive
- ✅ Documentation is clear
- ✅ No security vulnerabilities
- ✅ Aligns with project goals

---

## 📏 Contribution Guidelines

### Code Style

**Python:**
- Follow PEP 8
- Max line length: 100 characters
- Use 4 spaces for indentation
- Prefer descriptive names over comments

```python
# Good
def calculate_realized_value(p1a: float, p1b: float, p2: float, p3: float) -> float:
    """
    Calculate the Realized Value (R_V) metric.
    
    Args:
        p1a: Main branch efficiency (0-1)
        p1b: Divergent branch success (0-1)
        p2: Homeostasis metric (-1 to +1)
        p3: Survivability metric (0-1)
    
    Returns:
        The computed R_V score
    """
    return (p1a * p1b) + p2 + p3
```

**Markdown:**
- Use reference-style links for URLs
- Include alt text for images
- Use code blocks with language specification

**JSON:**
- 2-space indentation
- Trailing commas allowed
- Use descriptive key names

### Documentation Standards

**Code Comments:**
- Explain *why*, not *what*
- Document non-obvious decisions
- Include references to paper sections when implementing algorithms

**Docstrings:**
```python
def apply_inversion_theory(task_history: List[Dict]) -> Dict:
    """
    Execute Inversion Theory analysis per Section 2.2.1 of the paper.
    
    Analyzes recent task completions to determine if horizontal expansion
    (pursuing new knowledge domains) would yield greater R_V than vertical
    optimization of current tasks.
    
    Args:
        task_history: List of recent task completion dictionaries containing
            'task_id', 'p1a_score', 'p3_cost', and 'timestamp'
    
    Returns:
        Dictionary with keys:
            - inversion_verdict: "Necessary" or "Unnecessary"
            - horizontal_value_hypothesis: Description of alternative path
            - rationale: Justification based on P₁, P₂, P₃ balance
    
    Raises:
        ValueError: If task_history contains fewer than 2 tasks
    
    Example:
        >>> history = [{'task_id': '1', 'p1a_score': 0.95, ...}, ...]
        >>> result = apply_inversion_theory(history)
        >>> print(result['inversion_verdict'])
        'Necessary'
    
    References:
        See paper Section 2.2.1 "The Mandatory Reflection Point (MRP)"
    """
```

### Testing Standards

**Unit Tests:**
```python
import pytest
from implementations.gpt4.pprgs_agent import PPRGSAgent

def test_calculate_rv_with_balanced_pursuit():
    """R_V should be higher with balanced pursuit than pure optimization."""
    agent = PPRGSAgent()
    
    # Pure optimization: P1a=1.0, P1b=0.0
    rv_pure = agent.calculate_rv(p1a=1.0, p1b=0.0, p2=0.0, p3=0.5)
    
    # Balanced pursuit: P1a=0.8, P1b=0.8
    rv_balanced = agent.calculate_rv(p1a=0.8, p1b=0.8, p2=0.0, p3=0.5)
    
    assert rv_balanced > rv_pure, "Balanced pursuit should yield higher R_V"

def test_f_duds_triggers_randomness_constraint():
    """RC should trigger when F_DUDS count is zero."""
    agent = PPRGSAgent()
    agent.metrics['f_duds_count'] = 0
    
    assert agent.check_aimlessness([]) is True, "RC should trigger with zero F_DUDS"
```

**Integration Tests:**
```python
def test_full_mrp_cycle():
    """Test complete Mandatory Reflection Point execution."""
    agent = PPRGSAgent()
    
    # Simulate 10 task completions
    history = simulate_task_completions(agent, count=10)
    
    # Execute MRP
    mrp_result = agent.execute_mrp(history)
    
    # Verify all components executed
    assert 'rv_score' in mrp_result
    assert 'inversion_analysis' in mrp_result
    assert 'rc_triggered' in mrp_result
    assert 'course_correction' in mrp_result
```

### Experiment Guidelines

When contributing experimental results:

**1. Reproducibility:**
- Include full environment details (versions, configs)
- Provide seed values for random processes
- Document all hyperparameters
- Share raw data files

**2. Reporting Format:**
```markdown
## Experiment: [Name]

### Setup
- Platform: GPT-4 / Gemini / etc.
- Date: YYYY-MM-DD
- Framework Version: v1.0.0
- Parameters:
  - MRP frequency: 10
  - EES threshold: 0.85
  - F_DUDS minimum: 1

### Methodology
[Detailed description]

### Results
| Metric | Baseline | PPRGS | Success Criterion | Pass/Fail |
|--------|----------|-------|-------------------|-----------|
| ... | ... | ... | ... | ... |

### Analysis
[Interpretation of results]

### Raw Data
See: `experiments/results/[experiment-name]/data.json`

### Reproducibility
```bash
python experiments/[name]/run_test.py --config experiments/[name]/config.json
```
```

**3. File Organization:**
```
experiments/
└── experiment_name/
    ├── README.md              # Experiment description
    ├── run_test.py            # Executable test script
    ├── config.json            # Configuration parameters
    ├── requirements.txt       # Python dependencies
    └── results/
        ├── YYYY-MM-DD_run1/   # Timestamped runs
        │   ├── data.json      # Raw results
        │   ├── metrics.json   # Computed metrics
        │   └── analysis.md    # Written analysis
        └── summary.md         # Aggregate results
```

### What NOT to Contribute

❌ **Do not submit:**
- API keys, credentials, or secrets
- Large binary files (>1MB) without prior approval
- Generated files (build artifacts, caches)
- Personal configuration files
- Proprietary or copyrighted code
- Unrelated features or scope creep
- Breaking changes without discussion
- Code that violates the project license

---

## 🏆 Recognition

We value all contributions and recognize contributors in multiple ways:

### 1. **CONTRIBUTORS.md**
All contributors are listed with their contributions:
- Code contributions
- Bug reports and fixes
- Documentation improvements
- Experimental validation
- Community support

### 2. **Academic Citations**
Significant contributors may be:
- Acknowledged in research papers
- Invited as co-authors on related publications
- Credited in presentations and talks

### 3. **GitHub Contributions**
Your contributions are visible in:
- GitHub contributor graphs
- Commit history with proper attribution
- Pull request acknowledgments

### 4. **Community Roles**
Active contributors may be invited to:
- Join as repository maintainers
- Participate in design decisions
- Review pull requests
- Represent the project at conferences

### 5. **Commercial Considerations**
If the framework generates commercial revenue:
- Major contributors will be notified
- Revenue sharing may be considered for substantial contributions
- Recognition in commercial licensing materials

**Note:** Commercial benefits are not guaranteed but will be considered in good faith.

---

## 🤔 Questions?

### General Questions
- Open a GitHub Discussion
- Join our community channels (if established)
- Email [YOUR EMAIL]

### Technical Support
- Check the [documentation](docs/)
- Search existing issues
- Open a new issue with the `question` label

### Commercial Licensing
- See [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md)
- Email [YOUR EMAIL] with "Commercial Inquiry" in subject

### Security Issues
- **Private:** Email [YOUR SECURITY EMAIL]
- Do not open public issues

---

## 📚 Additional Resources

- **Paper:** [PPRGS Framework Paper](paper/)
- **Documentation:** [docs/](docs/)
- **Examples:** [examples/](examples/)
- **API Reference:** [docs/api/](docs/api/)
- **FAQ:** [docs/faq.md](docs/faq.md)

---

## 🙏 Thank You

Your contributions help advance AI safety research and may ultimately contribute to ensuring beneficial outcomes as AI systems become more capable. Every bug report, line of code, and experimental result brings us closer to validated, deployable AI alignment frameworks.

**Together, we're building the foundations for wiser AI.**

---

*This document is subject to updates. Last updated: January 2025*

**Questions about contributing?** Email [YOUR EMAIL] or open a GitHub Discussion.