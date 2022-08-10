import time
from collections import deque
from typing import Tuple, Set, Deque

from src.grid_node import GridNode
from src.grid_world import GridWorld


def depth_limited_search(env: GridWorld, start: Tuple[int, int], goal: Tuple[int, int], limit: int):
    t0 = time.time()

    visited: Set[Tuple[int, int]] = set()

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
            if new_state not in visited:
                visited.add(new_state)
                stack.append(GridNode(new_state, node.actions + (action,)))
                nodes_generated += 1

    print(f"Solution not found in {time.time() - t0}s. Visited {len(visited)} nodes and generated {nodes_generated}")
    return ()