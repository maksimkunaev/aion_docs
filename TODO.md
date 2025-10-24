# TODO List: From Idea to Working Proof

**State-based decomposition is the scaffolding, not the goal**. Here's what needs to happen:

## Phase 1: Learning (Can the system learn rules?)
- [ ] **Build rule learner from state sequences**
  - Input: 10-20 observed state transitions (e.g., alice pos 5→10, garden pos 10)
  - Output: Inferred rule (e.g., "move(X, Y) makes X.pos = Y.pos")
  - Success: System generalizes to new entities/locations not in training

- [ ] **Test on 3 different action types**
  - Move, take, drop (or similar)
  - Show it learns different patterns, not memorizing

## Phase 2: Concept Formation (How does the system abstract?)
- [ ] **Build symbol grounding from sensor data (simulated)**
  - Input: Noisy observations (pixel grid, point cloud, etc.)
  - Output: Discrete symbols (alice, garden, box)
  - Success: Works on data it hasn't seen (generalization test)

- [ ] **Build concept detector from sequences**
  - Input: State sequence showing growth/decay/change
  - Output: New concept name (e.g., "ripening" from color changes)
  - Success: Labels new instances correctly

## Phase 3: Reasoning Integration
- [ ] **Combine learned rules + grounded concepts**
  - Your POC uses hardcoded rules
  - Replace with: learned rules + learned concepts
  - Success: Still solves the planning problem

- [ ] **Test on 1 multi-step scenario**
  - Not just "move alice to garden"
  - Something like: "Get apple from tree" (move + climb + take)
  - Success: Plans multi-step sequence correctly

## Phase 4: Validation
- [ ] **Run on reasoning test suite**
  - Take your hallucination test examples
  - Show it answers correctly (or fails predictably)
  - Document what it CAN and CANNOT do

---

## Critical unknowns to resolve first

Before coding, answer these:

1. **Concept formation approach?**
   - Clustering raw observations?
   - LLM-assisted annotation?
   - Hand-designed feature extractors?

2. **Rule learning method?**
   - Inductive logic programming?
   - Symbolic regression?
   - Neural network + interpretation?
   - Simple pattern matching?

3. **Sensor data → symbols bridge?**
   - Simulated images → coordinates?
   - Simulated point clouds?
   - Or just synthetic state sequences?

Pick **ONE** for each. Don't try all at once.

---

## Minimal viable path (2-3 weeks)

1. **Week 1:** Rule learner (Phase 1)
   - Hardcode 5 action examples
   - Build learner to infer 1 rule type
   - Test generalization

2. **Week 2:** Concept grounding (Phase 2)
   - Simulate "observation → symbol" pipeline
   - Build simple detector (e.g., color threshold → "apple")
   - Show it labels new images

3. **Week 3:** Integration + validation
   - Plug learned rules + grounded concepts into your POC
   - Run test suite
   - Document success/failure modes

---

**Which one should you start with?** Rule learning is easier and unblocks everything else.