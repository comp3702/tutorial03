from typing import Tuple

from src.grid_world import GridWorld


def grid_world_manhattan_distance(env: GridWorld, start: Tuple[int, int], goal: Tuple[int, int]) -> int:
    return abs(goal[0] - start[0]) + abs(goal[1] - start[1])
