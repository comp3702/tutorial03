from typing import Tuple


class GridNode:
    def __init__(self, state: Tuple[int, int], actions: Tuple):
        self.state = state
        self.actions = actions


class GridNodeWithCost(GridNode):
    def __init__(self, state: Tuple[int, int], actions: Tuple, cost: int, heuristics_cost: int = 0):
        super().__init__(state, actions)

        self.cost = cost
        self.cost_for_heap_sorting = self.cost + heuristics_cost

    def __lt__(self, other):
        # this makes the difference between the official results
        # the return True which affects the sorting of the Heap
        if self.cost_for_heap_sorting != other.cost_for_heap_sorting:
            return self.cost_for_heap_sorting < other.cost_for_heap_sorting
        else:
            return self.actions[len(self.actions) - 1] < other.actions[len(other.actions) - 1]
