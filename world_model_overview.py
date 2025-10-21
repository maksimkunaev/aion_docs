import pprint
from text_parser import TextParser


class WorldModel:
    def __init__(self):
        self.state = []

    def initialize(self, entities, relationships):
        self.state = [
            {"name": "Farmer", "coordinates": [0, 0]},
            {"name": "garden", "coordinates": [3, 3]},
        ]
        return self.state


class Simulator:
    # THIS will be prgrammable, (not NN)
    # or changed later
    # the idea of creating a CommonSense Physics Engine is to make this engine learns what rules apply when.
    # The actual Simulator can be implemented separately from WM and Parser
    def apply_action(self, initial_state, action):
        event_type = action["event"]  # 'MOVE'
        event_parameters = action["parameters"]  # ['Farmer', '', 'garden']

        if event_type == "MOVE":
            return [
                {"name": "Farmer", "coordinates": [0, 0]},
                {"name": "Farmer", "coordinates": [3, 3]},
            ]

        if event_type == "GROW":
            return [
                {"name": "Tree", "size": 0.1},
                {"name": "Tree", "size": 0.3},
            ]
        return []


parser = TextParser("gemma2-9b-it")
wm = WorldModel()
simulator = Simulator()

text = "Farmer moves to garden. Tree grows"
parsed = parser.parse_text(text)

print("Parsed Input Text:")
pprint.pprint(parsed)

entities = parsed["entities"]
relationships = parsed["static_relations"]
actions = parsed["actions"]


initial_state = wm.initialize(entities, relationships)
print("\nWM intial state:")
pprint.pprint(initial_state)


combined_states = []

for action in actions:
    transition_states = simulator.apply_action(initial_state, action)
    combined_states.append({"action": action, "transition_states": transition_states})

print("\nWorld States:")
pprint.pprint(combined_states)


###
#     ~/pr/noesis    main ⇡2 !18 ?4  python test_wm.py       ✔  private 
# Parsed Input Text:
# {'actions': [{'event': 'MOVE', 'parameters': ['Farmer', '', 'garden']},
#              {'event': 'GROW', 'parameters': ['Tree', '', '']}],
#  'entities': {'Farmer': {'name': 'Farmer', 'properties': {}, 'type': 'PERSON'},
#               'Tree': {'name': 'Tree', 'properties': {}, 'type': 'PLANT'},
#               'garden': {'name': 'garden', 'properties': {}, 'type': 'AREA'}},
#  'static_relations': []}

# WM intial state:
# [{'coordinates': [0, 0], 'name': 'Farmer'},
#  {'coordinates': [3, 3], 'name': 'garden'}]

# World States:
# [{'action': {'event': 'MOVE', 'parameters': ['Farmer', '', 'garden']},
#   'transition_states': [{'coordinates': [0, 0], 'name': 'Farmer'},
#                         {'coordinates': [3, 3], 'name': 'Farmer'}]},
#  {'action': {'event': 'GROW', 'parameters': ['Tree', '', '']},
#   'transition_states': [{'name': 'Tree', 'size': 0.1},
#                         {'name': 'Tree', 'size': 0.3}]}]
