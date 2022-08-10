import unittest

from src.grid_world import GridWorldWithObstacles, ACTIONS, GridWorldWithCost
from src.search.a_star_search import a_star_search
from src.search.bfs import breadth_first_search
from src.search.grid_world_heuristics import grid_world_manhattan_distance
from src.search.ucs import uniform_cost_search


class TestQ32(unittest.TestCase):

    def test_32a(self):
        env = GridWorldWithObstacles((
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
        ))
        actions = breadth_first_search(env, (8, 0), (0, 8))

        self.assertEqual(16, len(actions))
        print(f"Actions took: {tuple(ACTIONS[action] for action in actions)}")

    def test_32b(self):
        env = GridWorldWithCost()
        actions, costs = uniform_cost_search(env, (8, 0), (0, 8))
        self.assertEqual(16, len(actions))
        self.assertEqual(16, costs)

    def test_32d(self):
        env = GridWorldWithCost()
        distance = grid_world_manhattan_distance(env, (8, 0), (0, 8))

        self.assertEqual(16, distance)

    def test_32e(self):
        env = GridWorldWithCost()

        actions, cost = a_star_search(env, (8, 0), (0, 8), grid_world_manhattan_distance)

        self.assertEqual(16, len(actions))
        print(f"Actions took: {tuple(ACTIONS[action] for action in actions)}")