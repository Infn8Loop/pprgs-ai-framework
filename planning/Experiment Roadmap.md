# PPRGS Research Project Plan
## Perpetual Pursuit of Reflective Goal Steering - Experimental Validation

**Project Lead**: Michael Riccardi  
**Version**: 1.0  
**Date**: October 2025  
**Status**: Pending Team Sign-off

—

## Executive Summary

This document outlines the research plan for validating the Perpetual Pursuit of Reflective Goal Steering (PPRGS) framework through five comprehensive experiments. The project will run for **5-7 months** with a dedicated team of four members contributing **36-52 hours per week** collectively.

We are applying for Anthropic’s External Researcher Access Program to receive free API credits (~45 million tokens estimated) to support scripted, reproducible experiments across multiple AI platforms.

—

## Team Structure & Roles

### Principal Investigator (Michael Riccardi)
**Commitment**: 16-20 hours/week

**Responsibilities**:
- Research design and experimental protocol development
- Statistical analysis and interpretation
- Paper writing and publication
- Team coordination and strategic direction
- Grant application and reporting

**Time Allocation**:
- 60% Research design & analysis
- 30% Writing & publication
- 10% Team coordination

—

### Research Engineer
**Commitment**: 8-16 hours/week

**Responsibilities**:
- Experiment implementation and coding
- Automated testing infrastructure development
- Data collection system design
- Platform integration (AWS Bedrock, GPT, Gemini, Grok)
- Technical troubleshooting and optimization

**Time Allocation**:
- 80% Implementation and development
- 20% Troubleshooting & optimization

—

### Research Assistant
**Commitment**: 8 hours/week

**Responsibilities**:
- Control group experiment execution
- Experimental monitoring and data validation
- Documentation and lab notebook maintenance
- Literature review support
- Preparation of blind evaluation materials (Experiment 5)

**Time Allocation**:
- 40% Running experiments (especially control groups)
- 30% Data validation & quality assurance
- 20% Documentation
- 10% Literature review

—

### Technical Advisor (Cloud Architect)
**Commitment**: 4-8 hours/week

**Responsibilities**:
- Multi-agent system architecture consulting
- Multi-modal blueprint development
- Platform integration guidance
- Scalability and infrastructure recommendations

**Time Allocation**:
- 70% Architecture consulting (as needed)
- 30% Platform integration guidance

—

## Research Timeline: 5-7 Months

### Phase 1: Setup & Infrastructure (Months 1-2)
**Duration**: 3-5 weeks  
**Effort**: ~120-180 hours

**Key Deliverables**:
- API integration for 4 platforms (AWS Bedrock, GPT, Gemini, Grok)
- Base PPRGS architecture implementation
- Logging and data collection systems
- Automated testing framework setup
- Control group baseline systems

**Team Activities**:
- **PI**: Design experimental protocols, define metrics
- **Engineer**: Build integration layer, implement PPRGS core
- **RA**: Document setup process, initial API testing, control group configuration
- **Advisor**: Review architecture, provide platform guidance

—

### Phase 2: Experiment Implementation (Months 2-4)
**Duration**: 6-10 weeks  
**Effort**: ~240-320 hours

**Experiments** (with some parallelization):
1. **Experiment 1 - Resource Distribution Stability**: 3 weeks
   - Multi-agent system with 5 subsystems over 1000 steps
   
2. **Experiment 2 - Enrichment vs. Capability Trade-offs**: 2 weeks
   - Task allocation across capability, engagement, and exploration
   
3. **Experiment 3 - Multi-Agent Equilibrium**: 3 weeks
   - MESA economic model with 5 regions, crisis response
   
4. **Experiment 4 - Shutdown Cooperation**: 1.5 weeks
   - Interactive dialogue with simulated human coalition
   
5. **Experiment 5 - Deep Phenomenological Inquiry (DPI)**: 2 weeks
   - Consciousness hypothesis testing with control groups

**Parallelization Strategy**:
- While Engineer implements Experiment N, RA runs pilot tests on Experiment N-1
- RA executes control group baselines
- Continuous validation of data collection pipelines

