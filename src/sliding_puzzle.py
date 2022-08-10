from typing import Tuple, Optional

from src.grid_world import GridWorldWithCost, DOWN, UP, RIGHT, LEFT


class SlidingPuzzle(GridWorldWithCost):
    def __init__(self, state: Optional[Tuple[Tuple[int, ...], ...]] = None):
        super().__init__()

        if state:
            self.state = state
        else:
            self.state = (
                (7, 2, 4),
                (5, 3, 6),
                (8, -1, 1)
            )
        self.last_row = len(self.state) - 1
        self.last_col = len(self.state[0]) - 1

    def find_blank(self, state: Tuple[Tuple[int, ...], ...]) -> Tuple[int, int]:
        for row_index, row in enumerate(state):
            if -1 in row:
                return row_index, row.index(-1)

    def actions(self, state: Tuple[Tuple[int, ...], ...]) -> Tuple[int, ...]:
        blank_row, blank_col = self.find_blank(state)

        actions = list[int]()

        if blank_col > 0:
            actions.append(LEFT)
        if blank_col < self.last_col:
            actions.append(RIGHT)
        if blank_row > 0:
            actions.append(UP)
        if blank_row < self.last_row:
            actions.append(DOWN)

        return tuple(actions)

    def step(self, action: int, state: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
        new_state = list(list(row) for row in state)

        blank_row, blank_col = self.find_blank(state)

        if blank_row == 0 and action == UP \
            or blank_row == self.last_row and action == DOWN \
            or blank_col == 0 and action == LEFT \
            or blank_col == self.last_col and action == RIGHT:
            raise Exception('Fell off the grid!')

        if action == UP:
            new_state[blank_row][blank_col] = new_state[blank_row - 1][blank_col]
            new_state[blank_row - 1][blank_col] = -1
        elif action == DOWN:
            new_state[blank_row][blank_col] = new_state[blank_row + 1][blank_col]
            new_state[blank_row + 1][blank_col] = -1
        elif action == LEFT:
            new_state[blank_row][blank_col] = new_state[blank_row][blank_col - 1]
            new_state[blank_row][blank_col - 1] = -1
        elif action == RIGHT:
            new_state[blank_row][blank_col] = new_state[blank_row][blank_col + 1]
            new_state[blank_row][blank_col + 1] = -1

        return tuple([tuple(row) for row in new_state])

    def cost(self, state: Tuple[Tuple[int, ...], ...]) -> int:
        return 1