import unittest

from src.grid_world import GridWorldWithObstacles, LEFT, UP, RIGHT, DOWN


class TestGridWorldWithObstacles(unittest.TestCase):
    def test_init(self):
        env = GridWorldWithObstacles()
        self.assertEqual(8, env.last_row)
        self.assertEqual(8, env.last_col)

    def test_actions_bottom_left(self):
        env = GridWorldWithObstacles()

        self.assertEqual((RIGHT, UP), env.actions((8, 0)))

    def test_actions_bottom_right(self):
        env = GridWorldWithObstacles()

        self.assertEqual((LEFT, UP), env.actions((8, 8)))

    def test_actions_top_right(self):
        env = GridWorldWithObstacles()

        self.assertEqual((LEFT, DOWN), env.actions((0, 8)))

    def test_actions_top_left(self):
        env = GridWorldWithObstacles()

        self.assertEqual((RIGHT, DOWN), env.actions((0, 0)))

    def test_actions_obstacle_up(self):
        env = GridWorldWithObstacles()

        self.assertEqual((LEFT, RIGHT), env.actions((8, 4)))

    def test_actions_obstacle_left(self):
        env = GridWorldWithObstacles()

        self.assertEqual((RIGHT, UP, DOWN), env.actions((3, 7)))

    def test_actions_obstacle_right(self):
        env = GridWorldWithObstacles()

        self.assertEqual((LEFT, UP, DOWN), env.actions((4, 5)))

    def test_actions_obstacle_down_and_right(self):
        env = GridWorldWithObstacles()

        self.assertEqual((LEFT, UP), env.actions((6, 5)))

    def test_step_up(self):
        env = GridWorldWithObstacles()
        new_state, cost = env.step(UP, (8, 0))

        self.assertEqual((7, 0), new_state)

    def test_step_down(self):
        env = GridWorldWithObstacles()
        new_state, cost = env.step(DOWN, (7, 0))

        self.assertEqual((8, 0), new_state)

    def test_step_right(self):
        env = GridWorldWithObstacles()
        new_state, cost = env.step(RIGHT, (8, 0))

        self.assertEqual((8, 1), new_state)

    def test_step_left(self):
        env = GridWorldWithObstacles()
        new_state, cost = env.step(LEFT, (8, 1))

        self.assertEqual((8, 0), new_state)


