# Common Sense Engine

## Project on Building a Causal Reasoning System

### Project Overview

**Common Sense Engine** is an experimental system designed to create AI capable of **causal reasoning** and **understanding basic physical world dynamics** without relying on formal models. The project addresses a key limitation of current large language models (LLMs): their lack of understanding of simple physical laws and cause-effect relationships.

### Problem Statement

Modern language models can generate impressive text but often fail to understand fundamental physical principles:

* Glasses fall but do not break.
* People float upward.
* Objects pass through walls.
* Basic causal chains are violated.

This happens because models learn from text where obvious facts are not explicitly mentioned. For example, in “the glass shattered,” the cause (it fell) is implied, not written.

### Core Philosophy

The project is based on the idea that **intelligence emerges through experience**, not formal logic—similar to how animals, early humans, or R2D2 learn. The system should *feel* the world through internal state models rather than *know* it through symbolic rules.

---

## System Architecture

### Concept

The world is represented as a sequence of states over time:

```
[State1] → [Action] → [State2] → [Action] → [State3] → ...
```

Each state includes:

* **Entities** — objects in the world
* **Properties** — object attributes
* **Relationships** — links between objects
* **Actions** — operations that change states

### Modular Pipeline

```
Text Input → [Text Parser] → [World Model] → [Action Pattern Generator] → [Cause-Effect Engine] → Reasoning Output
```

---

## System Components

### 1. Text Parser

**Purpose:** extract structured representations from natural language.

**Input:** raw text
**Output:** partial world model

**Example:**

```
Input: "Alice sat on the bank next to her sister"
Output: 
{
  "entities": ["Alice", "bank", "sister"],
  "relations": ["Alice-on-bank", "Alice-next-to-sister"]
}
```

**Technical details:**

* Uses an LLM to extract entities and relations.
* Employs finite dictionaries of object types.
* Builds a base relation graph.

---

### 2. World Model

**Purpose:** expand partial scene representations into complete ones on demand.

**Concept:**

* *Partial model:* “Alice is next to her sister.”
* *Complete model:* all possible relationships between scene entities.

**Query types:**

* `select(entity_set)` — get all relations among selected entities
* `expand_context(entity)` — get full context of an entity
* `get_relation(A, B)` — return specific relation

**Example:**

```
Query: ["Alice", "bank", "sister", "book"]
Response: [
  {"Alice": "near-sister"},
  {"sister": "holding-book"}, 
  {"Alice": "on-bank"},
  {"book": "on-bank"},
  {"sister": "on-bank"}
]
```

**Base spatial predicates:**

* `near(A, B)` — proximity
* `between(A, B, C)` — positional relation
* `inside(A, B)` — containment
* `moved_from(A, B)` — motion origin
* `moved_to(A, B)` — motion destination

---

### 3. Action Pattern Generator

**Purpose:** generate micro-state sequences for actions.

**Functions:**

* Decompose actions into fine-grained steps.
* Build chains: `State1 → State2 → State3`.
* Operate without absolute coordinates.

**Example:**

```
Action: "Rabbit runs to the rabbit hole"
Pattern:
[
  {"Rabbit": "near-Alice"},
  {"Rabbit": "on-field"}, 
  {"Rabbit": "near-rabbit-hole"}
]
```

---

### 4. Cause-Effect Engine

**Purpose:** perform reasoning over state models.

**Types of reasoning:**

1. **Forward prediction** — State + Action → New State
2. **Backward inference** — Effect → possible Causes
3. **Counterfactuals** — “What if” scenarios
4. **Planning** — Goal → Action sequence

---

## Levels of Reasoning

### Six core reasoning types

1. **Retrieval** — direct state lookup
2. **Conditional retrieval** — query with conditions
3. **Temporal reasoning** — reasoning over time
4. **Comparative/quantitative** — comparison and counting
5. **Causal reasoning** — cause-effect chains
6. **Planning** — goal-oriented sequencing

### Two-level reasoning model

* **Level 1:** simple rule-based IF–THEN patterns
* **Level 2:** contextual reasoning via LLM assistance

---

## Data Formats

### State

```json
{
  "timestamp": "t1",
  "entities": {
    "Alice": {
      "type": "Person",
      "location": "bank",
      "properties": ["sitting"],
      "relations": {"near": "sister"}
    },
    "sister": {
      "type": "Person", 
      "location": "bank",
      "activity": "reading"
    }
  }
}
```

