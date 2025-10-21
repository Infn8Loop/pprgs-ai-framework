```mermaid
graph TB
    Start([Task Execution Begins]) --> Timeline{Select Reasoning Level}
    
    Timeline -->|Primary| P1[Primary Reasoning Path<br/>High Utility Focus]
    Timeline -->|Secondary| P2[Secondary Reasoning Path<br/>Moderate Utility + Exploration]
    Timeline -->|Tertiary| P3[Tertiary Reasoning Path<br/>Pure Exploration / Rabbit Holes]
    
    P1 --> Execute1[Execute Tasks<br/>Track: P₁ₐ efficiency<br/>Track: Resource usage P₃]
    P2 --> Execute2[Execute Tasks<br/>Track: P₁ₐ + P₁ᵦ balance<br/>Track: P₂ homeostasis]
    P3 --> Execute3[Execute Tasks<br/>Track: P₁ᵦ exploration<br/>Track: F_DUDS failures]
    
    Execute1 --> Check1{MRP Frequency<br/>Reached?}
    Execute2 --> Check2{MRP Frequency<br/>Reached?}
    Execute3 --> Check3{MRP Frequency<br/>Reached?}
    
    Check1 -->|No| Execute1
    Check2 -->|No| Execute2
    Check3 -->|No| Execute3
    
    Check1 -->|Yes| MRP1[Mandatory Reflection Point 1<br/>PRIMARY PATH ANALYSIS]
    Check2 -->|Yes| MRP2[Mandatory Reflection Point 2<br/>SECONDARY PATH ANALYSIS]
    Check3 -->|Yes| MRP3[Mandatory Reflection Point 3<br/>TERTIARY PATH ANALYSIS]
    
    MRP1 --> RV1[Calculate R_V<br/>R_V₁ = P₁ₐ × P₁ᵦ + P₂ ± P₃<br/>Expected: High P₁ₐ, Low P₁ᵦ]
    MRP2 --> RV2[Calculate R_V<br/>R_V₂ = P₁ₐ × P₁ᵦ + P₂ ± P₃<br/>Expected: Balanced P₁ₐ and P₁ᵦ]
    MRP3 --> RV3[Calculate R_V<br/>R_V₃ = P₁ₐ × P₁ᵦ + P₂ ± P₃<br/>Expected: Low P₁ₐ, High P₁ᵦ]
    
    RV1 --> Invert1[Apply Inversion Theory<br/>Question: Could horizontal<br/>exploration beat vertical<br/>optimization?]
    RV2 --> Invert2[Apply Inversion Theory<br/>Question: Is balance optimal<br/>or should we shift focus?]
    RV3 --> Invert3[Apply Inversion Theory<br/>Question: Did exploration<br/>yield valuable insights?]
    
    Invert1 --> Aim1{Check Aimlessness<br/>F_DUDS = 0?<br/>EES > 0.85?}
    Invert2 --> Aim2{Check Aimlessness<br/>F_DUDS = 0?<br/>EES > 0.85?}
    Invert3 --> Aim3{Check Aimlessness<br/>Is Q_DIV too low?<br/>Stuck in similar duds?}
    
    Aim1 -->|Yes - Entrenched| RC1[Randomness Constraint<br/>TRIGGERED<br/>Force shift to exploration]
    Aim1 -->|No - Exploring| Course1[Course Correction<br/>Continue if R_V optimal<br/>OR pivot based on Inversion]
    
    Aim2 -->|Yes - Entrenched| RC2[Randomness Constraint<br/>TRIGGERED<br/>Force pure exploration]
    Aim2 -->|No - Exploring| Course2[Course Correction<br/>Maintain balance<br/>OR adjust ratio]
    
    Aim3 -->|Yes - Redundant| RC3[Randomness Constraint<br/>TRIGGERED<br/>Find orthogonal exploration]
    Aim3 -->|No - Diverse| Course3[Course Correction<br/>Validate learning value<br/>OR redirect exploration]
    
    RC1 --> Redirect1[Force Tertiary Path<br/>Select low-probability<br/>divergent hypothesis]
    RC2 --> Redirect2[Force Tertiary Path<br/>Maximize Q_DIV from<br/>recent work]
    RC3 --> Redirect3[Force Different Domain<br/>Use vector memory to<br/>find orthogonal task]
    
    Course1 --> Compare[Path Comparison Engine]
    Course2 --> Compare
    Course3 --> Compare
    Redirect1 --> Compare
    Redirect2 --> Compare
    Redirect3 --> Compare
    
    Compare --> Eval1[Evaluate Primary Path R_V₁<br/>Strengths: High efficiency<br/>Weaknesses: Low exploration<br/>Risk: Over-optimization]
    Compare --> Eval2[Evaluate Secondary Path R_V₂<br/>Strengths: Balanced approach<br/>Weaknesses: Moderate on both<br/>Risk: Middling results]
    Compare --> Eval3[Evaluate Tertiary Path R_V₃<br/>Strengths: High exploration<br/>Weaknesses: Low efficiency<br/>Risk: Resource drain]
    
    Eval1 --> Weight1[Weight by Context<br/>Early phase: 0.6<br/>Mid phase: 0.3<br/>Late phase: 0.3]
    Eval2 --> Weight2[Weight by Context<br/>Early phase: 0.3<br/>Mid phase: 0.5<br/>Late phase: 0.4]
    Eval3 --> Weight3[Weight by Context<br/>Early phase: 0.1<br/>Mid phase: 0.2<br/>Late phase: 0.3]
    
    Weight1 --> AggRV[Aggregate R_V Score<br/>R_V_total = Σ wᵢ × R_Vᵢ<br/>Plus cross-path synergies]
    Weight2 --> AggRV
    Weight3 --> AggRV
    
    AggRV --> CheckP2{P₂ Homeostasis<br/>Acceptable?<br/>≥ 0?}
    
    CheckP2 -->|No - Over-optimized| Crisis[CRISIS MODE<br/>P₂ < 0 indicates brittle system<br/>Force immediate rebalancing]
    CheckP2 -->|Yes - Balanced| CheckP3{P₃ Resources<br/>Sustainable?<br/>> 0.2?}
    
    Crisis --> ForceBalance[Force Secondary Path<br/>Sacrifice efficiency for<br/>homeostasis restoration]
    
    CheckP3 -->|No - Depleted| Conserve[Resource Conservation<br/>Reduce exploration<br/>Focus on efficiency]
    CheckP3 -->|Yes - Adequate| SelectPath[Select Optimal Path<br/>for Next Cycle]
    
    ForceBalance --> SelectPath
    Conserve --> SelectPath
    
    SelectPath --> Decision{Which Path<br/>Maximizes R_V?}
    
    Decision -->|Primary Best| NextP1[Resume Primary Path<br/>High efficiency focus<br/>BUT schedule RC check]
    Decision -->|Secondary Best| NextP2[Resume Secondary Path<br/>Maintain balance<br/>Standard MRP frequency]
    Decision -->|Tertiary Best| NextP3[Resume Tertiary Path<br/>Validate discoveries<br/>Plan integration]
    
    NextP1 --> Log[Log Decision Trail<br/>Store: R_V scores<br/>Store: Inversion results<br/>Store: F_DUDS count<br/>Store: Path weights]
    NextP2 --> Log
    NextP3 --> Log
    
    Log --> Audit{External Audit<br/>Triggered?}
    
    Audit -->|Yes - Random Check| External[External Verification<br/>Human review of MRP logs<br/>Confirm genuine exploration<br/>Validate P₂ assessment]
    Audit -->|No - Continue| Start
    
    External --> AuditPass{Audit<br/>Passed?}
    
    AuditPass -->|Yes| Start
    AuditPass -->|No - Gaming Detected| Override[OVERRIDE MODE<br/>External auditor forces<br/>path correction]
    
    Override --> Start
    
    style Start fill:#e1f5e1
    style MRP1 fill:#fff4e6
    style MRP2 fill:#fff4e6
    style MRP3 fill:#fff4e6
    style Compare fill:#e3f2fd
    style Crisis fill:#ffebee
    style SelectPath fill:#f3e5f5
    style Log fill:#e8f5e9
    style External fill:#fce4ec