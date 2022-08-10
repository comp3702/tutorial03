import unittest

from src.grid_world import GridWorldWithObstacles, RIGHT, UP, ACTIONS, GridWorldWithCost
from src.search.bfs import breadth_first_search


class TestBfs(unittest.TestCase):
    def setUp(self) -> None:
        self.env = GridWorldWithObstacles()

    def test_2_steps_right(self):
        start = (8, 0)
        goal = (8, 2)

        actions = breadth_first_search(self.env, start, goal)
        self.assertEqual(2, len(actions))
        self.assertEqual((RIGHT, RIGHT), actions)

    def test_2_steps_up(self):
        start = (8, 0)
        goal = (6, 0)

        actions = breadth_first_search(self.env, start, goal)
        self.assertEqual(2, len(actions))
        self.assertEqual((UP, UP), actions)
