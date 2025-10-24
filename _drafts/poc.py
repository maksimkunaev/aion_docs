"""
Minimal POC: State-based reasoning
"""

from pprint import pprint


# === Define entities ===
entities = {
    "alice": {"type": "person"},
    "house": {"type": "area"},
    "garden": {"type": "area"},
}

# === Define relationships (initial state) ===
relationships = [
    ("alice", "in", "house"),
]

# === Define world state ===
world_state = {
    "alice": {"pos_x": 5},
    "house": {"pos_x": 5},
    "garden": {"pos_x": 10},
}

# === Define rules ===
RULES = {
    "move": lambda subject, target, state: {
        **state,
        subject: {**state[subject], "pos_x": state[target]["pos_x"]},
    }
}


def apply_action(state, action_name, subject, target):
    """Apply action rule to state"""
    if action_name not in RULES:
        return state, False, f"Unknown action: {action_name}"

    if subject not in state or target not in state:
        return state, False, "Subject or target not in state"

    new_state = RULES[action_name](subject, target, state)
    return new_state, True, f"{subject} moved to {target}"


# === Store experiences ===
EXPERIENCES = [
    {
        "action": "move",
        "states": [
            {"alice": {"pos_x": 5}, "garden": {"pos_x": 10}, "house": {"pos_x": 5}},
            {"alice": {"pos_x": 10}, "garden": {"pos_x": 10}, "house": {"pos_x": 5}},
        ],
    },
    {
        "action": "take",
        "states": [
            {
                "alice": {"posession_x": 5},
                "garden": {"posession_x": 10},
                "house": {"posession_x": 5},
            },
            {
                "alice": {"posession_x": 10},
                "garden": {"posession_x": 10},
                "house": {"posession_x": 5},
            },
        ],
    },
]


# === Planning / Goal achievement ===
def analyse_relationships(state):
    """Extract relationships from state"""
    relationships = []

    entities_list = list(state.keys())
    for i, entity_a in enumerate(entities_list):
        for entity_b in entities_list:
            if entity_a != entity_b:
                # Check if they have same position
                if state[entity_a].get("pos_x") == state[entity_b].get("pos_x"):
                    relationships.append((entity_a, "in", entity_b))

    return relationships


def find_experience(goal_state, experiences):
    """Find experience that achieves goal"""
    for experience in experiences:
        action = experience["action"]
        states = experience["states"]
        final_state = states[-1]

        relationships = analyse_relationships(final_state)

        if goal_state in relationships:
            return experience

    return None


# === Execute ===
print("=== Initial State ===")
print(f"Relationships: {relationships}")
pprint(world_state)
print()

# Apply: alice move to garden
new_state, success, reason = apply_action(world_state, "move", "alice", "garden")

print("=== Action: move alice to garden ===")
print(f"Success: {success}")
print(f"Reason: {reason}\n")

print("=== New State ===")
pprint(new_state)
print()

# === Planning ===
question = "How can Alice reach the garden?"
goal = ("alice", "in", "garden")

print(f"=== Question: {question} ===")
print(f"Goal state: {goal}\n")

relevant_experience = find_experience(goal, EXPERIENCES)

if relevant_experience:
    print(f"✓ Found relevant experience: action '{relevant_experience['action']}'")
    print(f"  Initial state: {relevant_experience['states'][0]}")
    print(f"  Final state: {relevant_experience['states'][1]}")
else:
    print("✗ No relevant experience found")
