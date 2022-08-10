import unittest

from src.grid_world import ACTIONS, GridWorldWithObstacles
from src.search.bfs import breadth_first_search
from src.search.depth_limited_search import iterative_deepening_search


class TestQ31(unittest.TestCase):

    def test_31b(self):
        env = GridWorldWithObstacles()
        start = (8, 0)
        goal = (0, 8)

        actions = breadth_first_search(env, start, goal)
        self.assertEqual(16, len(actions))
        print(f"Actions took: {tuple(ACTIONS[action] for action in actions)}")

    def test_31c(self):
        env = GridWorldWithObstacles()
        start = (8, 0)
        goal = (0, 8)

        actions = iterative_deepening_search(env, start, goal)
        self.assertEqual(16, len(actions))
        print(f"Actions took: {tuple(ACTIONS[action] for action in actions)}")
