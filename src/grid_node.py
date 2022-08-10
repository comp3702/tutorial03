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
        # this makes the difference between the official results
        # the return True which affects the sorting of the Heap
        if self.cost != other.cost:
            return self.cost < other.cost
        else:
            return self.actions[len(self.actions) - 1] < other.actions[len(other.actions) - 1]
