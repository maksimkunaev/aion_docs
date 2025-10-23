# Common Sense Engine — Reasoning & World Models

> Exploratory research on building AI systems that understand the world through structured internal models, not just token prediction.

## The Problem

Current LLMs excel at pattern matching in text but consistently fail at:

- **Spatial reasoning** — "Alice is left of Bob" should mean Bob ≠ left of Alice
- **Causal reasoning** — Dropping a glass causes breaking, not flying upward
- **Common sense** — The obvious causes aren't stated in text, so models miss them

**Example:** A language model might generate:
> "The glass fell and floated gently into the air, where it multiplied."

This isn't random. It's because LLM training text doesn't explicitly state obvious causes ("glass is rigid → breaks not float"). Models learn patterns, not physics.

## Our Approach

Don't build one magical end-to-end model. **Separate concerns:**

```
Text → Parser → World Model → Reasoning Engine → Answer
```

Each component is simpler, debuggable, and improvable.

**Key insight:** The world has structure (entities, relationships, causality). Exploit that structure instead of trying to compress it into token embeddings.

---

## What's Inside

### Core Ideas (Read in Order)

**[01-common-sense-engine.md](01-common-sense-engine.md)** (15 min)
- Core architecture: State → Action → NewState
- Modular design: Parser, World Model, Cause-Effect Engine
- Data formats: How to represent entities, relationships, actions
- Why this matters: Separates the reasoning problem from language understanding

**[02-reasoning-hierarchy.md](02-reasoning-hierarchy.md)** (10 min)
- 10 levels of reasoning (from reflexes to meta-cognition)
- How these map to computational complexity
- Which levels our architecture aims to support

**[03-world-simulation-design.md](03-world-simulation-design.md)** (10 min)
- Concrete design for a 2D grid-based reasoning system
- How to represent observations, concepts, and knowledge
- Example: Plant grows near water (positive feedback)
- Template for building similar systems

**[04-experiment-llm-spatial-model.md](04-experiment-llm-spatial-model.md)** (15 min)
- We tested: Can LLMs directly learn spatial reasoning?
- Result: No (60% accuracy on simple spatial relations)
- Why it failed: LLMs poor at numbers, missing data forces guessing
- Lesson: This motivated the modular, state-based approach

**[05-reasoning-capability-framework.md](05-reasoning-capability-framework.md)** (10 min)
- What should a reasoning system do? 4 capability tiers:
  - Tier 1: Retrieval (facts)
  - Tier 2: Reasoning (comparisons)
  - Tier 3: Causality (why?)
  - Tier 4: Planning (how to achieve X?)
- Design tradeoffs: Why separate these concerns?

**[06-pattern-representation.md](06-pattern-representation.md)** (5 min)
- Alternative: Simplify world to numerical patterns
- When to use: Simple scenarios, fast inference
- When not to use: Complex reasoning, multi-step planning

### Experiments & Lessons

**[implementation-roadmap.md](implementation-roadmap.md)** (10 min)
- How you'd actually build this (proposed 2-week POC)
- Phase breakdown: from setup to demo
- Why simulate-first > LLM-first for POC

### Tests & Examples

**[tests-hallucination-examples.md](tests-hallucination-examples.md)**
- 10 categories of common AI failures
- Concrete examples (factual, logical, causal)
- Use to validate your reasoning system

**[tests-logic-questions.md](tests-logic-questions.md)**
- 8 logic puzzles to test reasoning
- From easy (arithmetic) to hard (spatial planning)

**[example-2d-simulation.py](example-2d-simulation.py)**
- Runnable code: 2D world with plants and water
- Demonstrates State → Action → NewState
- ~100 lines, no dependencies

**[example-pattern-detection.py](example-pattern-detection.py)**
- Runnable code: Detect apple growth/ripening/falling
- Demonstrates pattern recognition on state sequences
- Shows how to answer "did X happen?" questions

### Reference

**[REFERENCES.md](REFERENCES.md)**
- Books & papers that inform this approach
- Cognitive science (mental models, spatial reasoning)
- AI/reasoning (search, planning, causal inference)

---

## Key Findings

### ❌ What Didn't Work

1. **Direct LLM-to-world-model** — Training LLM to output coordinates: 60% accuracy. Fails because:
   - LLMs struggle with precise numbers
   - Text provides incomplete information
   - Models memorize patterns instead of learning reasoning

2. **"Complete world model" requirement** — Overkill for proving the core idea. Better to:
   - Start with minimal ontology (5-10 entities)
   - Build incrementally
   - Test each reasoning level independently

### ⚠️ What's Still Open

- **Scaling:** Does this work beyond toy 2D worlds?
- **Grounding:** How do you connect symbols to real sensor data?
- **Learning:** Can the reasoning rules be learned, not hardcoded?
- **Integration:** How does this work with LLMs for language understanding?

---

## Status

🟡 **Exploratory Phase**

- Some ideas validated through experiments
- Most untested in production
- Use as inspiration, not as blueprint

### What This Is

- Design documents & conceptual frameworks
- Failed experiments (lessons learned)
- Test cases & examples
- Roadmap for future implementation

### What This Is NOT

- Production-ready code
- Complete system
- Peer-reviewed research
- Finished ideas

---

## Who This Is For

- **People skeptical of LLM-only approaches** who want to understand why
- **Anyone interested in causal reasoning systems** looking for architecture ideas
- **Builders** who want a concrete alternative to pure language models

---

## Next Steps

Pick one idea. Build it. Measure it. Iterate.

Some concrete options:

---

## No Hype, Just Ideas

This project is honest about limitations:

- ✅ Explains what worked and what didn't
- ✅ No fake demos or overstatements
- ✅ Clear about what's exploratory vs. proven
- ✅ Separates big vision from practical steps
- ❌ Not claiming to solve AGI
- ❌ Not claiming to replace LLMs
- ❌ Not claiming production-readiness

**Collaboration welcome.** Fork, improve, build on this.

---

## License

These ideas are open. Use, modify, improve them freely.