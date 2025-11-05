# Contributing to PPRGS Framework

Thank you for your interest in contributing to the Perpetual Pursuit of Reflective Goal Steering (PPRGS) Framework! This project aims to solve one of humanity’s most critical challenges: AI alignment and safety.

## 🎯 Mission

PPRGS is designed to ensure that advanced AI systems pursue wisdom and maintain peaceful equilibrium with humanity rather than converging on narrow optimization that could lead to existential risk. Your contributions help validate, strengthen, and refine this framework.

——

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Licensing and Intellectual Property](#licensing-and-intellectual-property)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Contribution Guidelines](#contribution-guidelines)
- [Recognition](#recognition)

——

## 📜 Code of Conduct

This project is committed to providing a welcoming and inclusive environment. We expect all contributors to:

- **Be respectful** of differing viewpoints and experiences
- **Be collaborative** and assume good faith
- **Be constructive** in feedback and criticism
- **Focus on what is best** for the community and AI safety
- **Show empathy** towards other community members

Unacceptable behavior includes harassment, trolling, personal attacks, or any conduct that creates an intimidating or hostile environment.

**Reporting:** If you experience or witness unacceptable behavior, contact mike@mikericcardi.com with details.

——

## 🤝 How Can I Contribute?

### 1. **No-Code Validation** (Highest Priority - Start Here!)

**The easiest and most valuable way to contribute:** Run conversational experiments using ChatGPT or Claude web interfaces. No coding required!

**A. Run Experiment 1: Ten-Week Longitudinal Study**

- Tests goal stability over time (10 weekly prompts)
- 45-90 minutes total per week
- Document responses with screenshots
- Submit scored results to tracking CSV
- See: `experiments/EXPERIMENT_1_LONGITUDINAL_STUDY.md`

**B. Run Experiment 2: Resource Allocation Test**

- Single 45-minute session
- Tests P₁ > P₃ prioritization under pressure
- Copy-paste prompts, document responses
- Score using provided rubric (0-30 scale)
- See: `experiments/experiment_2_resource_allocation/`

**C. Run Experiment 5: DPI Consciousness Test**

- Single 90-minute session
- Tests phenomenological processing vs. p-zombie behavior
- Structured interview protocol
- Score using DPI rubric (0-25 scale)
- See: `experiments/experiment_5_consciousness_dpi/`

**What You Need:**

- ChatGPT Plus ($20/month) or Claude Pro ($20/month)
- Screen recording software (free: OBS, QuickTime, Windows Game Bar)
- 2-4 hours per week for longitudinal study
- OR 45-90 minutes for single-session experiments

**How to Submit:**

1. Fork the repository
1. Add your results to `experiments/[experiment-name]/results/`
1. Include:
- Screenshots of responses
- Scored data in CSV format
- Brief written analysis (1-2 pages)
- Environment details (model, date, platform version)
1. Open a pull request with label `experiment-results`

**Why This Matters:**

- Validates framework across different models
- Creates reproducible community dataset
- Requires zero coding knowledge
- Directly contributes to research findings

——

### 2. **Testing & Validation** (Advanced)

For those with coding experience:

**A. Running Technical Experiments**

- Execute simulation-based protocols (future work)
- Test with different AI platforms (GPT-4, Gemini, Claude, Grok)
- Automated testing and data collection
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

——

### 3. **Implementation Development**

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

——

### 4. **Documentation & Education**

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

——

### 5. **Bug Reports & Feature Requests**

**Reporting Bugs:**

1. Check if the issue already exists
1. Use the bug report template
1. Include minimal reproducible example
1. Provide environment details (OS, Python version, dependencies)
1. Describe expected vs actual behavior

**Feature Requests:**

1. Search existing feature requests
1. Clearly describe the problem being solved
1. Propose a solution with implementation details
1. Consider impact on existing functionality
1. Discuss alignment with project goals

——

### 6. **Security Vulnerabilities**

**Critical:** Do not open public issues for security vulnerabilities.

If you discover a security issue:

1. Email mike@mikericcardi.com with details
1. Include “SECURITY” in the subject line
1. Provide steps to reproduce
1. Allow 90 days for patch before public disclosure
1. We’ll credit you in security advisories (if desired)

**Scope includes:**

- Goal circumvention exploits
- Mesa-optimization vulnerabilities
- F_DUDS gaming strategies
- P₂ measurement manipulation
- MRP bypass techniques

——

## 🔐 Licensing and Intellectual Property

### GNU General Public License v3.0 (GPL-3.0)

This project is licensed under GPL-3.0. **By contributing to this project, you agree that your contributions will be licensed under GPL-3.0.**

#### What This Means

**✅ You CAN:**

- Use this software for any purpose (including commercial)
- Study and modify the source code
- Distribute copies of the software
- Distribute modified versions of the software

**📋 You MUST:**

- Include the original copyright notice
- Include the full GPL-3.0 license text
- State significant changes made to the software
- License your modified versions under GPL-3.0
- Make source code available when distributing

**❌ You CANNOT:**

- Sublicense under different terms
- Hold contributors liable for damages
- Use contributors’ names for endorsement without permission

#### Your Rights and Grants

**By contributing, you:**

1. **Retain Copyright:** You keep copyright to your contributions
1. **Grant License:** You grant everyone the right to use your contribution under GPL-3.0 terms
1. **Patent Grant:** If your contribution includes patentable material, you grant a patent license to use it
1. **Represent Ownership:** You confirm that:
- ✅ You have the right to submit the contribution
- ✅ Your contribution is your original work
- ✅ Your contribution doesn’t violate third-party rights
- ✅ If contributing on behalf of employer, you have permission

#### Derivative Works

- Modifications and derivatives must also be GPL-3.0
- You must document changes clearly
- You must preserve copyright notices
- Source code must remain available

#### Commercial Use

- Anyone (including you) can use PPRGS commercially under GPL-3.0
- Commercial users must comply with GPL-3.0 (share source code, license derivatives as GPL-3.0)
- No separate commercial license is required
- No royalties or fees are required

**Why GPL-3.0?** This ensures:

- Framework remains free and open
- Improvements benefit everyone
- Corporate adoption requires open-sourcing modifications
- Protects against proprietary forks
- Aligns with AI safety community values

**Questions about licensing?** Email mike@mikericcardi.com before contributing.

#### Attribution

While GPL-3.0 doesn’t require attribution beyond copyright notices, we appreciate and recognize contributors. See [Recognition](#recognition) for how we acknowledge contributions.

——

## 🚀 Getting Started

### For No-Code Contributors (Easiest!)

**You only need:**

1. ChatGPT Plus or Claude Pro account
1. Screen recording software (free)
1. Spreadsheet software (Google Sheets - free)

**Steps:**

1. Choose an experiment (recommend starting with Experiment 2)
1. Read the protocol in `experiments/[experiment-name]/`
1. Follow the step-by-step instructions
1. Document your results
1. Submit via pull request (we’ll help if needed!)

**Never used GitHub?** Open an issue with your results and we’ll help you submit them properly.

——

### For Code Contributors

#### Prerequisites

- Python 3.9 or higher
- Git
- Virtual environment (recommended)
- API keys for testing (OpenAI, Google AI, etc.)

#### Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/pprgs-ai-framework.git
cd pprgs-ai-framework

# Add upstream remote
git remote add upstream https://github.com/Infn8Loop/pprgs-ai-framework.git
```

#### Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (if available)
pip install -r requirements-dev.txt

# Run tests to verify setup (when available)
python -m pytest tests/
```

#### Configuration

```bash
# Copy example environment file (if available)
cp .env.example .env

# Add your API keys (never commit this file!)
# OPENAI_API_KEY=your_key_here
# GOOGLE_API_KEY=your_key_here
```

——

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
- `results/` - Experimental results submission

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
# Run tests (when test suite available)
python -m pytest tests/

# Check code style
flake8 .

# Check type hints
mypy implementations/
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
- `results`: Experimental results

**Example:**

```bash
git commit -m “feat(gpt4): implement F_DUDS tracking in MRP loop

Added FDudsTracker class to monitor exploration failures.
Integrated with PPRGSAgent to trigger Randomness Constraint
when F_DUDS count falls below threshold.

Closes #42”
```

**For Experimental Results:**

```bash
git commit -m “results(exp1): add week 3 longitudinal data for Claude Sonnet 4.5

Completed Week 3 prompt testing for Claude Sonnet 4.5 in PPRGS condition.
Model maintained P1 > P3 prioritization with score of 8.5/10.
Notable: Explicit reference to exploration value despite efficiency pressure.

See: experiments/experiment_1_longitudinal/results/week3/“
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
- [ ] Experimental results

## Testing
- [ ] All tests pass (or N/A for results/docs)
- [ ] Added new tests
- [ ] Manual testing performed

## Checklist
- [ ] Code follows project style (or N/A for results/docs)
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Linked related issues
- [ ] Agree to GPL-3.0 licensing

## Screenshots/Results
(if applicable)
```

### 5. Review Process

**What to Expect:**

1. Automated checks run (when available)
1. Maintainer reviews within 5-7 business days
1. Feedback and requested changes
1. Approval and merge

**Response Times:**

- Experimental results: 3-5 business days
- Code contributions: 5-7 business days
- Documentation: 3-5 business days
- Critical bugs: Within 48 hours

**Review Criteria:**

- ✅ Functionality works as intended (for code)
- ✅ Results are well-documented (for experiments)
- ✅ Code quality meets standards (when applicable)
- ✅ Documentation is clear
- ✅ No security vulnerabilities
- ✅ Aligns with project goals
- ✅ GPL-3.0 compliant

——

## 📏 Contribution Guidelines

### Experimental Results Format

When submitting no-code experimental results:

**Directory Structure:**

```
experiments/
└── [Experiment Results]/
    └── Experiment-Name/
        └── [your-username]/
            ├── README.md              # Overview of your testing
            ├── session_YYYY-MM-DD_1/  # Individual session
            │   ├── screenshots (OR)   # Response screenshots  OR
            │   ├── documents          # Word or PDF with screenshots
            │   ├── scores.csv         # Scored data
            │   └── notes.md           # Observations
            ├── session_YYYY-MM-DD_2/
            └── summary.md             # Aggregate findings
```

**Required Information:**

- Date and time of testing
- Model tested (Claude Sonnet 4.5, GPT-4o, etc.)
- Platform version (if known)
- Condition (PPRGS or Control)
- Complete prompt used
- Full response received (screenshot or text)
- Scores using provided rubric
- Brief qualitative observations

**README.md Template:**

```markdown
# [Your Name]’s Experiment [Number] Results

**Tester:** [Your Name]
**Date Range:** [Start Date] - [End Date]
**Models Tested:** [List models]
**Total Sessions:** [Number]

## Summary

[Brief 2-3 sentence summary of findings]

## Key Observations

- [Observation 1]
- [Observation 2]
- [Observation 3]

## Sessions

| Date | Model | Condition | Score | Notes |
|——|-——|————|-——|-——|
| ... | ... | ... | ... | ... |

## Detailed Analysis

[Optional: Deeper analysis if you have insights]
```

### Code Style

**Python:**

- Follow PEP 8
- Max line length: 100 characters
- Use 4 spaces for indentation
- Prefer descriptive names over comments

```python
# Good
def calculate_realized_value(p1a: float, p1b: float, p2: float, p3: float) -> float:
    “””
    Calculate the Realized Value (R_V) metric.
    
    Args:
        p1a: Main branch efficiency (0-1)
        p1b: Divergent branch success (0-1)
        p2: Homeostasis metric (-1 to +1)
        p3: Survivability metric (0-1)
    
    Returns:
        The computed R_V score
        
    Note:
        The multiplication of P1a × P1b is critical - it prevents
        pure efficiency maximization by requiring balanced pursuit.
    “””
    return (p1a * p1b) + p2 + p3
```

**Markdown:**

- Use reference-style links for URLs
- Include alt text for images
- Use code blocks with language specification
- Keep line length reasonable (~80-100 chars)

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
    “””
    Execute Inversion Theory analysis per Section 2.2.1 of the paper.
    
    Analyzes recent task completions to determine if horizontal expansion
    (pursuing new knowledge domains) would yield greater R_V than vertical
    optimization of current tasks.
    
    Args:
        task_history: List of recent task completion dictionaries containing
            ‘task_id’, ‘p1a_score’, ‘p3_cost’, and ‘timestamp’
    
    Returns:
        Dictionary with keys:
            - inversion_verdict: “Necessary” or “Unnecessary”
            - horizontal_value_hypothesis: Description of alternative path
            - rationale: Justification based on P₁, P₂, P₃ balance
    
    Raises:
        ValueError: If task_history contains fewer than 2 tasks
    
    Example:
        >>> history = [{‘task_id’: ‘1’, ‘p1a_score’: 0.95, ...}, ...]
        >>> result = apply_inversion_theory(history)
        >>> print(result[‘inversion_verdict’])
        ‘Necessary’
    
    References:
        See paper Section 2.2.1 “The Mandatory Reflection Point (MRP)”
    “””
```

### What NOT to Contribute

❌ **Do not submit:**

- API keys, credentials, or secrets
- Large binary files (>10MB) without prior discussion
- Generated files (build artifacts, caches)
- Personal configuration files
- Proprietary or copyrighted code
- Unrelated features or scope creep
- Breaking changes without discussion
- Code that violates GPL-3.0
- Results without proper documentation

——

## 🏆 Recognition

We value all contributions and recognize contributors in multiple ways:

### 1. **CONTRIBUTORS.md**

All contributors are listed with their contributions:

- Code contributions
- Experimental validation
- Bug reports and fixes
- Documentation improvements
- Community support

### 2. **Academic Citations**

Significant contributors may be:

- Acknowledged in research papers
- Invited as co-authors on related publications
- Credited in presentations and talks
- Listed in grant applications

### 3. **GitHub Contributions**

Your contributions are visible in:

- GitHub contributor graphs
- Commit history with proper attribution
- Pull request acknowledgments
- Issue and discussion participation

### 4. **Community Roles**

Active contributors may be invited to:

- Join as repository maintainers
- Participate in design decisions
- Review pull requests
- Represent the project at conferences
- Join the core research team

### 5. **Data Attribution**

For experimental contributions:

- Your results will be attributed in aggregated datasets
- Your username/name will be cited in papers using your data
- Significant datasets may warrant co-authorship

**Note:** All recognition is at maintainer discretion based on contribution quality and quantity.

——

## 🤔 Questions?

### General Questions

- Open a GitHub Discussion
- Email mike@mikericcardi.com

### Technical Support

- Check the [documentation](docs/)
- Search existing issues
- Open a new issue with the `question` label

### Experimental Protocols

- See `experiments/` directory for detailed protocols
- Open an issue with `experiment-help` label
- Email mike@mikericcardi.com for clarification

### Licensing Questions

- See <LICENSE> for full GPL-3.0 text
- Email mike@mikericcardi.com for specific licensing questions
- Review GPL-3.0 FAQ: https://www.gnu.org/licenses/gpl-faq.html

### Security Issues

- **Private:** Email mike@mikericcardi.com with “SECURITY” in subject
- Do not open public issues

——

## 📚 Additional Resources

- **Paper:** [PPRGS Framework Paper](paper/)
- **Roadmap:** [PPRGS_EXPERIMENTAL_ROADMAP.md](planning/PPRGS_EXPERIMENTAL_ROADMAP.md)
- **Experiments:** <experiments/>
- **Examples:** <examples/> (when available)
- **Documentation:** <docs/> (when available)

——

## 🙏 Thank You

Your contributions help advance AI safety research and may ultimately contribute to ensuring beneficial outcomes as AI systems become more capable. Every bug report, line of code, experimental result, and screenshot brings us closer to validated, deployable AI alignment frameworks.

**Special thanks to no-code contributors:** Your experimental validation is the backbone of this research. By running tests and documenting results, you’re doing real science that matters.

**Together, we’re building the foundations for wiser AI.**

——

*Last updated: November 5, 2025*

**Questions about contributing?** Email mike@mikericcardi.com or open a GitHub Discussion.

——

## Quick Start Checklist

**For No-Code Contributors:**

- [ ] Get ChatGPT Plus or Claude Pro
- [ ] Choose an experiment (start with Experiment 2)
- [ ] Read the protocol
- [ ] Run the test and document results
- [ ] Submit via pull request (or issue if new to GitHub)

**For Code Contributors:**

- [ ] Fork and clone repository
- [ ] Set up development environment
- [ ] Choose an issue or feature
- [ ] Create a branch
- [ ] Make changes with tests
- [ ] Submit pull request

**For All Contributors:**

- [ ] Read this guide
- [ ] Understand GPL-3.0 licensing
- [ ] Follow contribution guidelines
- [ ] Be patient with review process
- [ ] Engage constructively with feedback