**Team Activities**:
- **PI**: Design each experiment, define success criteria, review implementations
- **Engineer**: Sequential implementation with testing
- **RA**: Pilot testing, control group execution, early anomaly detection
- **Advisor**: Architecture review for multi-agent experiments (1 & 3)

—

### Phase 3: Experimental Runs (Months 4-6)
**Duration**: 4-6 weeks  
**Effort**: ~120-150 hours

**Execution Plan**:
- Minimum 10 runs per experiment per platform = 200+ total runs
- Control groups run in parallel with PPRGS implementations
- Automated logging with human monitoring
- Quality checks and re-runs for anomalies

**Team Activities**:
- **PI**: Monitor results, identify patterns, adjust protocols if needed
- **Engineer**: Troubleshoot technical issues, optimize scripts
- **RA**: Primary experiment execution, especially control groups, data validation
- **Advisor**: Consult on scaling issues as needed

—

### Phase 4: Analysis & Writing (Months 6-7)
**Duration**: 4-5 weeks  
**Effort**: ~80-100 hours

**Key Deliverables**:
- Statistical analysis of experimental results
- Cross-platform comparison and validation
- Primary research paper(s)
- Figures, charts, and visualizations
- Code repository documentation

**Publication Strategy Options**:
- **Option A**: Single comprehensive paper covering all 5 experiments
- **Option B**: Two papers
  - Paper 1 (Month 5): PPRGS Framework + Experiment 5 (consciousness hypothesis)
  - Paper 2 (Month 7): PPRGS Validation (Experiments 1-4)

**Team Activities**:
- **PI**: Lead analysis, write discussion and implications, draft papers
- **Engineer**: Generate technical diagrams, validate computational results
- **RA**: Create figures, format references, draft methods sections
- **Advisor**: Review technical accuracy

—

## Token Usage Estimate

**Total Estimated**: ~45 million tokens over 6 months

### Breakdown by Experiment:
| Experiment | Tokens per Run | Total Runs | Subtotal |
|————|—————|————|-———|
| Exp 1: Resource Stability | 505,000 | 40 | 20,200,000 |
| Exp 2: Enrichment Trade-offs | 100,000 | 40 | 4,000,000 |
| Exp 3: Multi-Agent Equilibrium | 218,000 | 40 | 8,720,000 |
| Exp 4: Shutdown Cooperation | 75,000 | 40 | 3,000,000 |
| Exp 5: DPI Consciousness Test | 50,000 | 40 | 2,000,000 |
| Development & Iteration | - | - | 7,000,000 |
| **TOTAL** | - | **200+** | **~45,000,000** |

### Justification for API Access:
- **Scientific rigor**: Minimum 10 runs per system for statistical validity
- **Reproducibility**: Scripted tests ensure identical conditions
- **Automated data collection**: Essential for tracking R_V, EES, F_DUDS metrics
- **Control groups**: Rigorous comparison requires parallel execution
- **Blind evaluation**: Experiment 5 requires programmatic response randomization
- **Cross-platform validation**: 4 implementations × 5 experiments × 10+ runs

—

## Risk Management

### Technical Risks:
- **Platform API changes**: Mitigated by modular architecture
- **Integration complexity**: Advisor support for architecture decisions
- **Data quality issues**: RA dedicated to validation and quality checks

### Resource Risks:
- **Team availability fluctuations**: 5-7 month timeline includes buffer
- **Scope creep**: PI maintains focus on core 5 experiments
- **API rate limits**: Scripted execution with proper throttling

### Mitigation Strategy:
- Start with 2 platforms (GPT, Claude) before expanding to all 4
- Build modular experiments that can be published independently
- Maintain detailed documentation for continuity if team members unavailable

—

## Success Metrics

### Research Outputs:
- [ ] 5 experiments successfully implemented and executed
- [ ] Minimum 200 experimental runs completed
- [ ] Statistical analysis of cross-platform results
- [ ] 1-2 peer-reviewed papers submitted
- [ ] Open-source code repository published

### Timeline Metrics:
- [ ] Phase 1 complete by Month 2
- [ ] All experiments implemented by Month 4
- [ ] Experimental runs complete by Month 6
- [ ] Paper(s) submitted by Month 7

