from src.grid_world import GridWorldWithCost, ACTIONS
from src.search.a_star_search import a_star_search
from src.search.grid_world_heuristics import grid_world_manhattan_distance
from src.search.sliding_puzzle_heuristics import mismatches_heuristics
from src.sliding_puzzle import SlidingPuzzle

if __name__ == '__main__':
    # this file can be used as a playground to run different searches
    # but the main interface is through the tests under tests/questions

    # this is Q3.2e
    env = GridWorldWithCost()

    actions, cost = a_star_search(env, (8, 0), (0, 8), grid_world_manhattan_distance)

    print(f"Actions took: {tuple(ACTIONS[action] for action in actions)}")

    # this will run out of memory
    # init_state = (
    #     (9, 2, 1, 4),
    #     (6, 13, 8, 14),
    #     (11, 5, 3, -1),
    #     (10, 12, 7, 15)
    # )
    # goal_state = (
    #     (1, 2, 3, 4),
    #     (5, 6, 7, 8),
    #     (9, 10, 11, 12),
    #     (13, 14, 15, -1)
    # )
    # puzzle15 = SlidingPuzzle(init_state)
    #
    # a_star_search(puzzle15, init_state, goal_state, mismatches_heuristics)
