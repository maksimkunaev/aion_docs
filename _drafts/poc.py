"""
Minimal POC: State-based reasoning
Matches your pseudocode exactly
"""

from copy import deepcopy
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
    "alice": {"pos": 5},
    "house": {"pos": 5},
    "garden": {"pos": 10},
}

# === Define rules ===
RULES = {
    "move": lambda subject, target, state: {
        **state,
        subject: {**state[subject], "pos": state[target]["pos"]},
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


# === Execute ===
print("=== Initial State ===")
print(f"Relationships: {relationships}")
print(f"World state: {world_state}\n")

# Apply: alice move to garden
new_state, success, reason = apply_action(world_state, "move", "alice", "garden")

print(f"=== Action: move alice to garden ===")
print(f"Success: {success}")
print(f"Reason: {reason}\n")

print(f"=== New State ===")

states = [world_state, new_state]
pprint(states)
# print(f"World state: {new_state}")
# print(f"Alice pos: {new_state['alice']['pos']} (same as garden: {new_state['garden']['pos']})")
