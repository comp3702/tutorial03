import time
from collections import deque
from typing import Tuple, Set, Deque, Dict, Optional

from src.grid_node import GridNode
from src.grid_world import GridWorldWithObstacles


def depth_limited_search(env: GridWorldWithObstacles, start: Tuple[int, int], goal: Tuple[int, int], max_depth: int) -> Optional[Tuple[int, ...]]:
    t0 = time.time()

    # to allow revisiting of nodes found with fewer steps
    visited: Dict[Tuple[int, int], int] = {}

    stack: Deque[GridNode] = deque()
    stack.append(GridNode(start, ()))

    nodes_generated = 0

    while stack:
        node = stack.pop()
        if node.state == goal:
            print(f"Found the goal in {len(node.actions)} steps and {time.time() - t0}s. Visited {len(visited)} nodes and generated {nodes_generated}")
            return node.actions

        for action in env.actions(node.state):
            new_state = env.step(action, node.state)
            if (new_state not in visited.keys() or visited[new_state] > len(node.actions) + 1) and len(node.actions) + 1 < max_depth:
                visited[new_state] = len(node.actions) + 1
                stack.append(GridNode(new_state, node.actions + (action,)))
                nodes_generated += 1

    return None


def iterative_deepening_search(env: GridWorldWithObstacles, start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[int, ...]:
    for max_depth in range(1000):
        actions = depth_limited_search(env, start, goal, max_depth)
        if actions:
            return actions
