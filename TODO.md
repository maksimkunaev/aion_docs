# TODO: Common Sense Reasoning Engine

## Priority 1: Rule Learning
- [ ] Extract rules from state transition sequences
  - Input: `{alice: pos_x=5} → {alice: pos_x=10}` paired with `{bob: pos_x=3} → {bob: pos_x=8}`
  - Output: Generalized rule `move(X, target) := X.pos = target.pos`
  - Generalization test: Apply to unseen entity (charlie)

- [ ] Learn rules for 3+ action types (move, take, drop)
  - Each action learns different transformation pattern
  - Verify: Not memorizing, actual generalization

## Priority 2: State Matching
- [ ] Build flexible state matching (not exact dict comparison)
  - Current: fails if `pos_x` differs by 1
  - Fix: Match relevant properties, ignore noise
  - Test: Match similar states with variations

## Priority 3: Variable Concept Counts
- [ ] System works with any number of concepts
  - 2 concepts (alice, garden) → works
  - 5 concepts (alice, bob, garden, house, tree) → works
  - 20 concepts → works
  - No hardcoding entity types

## Priority 4: Pattern Detection
- [ ] Detect patterns in state sequences (growth, decay, movement, etc)
  - Input: sequence `[{size: 1}, {size: 1.5}, {size: 2}]`
  - Output: Detected pattern = "growth"
  
- [ ] Classify new sequences by detected patterns
  - Given unseen sequence, identify which pattern it matches

## Priority 5: Multi-step Planning
- [ ] Extend planner from 1-step to N-step sequences
  - Current: "alice move to garden"
  - Target: "alice move to tree → climb tree → take apple"

- [ ] Chain learned rules to reach goal state

## Priority 6: Validation
- [ ] Test on reasoning test suite
  - Causal: "Why did X happen?"
  - Planning: "How to achieve goal Y?"
  - Spatial: "Where is alice relative to bob?"

- [ ] Document what works / fails