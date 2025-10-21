from pprint import pprint


class Entity:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.attributes = {}

    def __str__(self):
        return f"{self.type} at ({self.x}, {self.y})"


class Plant(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, "Plant")
        self.attributes["health"] = 10
        self.attributes["size"] = 1


class WaterSource(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, "WaterSource")


class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)
        self.grid[entity.y][entity.x] = entity

    def remove_entity(self, entity):
        self.entities.remove(entity)
        self.grid[entity.y][entity.x] = None

    def get_current_state(self):
        state = []
        for entity in self.entities:
            state.append([entity.type, entity.attributes, entity.x, entity.y])

        return state

    def simulate(self):
        for entity in self.entities:
            if isinstance(entity, Plant):
                nearby_water = any(
                    isinstance(e, WaterSource)
                    for e in self.entities
                    if e.x == entity.x and e.y == entity.y - 1
                )
                if nearby_water:
                    entity.attributes["health"] += 1
                    entity.attributes["size"] += 0.1
                else:
                    entity.attributes["health"] -= 1
                    entity.attributes["size"] -= 0.1

                if entity.attributes["health"] <= 0:
                    self.remove_entity(entity)

    def print_grid(self):
        for row in self.grid:
            for cell in row:
                if cell:
                    print(cell, end=" ")
                else:
                    print("-", end=" ")
            print()


# Create a 10x10 environment

initial_states = [
    [
        Plant(3, 3),
        WaterSource(3, 2),
    ],
    [Plant(3, 3), WaterSource(5, 5)],
]

for entities in initial_states:
    print("Start simulation.")

    env = Environment(10, 10)
    for entity in entities:
        env.add_entity(entity)

    for i in range(3):
        env.simulate()
        state = env.get_current_state()
        print(f"Step {i + 1}:", str(state))
    print("### End simulation. ### \n\n")
