import heapq
import time
from typing import Tuple, List, Dict

from src.grid_node import GridNodeWithCost
from src.grid_world import GridWorld, GridWorldWithCost


def a_star_search(env: GridWorldWithCost, start: Tuple[int, int], goal: Tuple[int, int], heuristics) -> Tuple[Tuple[int, ...], int]:
    t0 = time.time()

    visited: Dict[Tuple[int, int], int]= {start: 0}

    # the heap is sorted by current cost with heuristics
    # but the node only keeps the actual cost incurred
    heap = [(heuristics(env, start, goal), GridNodeWithCost(start, (), 0))]
    heapq.heapify(heap)

    nodes_expanded = 0

    while heap:
        _, node = heapq.heappop(heap)

        if node.state == goal:
            print(f"Found the goal in {len(node.actions)} steps and {time.time() - t0}s. Visited {len(visited)} nodes and expanded {nodes_expanded}")
            print(f"Path cost: {node.cost}")
            return node.actions, node.cost

        for action in env.actions(node.state):
            new_state, cost = env.step(action, node.state)
            new_cost = cost + node.cost

            if new_state not in visited.keys() or visited[new_state] > new_cost:
                visited[new_state] = new_cost
                heapq.heappush(heap, (new_cost + heuristics(env, new_state, goal), GridNodeWithCost(new_state, node.actions + (action,), new_cost)))

        nodes_expanded += 1