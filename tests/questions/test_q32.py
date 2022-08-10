import unittest

from src.grid_world import GridWorldWithObstacles, ACTIONS, GridWorldWithCost
from src.search.bfs import breadth_first_search
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