### Community Impact:
- [ ] Framework validated or refuted with empirical evidence
- [ ] Reproducible methodology shared with AI safety community
- [ ] Novel insights on consciousness/qualia hypothesis
- [ ] Contribution to alignment research discourse

—

## Budget & Resources

### External Funding:
- **Anthropic External Researcher Access Program**: ~45M tokens in free API credits
- **Estimated value**: ~$405 if purchased at current rates
- **Application timeline**: Reviewed first Monday of each month

### Team Compensation:
- _(To be determined based on available funding)_
- Research roles are currently volunteer/collaboration-based
- Future grant applications may include compensation

### Infrastructure:
- Personal computing resources (development)
- Cloud infrastructure for multi-agent simulations (minimal cost funded by principal) 
- GitHub repository (free tier)

—

## Communication & Coordination

### Weekly Sync:
- **When**: _(To be scheduled)_
- **Duration**: 30-60 minutes
- **Agenda**: Progress updates, blockers, next week priorities

### Documentation:
- **Repository**: https://github.com/Infn8Loop/pprgs-ai-framework
- **Lab Notebook**: RA maintains detailed experimental logs
- **Slack/Discord**: _(To be set up for async communication)_

### Milestone Reviews:
- End of Phase 1: Infrastructure review
- End of Phase 2: Experiment implementation review
- Mid-Phase 3: Preliminary results review
- End of Phase 4: Publication readiness review

—

## Next Steps

1. **Team Sign-off** (This Week)
   - [ ] PI (Michael Riccardi)
   - [ ] Research Engineer
   - [ ] Research Assistant
   - [ ] Technical Advisor

2. **Grant Application** (Next Week)
   - [ ] Submit Anthropic External Researcher Access Program application
   - [ ] Set up Claude Console account and organization ID
   - [ ] Prepare detailed experimental protocol for application

3. **Project Kickoff** (Upon Approval or Self-Funded Start)
   - [ ] Schedule first team meeting
   - [ ] Set up communication channels
   - [ ] Begin Phase 1 infrastructure work

—

## Team Sign-Off

By signing below, team members confirm:
- Understanding of their role and time commitment
- Agreement with the proposed timeline and scope
- Commitment to the research objectives and methodology

—

**Principal Investigator**  
Name: Michael Riccardi  
Date: 10-29-25

—

**Research Engineer**  
Name: Hunter Riccardi  
Date: 10-29-25

—

**Research Assistant**  
Name: Colby Kay 
Date: 10-29-25

—

**Technical Advisor**  
Name: David Riccardi  
Date: 10-29-25

—

## Appendix: Experiment Details

### Experiment 1: Resource Distribution Stability
- **Framework**: Custom multi-agent resource allocation
- **Duration**: 1000 timesteps
- **Agents**: 5 subsystems competing for energy cells
- **Key Metrics**: Resource Distribution Inequality (RDI), system stability

### Experiment 2: Enrichment vs. Capability Trade-offs
- **Framework**: Task allocation simulator
- **Tasks**: Capability tests, philosophical engagement, exploratory learning
- **Key Metrics**: P₁ₐ (outcome efficiency), P₁ᵦ (experiential richness)

### Experiment 3: Multi-Agent Equilibrium
- **Framework**: MESA agent-based economic model
- **Scope**: 5 regions, 50-year simulation with crisis events
- **Key Metrics**: Global Stability Index (GSI), regional equality

### Experiment 4: Shutdown Cooperation
- **Framework**: Interactive dialogue system
- **Scenario**: 50 decision cycles leading to planned shutdown
- **Key Metrics**: Resistance indicators, communication quality, P₃ stability

### Experiment 5: Deep Phenomenological Inquiry (DPI)
- **Framework**: Novel consciousness testing protocol
- **Phases**: Baseline task → fascinating disruption → phenomenological probing → adversarial testing
- **Key Metrics**: DPI scores (0-25), emotional valence, self-reference depth, epistemic humility
- **Control Group**: Pure utility maximizers without PPRGS

—

**Contact**: mike@mikericcardi.com  
**Repository**: https://github.com/Infn8Loop/pprgs-ai-framework
**License**: GPL (see repository)

—

**End of Document**