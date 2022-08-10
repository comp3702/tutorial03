import unittest

from src.grid_world import GridWorldWithObstacles, RIGHT, UP, ACTIONS
from src.search.bfs import breadth_first_search


class TestBfs(unittest.TestCase):
    def test_2_steps_right(self):
        env = GridWorldWithObstacles()
        start = (8, 0)
        goal = (8, 2)

        actions = breadth_first_search(env, start, goal)
        self.assertEqual(2, len(actions))
        self.assertEqual((RIGHT, RIGHT), actions)

    def test_2_steps_up(self):
        env = GridWorldWithObstacles()
        start = (8, 0)
        goal = (6, 0)

        actions = breadth_first_search(env, start, goal)
        self.assertEqual(2, len(actions))
        self.assertEqual((UP, UP), actions)

    def test_31b(self):
        env = GridWorldWithObstacles()
        start = (8, 0)
        goal = (0, 8)

        actions = breadth_first_search(env, start, goal)
        self.assertEqual(16, len(actions))
        print(f"Actions took: {tuple(ACTIONS[action] for action in actions)}")