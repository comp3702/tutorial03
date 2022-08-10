import unittest

from src.grid_world import GridWorldWithObstacles, UP, ACTIONS
from src.search.depth_limited_search import depth_limited_search, iterative_deepening_search


class TestDepthLimitedSearch(unittest.TestCase):
    def test_2_steps_up(self):
        env = GridWorldWithObstacles()
        start = (8, 0)
        goal = (6, 0)

        limit = 4

        actions = depth_limited_search(env, start, goal, limit)
        self.assertEqual(2, len(actions))
        self.assertEqual((UP, UP), actions)

    def test_step_up_over_the_limit(self):
        env = GridWorldWithObstacles()
        start = (8, 0)
        goal = (2, 0)

        limit = 4

        actions = depth_limited_search(env, start, goal, limit)
        # None is the depth limit hit marker!
        self.assertEqual(None, actions)

    def test_step_up_over_the_limit_width_iddfs(self):
        env = GridWorldWithObstacles()
        start = (8, 0)
        goal = (2, 0)

        actions = iterative_deepening_search(env, start, goal)
        # None is the depth limit hit marker!
        self.assertEqual(6, len(actions))
