import unittest

from src.grid_world import LEFT, UP, RIGHT, DOWN
from src.sliding_puzzle import SlidingPuzzle, BLANK


class TestSlidingPuzzle(unittest.TestCase):
    def setUp(self) -> None:
        self.env = SlidingPuzzle()

        self.bottom_left = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, BLANK)
        )

    def test_init(self):
        env = SlidingPuzzle()
        self.assertEqual(2, env.last_row)
        self.assertEqual(2, env.last_col)

    def test_find_blank(self):
        self.assertEqual((2, 2), self.env.find_blank(self.bottom_left))

    def test_find_actions_bottom_right(self):
        self.assertEqual(
            (LEFT, UP),
            self.env.actions(self.bottom_left)
        )

    def test_find_actions_top_left(self):
        self.assertEqual(
            (RIGHT, DOWN),
            self.env.actions((
                (BLANK, 2, 3),
                (4, 5, 6),
                (7, 8, 1)
            ))
        )

    def test_find_actions_center(self):
        self.assertEqual(
            (LEFT, RIGHT, UP, DOWN),
            self.env.actions(
                (
                    (5, 2, 3),
                    (4, BLANK, 6),
                    (7, 8, 1)
                ))
        )

    def test_step_up(self):
        self.assertEqual(
            (
                (5, BLANK, 3),
                (4, 2, 6),
                (7, 8, 1)
            ),
            self.env.step(UP, (
            (5, 2, 3),
            (4, BLANK, 6),
            (7, 8, 1)
        ))
        )

    def test_step_down(self):
        state = (
            (5, 2, 3),
            (4, BLANK, 6),
            (7, 8, 1)
        )
        self.assertEqual(
            (
                (5, 2, 3),
                (4, 8, 6),
                (7, BLANK, 1)
            ),
            self.env.step(DOWN, state)
        )

    def test_step_left(self):
        state = (
            (5, 2, 3),
            (4, BLANK, 6),
            (7, 8, 1)
        )
        self.assertEqual(
            (
                (5, 2, 3),
                (BLANK, 4, 6),
                (7, 8, 1)
            ),
            self.env.step(LEFT, state)
        )

    def test_step_right(self):
        state = (
            (5, 2, 3),
            (4, BLANK, 6),
            (7, 8, 1)
        )
        self.assertEqual(
            (
                (5, 2, 3),
                (4, 6, BLANK),
                (7, 8, 1)
            ),
            self.env.step(RIGHT, state)
        )

    def test_cost(self):
        self.assertEqual(1, self.env.cost(self.bottom_left))