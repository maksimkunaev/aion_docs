# Implementation Roadmap (Mock / Not Final): POC Reasoning System

> **Status:** Exploratory. This is a proposed implementation plan, not an executed roadmap. Shared as reference for building similar systems.

---

## Goal

Prove that a system can solve multi-step reasoning tasks by predicting world states using a minimal ontology and simple text input.

---

## Phase 0: Setup (1-2 days)

- [ ] Choose primary approach (simulation-based vs LLM-based)
- [ ] Define minimal ontology (entities, properties, relationships, actions)
- [ ] Write 3-5 test questions of varying difficulty (easy, medium, hard)

---

## Phase 1: Toy Scenario Definition (2-3 days)

**Scenario: "Alice and the Apple Tree"**

**Initial State** (extracted from text):
- Alice in garden, hungry (energy=0)
- Apple tree with 5 apples (count=5)
- Path from Alice to tree (distance=3 steps)

**Goal:** Alice collects all apples and becomes full (energy=5)

**Example Questions:**
- **Easy:** "Where is Alice? How many apples are on the tree?"
- **Medium:** "What will happen if Alice walks to the tree?"
- **Hard:** "How can Alice collect all apples? How many steps does it take?"

---

## Phase 2: Implement State Prediction (3-5 days)

**Option A: Simulation-First** (recommended)
- [ ] Write simple state engine (State → Action → NewState)
- [ ] Code 5-10 rules (walk_towards, pick_up, eat, etc.)
- [ ] Generate 100-200 trajectories (state sequences)

**Option B: LLM-Based**
- [ ] Parser: text → structured state
- [ ] LLM as predictor: (state + action) → next state
- [ ] Train on 100-200 examples or use in-context learning

**Recommendation:** Start with Option A (simpler, clearer). Then compare with Option B.

---

## Phase 3: Build Query Answering (2-3 days)

- [ ] Question parser (extract: subject, predicate, question_type)
- [ ] Routing logic: question type → reasoning algorithm
  - **Retrieval:** search current state
  - **Prediction:** simulate → find answer
  - **Planning:** backward search from goal

- [ ] Implement answering for all 3 question types

---

## Phase 4: Test & Validate (2-3 days)

- [ ] Run all test questions, verify answer correctness
- [ ] Test with new state configurations (vary initial conditions)
- [ ] Confirm: system reasons, not memorizes

---

## Phase 5: Demo & Documentation (1-2 days)

- [ ] Write end-to-end example
- [ ] Visualize state transitions (text or ASCII grid)
- [ ] Document architecture (how the black box works)

---

## Success Criteria

✅ System answers all 9 test questions (3 easy + 3 medium + 3 hard)  
✅ Answers are logically consistent with each other  
✅ When initial state changes, answers update correctly  
✅ Can display reasoning chain (state1 → action → state2)  

---

## Time Estimate

**Total: ~2 weeks** (focused work)

---

## Key Decision

**Approach Choice:**
- **Simulation (Option A):** Faster POC, clearer architecture, can migrate to LLM later
- **LLM (Option B):** Looks more "magical," but requires training data and harder to debug

**Recommendation:** **Start with Option A**. Get working POC in 1 week. Then experiment with Option B in parallel.

---

## Why This Approach

1. **Simulation** isolates the reasoning problem from language model training
2. **Minimal ontology** makes the system understandable and debuggable
3. **Explicit state transitions** allow verification of reasoning chains
4. **Incremental difficulty** (easy → medium → hard) helps identify failure modes
5. **Clear success criteria** prevent endless iteration

---

## Alternative Path: LLM-First

If you prefer the LLM-based approach:

1. Use a smaller model (Llama 2, Gemma) for faster iteration
2. Generate synthetic training data (state transitions created by simulation)
3. Start with in-context learning (few-shot examples in prompt)
4. Only fine-tune if in-context fails
5. Validate against simulation as ground truth

---

## Lessons from Experiments

From earlier attempts documented in `06-experiments-postmortem.md`:

- ❌ Direct text → coordinates doesn't work (LLMs struggle with spatial math)
- ✅ Symbolic state representations work better
- ✅ Relative relationships (near, above) > absolute coordinates
- ⚠️ Training data generation is the bottleneck

Apply these to avoid repeating mistakes.