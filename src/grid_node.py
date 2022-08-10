from typing import Tuple


class GridNode:
    def __init__(self, state: Tuple[int, int], actions: Tuple):
        self.state = state
        self.actions = actions


class GridNodeWithCost(GridNode):
    def __init__(self, state: Tuple[int, int], actions: Tuple, cost: int):
        super().__init__(state, actions)

        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
