import time
from queue import Queue
from typing import Tuple

from src.grid_node import GridNode
from src.grid_world import GridWorld


def breadth_first_search(env: GridWorld, start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[int, ...]:
    t0 = time.time()

    visited = set[Tuple[int, int]]()

    q: Queue[GridNode] = Queue()
    q.put(GridNode(start, ()))

    while not q.empty():
        node = q.get()

        if node.state == goal:
            print(f"Found the goal in {len(node.actions)} steps and {time.time() - t0}s")
            return node.actions

        for action in env.actions(node.state):
            new_state = env.step(action, node.state)
            if new_state not in visited:
                visited.add(new_state)
                q.put(GridNode(new_state, node.actions + (action,)))

    print(f"No solution found in {time.time() - t0}s!")
    return ()
