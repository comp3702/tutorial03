import unittest

from src.grid_world import GridWorld, LEFT, UP, RIGHT, DOWN


class TestGridWorld(unittest.TestCase):
    def test_init(self):
        env = GridWorld()
        self.assertEqual(8, env.last_row)
        self.assertEqual(8, env.last_col)
        self.assertEqual((0, 8), env.goal)
        self.assertEqual((8, 0), env.start)

    def test_actions_bottom_left(self):
        env = GridWorld((8, 0))

        self.assertEqual(8, env.current_row)
        self.assertEqual(0, env.current_col)

        self.assertEqual([RIGHT, UP], env.actions())

    def test_actions_bottom_right(self):
        env = GridWorld((8, 8))

        self.assertEqual([LEFT, UP], env.actions())

    def test_actions_top_right(self):
        env = GridWorld((0, 8))

        self.assertEqual([LEFT, DOWN], env.actions())

    def test_actions_top_left(self):
        env = GridWorld((0, 0))

        self.assertEqual([RIGHT, DOWN], env.actions())

    def test_actions_obstacle_up(self):
        env = GridWorld((8, 4))

        self.assertEqual([LEFT, RIGHT], env.actions())

    def test_actions_obstacle_left(self):
        env = GridWorld((3, 7))

        self.assertEqual([RIGHT, UP, DOWN], env.actions())

    def test_actions_obstacle_right(self):
        env = GridWorld((4, 5))

        self.assertEqual([LEFT, UP, DOWN], env.actions())

    def test_actions_obstacle_down_and_right(self):
        env = GridWorld((6, 5))

        self.assertEqual([LEFT, UP], env.actions())

    def test_step_up(self):
        env = GridWorld((8, 0))
        env.step(UP)

        self.assertEqual(7, env.current_row)
        self.assertEqual(0, env.current_col)

    def test_step_down(self):
        env = GridWorld((7, 0))
        env.step(DOWN)

        self.assertEqual(8, env.current_row)
        self.assertEqual(0, env.current_col)

    def test_step_right(self):
        env = GridWorld((8, 0))
        env.step(RIGHT)

        self.assertEqual(8, env.current_row)
        self.assertEqual(1, env.current_col)

    def test_step_left(self):
        env = GridWorld((8, 1))
        env.step(LEFT)

        self.assertEqual(8, env.current_row)
        self.assertEqual(0, env.current_col)
