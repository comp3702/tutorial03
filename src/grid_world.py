from abc import abstractmethod, ABC
from typing import Optional, Tuple

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

ACTIONS = {
    LEFT: 'L',
    RIGHT: 'R',
    UP: 'U',
    DOWN: 'D'
}


class GridWorld(ABC):
    def __init__(self):
        self.last_row = 0
        self.last_col = 0

    @abstractmethod
    def actions(self, position: Tuple[int, int]):
        pass

    def step(self, action: int, position: Tuple[int, int]) -> Tuple[int, int]:
        current_row = position[0]
        current_col = position[1]

        if action == UP:
            current_row -= 1
        elif action == DOWN:
            current_row += 1
        elif action == LEFT:
            current_col -= 1
        elif action == RIGHT:
            current_col += 1

        if current_row < 0 or current_col < 0 or current_row > self.last_row or current_col > self.last_col:
            raise Exception(f"Fell off the grid! At position {current_row}x{current_col}")

        return current_row, current_col


class GridWorldWithObstacles(GridWorld):
    def __init__(self, obstacles: Optional[Tuple[Tuple]] = None):
        super().__init__()
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

    def actions(self, position: Tuple[int, int]) -> list[int]:
        current_row = position[0]
        current_col = position[1]

        actions = list[int]()

        if current_col > 0 and self.obstacles[current_row][current_col - 1] != 1:
            actions.append(LEFT)
        if current_col < self.last_col and self.obstacles[current_row][current_col + 1] != 1:
            actions.append(RIGHT)
        if current_row > 0 and self.obstacles[current_row - 1][current_col] != 1:
            actions.append(UP)
        if current_row < self.last_row and self.obstacles[current_row + 1][current_col] != 1:
            actions.append(DOWN)

        return actions

