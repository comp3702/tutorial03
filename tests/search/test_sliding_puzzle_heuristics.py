import unittest

from src.search.sliding_puzzle_heuristics import mismatches_heuristics
from src.sliding_puzzle import SlidingPuzzle


class TestSlidingPuzzleHeuristics(unittest.TestCase):
    def setUp(self) -> None:
        self.goal = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, -1)
        )

    def test_mismatches_heuristics(self):
        env = SlidingPuzzle()
        state = (
            (1, 2, 3),
            (4, 5, 6),
            (-1, 7, 8)
        )

        cost = mismatches_heuristics(env, state, self.goal)
        self.assertEqual(3, cost)

    def test_mismatches_heuristics_hard(self):
        env = SlidingPuzzle()
        state = (
            (7, 2, 4),
            (5, 3, 6),
            (8, -1, 1)
        )

        cost = mismatches_heuristics(env, state, self.goal)
        self.assertEqual(7, cost)

