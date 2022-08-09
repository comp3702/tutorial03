from typing import Optional, Tuple

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

actions = {
    LEFT: 'L',
    RIGHT: 'R',
    UP: 'U',
    DOWN: 'D'
}

class GridWorld:
    def __init__(self, start: Tuple[int, int] = (8, 0), goal: Tuple[int, int] = (0, 8),
                 obstacles: Optional[Tuple[Tuple]] = None, costs: Optional[Tuple[Tuple]] = None):
        self.start = start
        self.goal = goal

        self.current_row = start[0]
        self.current_col = start[1]

        if obstacles:
            self.obstacles = obstacles
        else:
            self.obstacles = (
                (0, 0, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 1, 1, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 0)
            )
        self.last_row = len(self.obstacles) - 1
        self.last_col = len(self.obstacles[0]) - 1

        if costs:
            self.costs = costs
        else:
            self.costs = (
                (1, 1, 1, 5, 5, 5, 5, 1, 1),
                (1, 1, 1, 5, 5, 5, 5, 1, 1),
                (1, 1, 10, 10, 10, 10, 10, 1, 1),
                (1, 1, 1, 10, 10, 10, 10, 1, 1),
                (1, 1, 1, 1, 1, 10, 10, 1, 1),
                (1, 1, 1, 1, 1, 10, 10, 1, 1),
                (1, 1, 1, 1, 10, 10, 10, 1, 1),
                (1, 1, 1, 10, 10, 10, 10, 1, 1),
                (1, 1, 1, 1, 1, 1, 1, 1, 1)
            )

    def actions(self):
        actions = list[int]()

        if self.current_col > 0 and self.obstacles[self.current_row][self.current_col - 1] != 1:
            actions.append(LEFT)
        if self.current_col < self.last_col and self.obstacles[self.current_row][self.current_col + 1] != 1:
            actions.append(RIGHT)
        if self.current_row > 0 and self.obstacles[self.current_row - 1][self.current_col] != 1:
            actions.append(UP)
        if self.current_row < self.last_row and self.obstacles[self.current_row + 1][self.current_col] != 1:
            actions.append(DOWN)

        return actions
