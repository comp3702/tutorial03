import unittest

from src.grid_world import GridWorld, UP
from src.search.depth_limited_search import depth_limited_search


class TestDepthLimitedSearch(unittest.TestCase):
    def test_2_steps_up(self):
        env = GridWorld()
        start = (8, 0)
        goal = (6, 0)

        limit = 4

        actions = depth_limited_search(env, start, goal, limit)
        self.assertEqual(2, len(actions))
        self.assertEqual((UP, UP), actions)

    def test_step_up_over_the_limit(self):
        env = GridWorld()
        start = (8, 0)
        goal = (2, 0)

        limit = 4

        actions = depth_limited_search(env, start, goal, limit)
        # None is the depth limit hit marker!
        self.assertEqual(None, actions)
