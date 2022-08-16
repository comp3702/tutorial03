from typing import Tuple

from src.sliding_puzzle import SlidingPuzzle, BLANK


# h1 from page 115 Russel & Norvig
def mismatches_heuristics(env: SlidingPuzzle, state: Tuple[Tuple[int, ...], ...], goal: Tuple[Tuple[int, ...], ...]) -> int:
    mismatched = 0
    for row_ind, row in enumerate(state):
        goal_row = goal[row_ind]
        for col_ind, tile in enumerate(row):
            goal_tile = goal_row[col_ind]
            if goal_tile != tile and tile != BLANK: # blank not included see h1 page 115 Russel & Norvig
                mismatched += 1

    return mismatched

# h2 from page 116 Russel & Norvig
def manhattan_distance_heuristics(env: SlidingPuzzle, state: Tuple[Tuple[int, ...], ...], goal: Tuple[Tuple[int, ...], ...]) -> int:
    manhattan_distance = 0
    for row_ind, row in enumerate(state):
        for col_ind, tile in enumerate(row):
            if tile != BLANK:
                goal_position = env.find_tile(goal, tile)
                manhattan_distance += abs(goal_position[0] - row_ind) + abs(goal_position[1] - col_ind)

    return manhattan_distance
