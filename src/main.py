from src.grid_world import GridWorldWithCost, ACTIONS
from src.search.a_star_search import a_star_search
from src.search.grid_world_heuristics import grid_world_manhattan_distance

if __name__ == '__main__':
    # this file can be used as a playground to run different searches
    # but the main interface is through the tests under tests/questions

    # this is Q3.2e
    env = GridWorldWithCost()

    actions, cost = a_star_search(env, (8, 0), (0, 8), grid_world_manhattan_distance)

    print(f"Actions took: {tuple(ACTIONS[action] for action in actions)}")