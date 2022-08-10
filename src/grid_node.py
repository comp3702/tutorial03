from typing import Tuple


class GridNode:
    def __init__(self, state: Tuple[int, int], actions: Tuple):
        self.state = state
        self.actions = actions