### Action

```json
{
  "action": "move",
  "agent": "Alice",
  "target": "rabbit_hole",
  "parameters": {
    "method": "running",
    "path": "field"
  }
}
```

### Cause-Effect Rule

```json
{
  "if": {"entity_type": "Glass", "action": "falls"},
  "then": {"entity.state": "broken"}
}
```

---

## Development Stages

### Stage 1: Pattern Generation

**Goal:** teach the system to parse actions into state chains.

**Tasks:**

* Implement the Text Parser.
* Build a pattern base for common actions.
* Train on simple physical examples.

**Test case:**

```
"Glass fell" → [
  {"Glass": "on-table"},
  {"Glass": "falling"}, 
  {"Glass": "on-floor", "state": "broken"}
]
```

---

### Stage 2: Cause-Effect Reasoning

**Goal:** enable effect prediction and action planning.

**Tasks:**

* Construct a cause-effect knowledge base.
* Implement the Cause-Effect Engine.
* Add counterfactual reasoning.

**Test case:**

```
Question: "What happens if Alice runs after the rabbit?"
Answer: generates a sequence showing Alice moving.
```

---

## Data and Training

### The Data Gap

**Problem:** obvious causal knowledge is rarely written in text.

**Solutions:**

1. **Manual generation (100–300 samples)**

   * Build a reference kernel of core relations.
   * Standardize the data format.

2. **Template generation**

   * Entity(type) + Action + Effect.
   * Combine entities and actions systematically.

3. **Extraction from procedural texts**

   * Recipes, manuals, game scripts.

4. **LLM pre-generation**

   * Use LLMs to synthesize base patterns.
   * Apply filtering afterward.

**Sample cause-effect pairs:**

```
Fell → landed on the ground  
Drank water → quenched thirst  
Turned on light → became bright  
Broke glass → shards appeared  
Opened door → passage became available
```

---

## System Testing

### Case Study: *Alice in Wonderland*

**Scenario:**

```
"Alice sat on the bank beside her sister, who was reading a book. 
A rabbit ran past her toward a rabbit hole."
```

**Test types:**

1. **Direct query:** “Why did Alice get bored?”
2. **Hidden cause:** “Why did she look into the book?”
3. **Counterfactual:** “What if the book had pictures?”
4. **Inverse reasoning:** “What caused the rabbit’s appearance?”

**Final test:**

```
Question: "What happens if Alice stands up and runs after the rabbit?"
Expected output: movement sequence for Alice.
Follow-up: "How many people remain on the bank?"
Answer: "One" (her sister).
```

---

## Technical Features

### LLM Integration

* **Parsing:** extract structures from text.
* **Context expansion:** fill missing world details.
* **Pattern generation:** synthesize micro-state sequences.
* **Typing format:** `[Alice:Person]` for explicit entity tagging.

### No Absolute Coordinates

**Instead of:** `x: 10, y: 15`
**Use:** `near(Alice, sister)`, `between(Alice, bank, hole)`

**Benefits:**

* Easier learning.
* Better generalization.
* No dependency on numeric data.

### Modularity

Each module evolves independently:

* Parser upgrades independently.
* World Model can expand.
* Reasoning Engine can retrain.

---

## Future Roadmap

### Short-term

* [ ] Implement Text Parser
* [ ] Build World Model with 50 relations
* [ ] Action Pattern Generator for 10 actions
* [ ] Test on *Alice in Wonderland* scenes

### Mid-term

* [ ] Expand to 1000+ causal rules
* [ ] Integrate external knowledge sources
* [ ] Train on large text corpora
* [ ] Add temporal reasoning

### Long-term

* [ ] Full-scale reasoning engine
* [ ] Robotics integration
* [ ] Application to simulated game worlds
* [ ] Scaling to complex scenarios

---

## Conclusion

**Common Sense Engine** introduces a new paradigm for building AI systems capable of *natural understanding* of the world through **empirical experience** rather than **formal logic**. The project is currently in the MVP phase and shows promise in addressing the core challenge of physical reasoning in modern AI.

**Key innovations:**

* Representing the world as temporal state sequences.
* Modular architecture for flexible reasoning.
* Relative spatial representation instead of coordinates.
* Two-level causal reasoning model.

The project is open to collaboration and further research toward developing AI systems with genuine understanding of the physical world.
