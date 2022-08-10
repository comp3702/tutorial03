import unittest

from src.grid_world import GridWorldWithCost, LEFT, UP, RIGHT, DOWN


class TestGridWorldWithCost(unittest.TestCase):
    def setUp(self) -> None:
        self.env = GridWorldWithCost()

    def test_init(self):
        env = GridWorldWithCost()
        self.assertEqual(8, env.last_row)
        self.assertEqual(8, env.last_col)

    def test_find_actions_bottom_right(self):
        self.assertEqual(
            (LEFT, UP),
            self.env.actions((8, 8))
        )

    def test_find_actions_top_left(self):
        self.assertEqual(
            (RIGHT, DOWN),
            self.env.actions((0, 0))
        )

    def test_find_actions_center(self):
        self.assertEqual(
            (LEFT, RIGHT, UP, DOWN),
            self.env.actions((4, 4))
        )

    def test_step_left(self):
        new_state = self.env.step(LEFT, (8, 1))

        self.assertEqual((8, 0), new_state)

    def test_step_right(self):
        new_state = self.env.step(RIGHT, (2, 3))

        self.assertEqual((2, 4), new_state)

    def test_cost1(self):
        self.assertEqual(1, self.env.cost((8, 0)))

    def test_cost10(self):
        self.assertEqual(10, self.env.cost((2, 2)))

