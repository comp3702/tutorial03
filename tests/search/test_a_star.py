import unittest

from src.grid_world import GridWorldWithObstacles, GridWorldWithCost, ACTIONS
from src.search.a_star_search import a_star_search
from src.search.grid_world_heuristics import grid_world_manhattan_distance


class TestAStar(unittest.TestCase):
    def test_grid_world_manhattan_distance(self):
        env = GridWorldWithCost()
        distance = grid_world_manhattan_distance(env, (8, 0), (0, 8))

        self.assertEqual(16, distance)

    def test_a_star_in_grid_world(self):
        env = GridWorldWithCost()

        actions, cost = a_star_search(env, (8, 0), (0, 8), grid_world_manhattan_distance)

        self.assertEqual(16, len(actions))
        print(f"Actions took: {tuple(ACTIONS[action] for action in actions)}")