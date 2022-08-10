from typing import Tuple

from src.sliding_puzzle import SlidingPuzzle


def mismatches_heuristics(env: SlidingPuzzle, state: Tuple[Tuple[int, ...], ...], goal: Tuple[Tuple[int, ...], ...]) -> int:
    mismatched = 0
    for row_ind, row in enumerate(state):
        goal_row = goal[row_ind]
        for col_ind, tile in enumerate(row):
            goal_tile = goal_row[col_ind]
            if goal_tile != tile:
                mismatched += 1

    return mismatched
