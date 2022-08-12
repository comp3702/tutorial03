import unittest

from src.search.sliding_puzzle_heuristics import mismatches_heuristics, manhattan_distance_heuristics
from src.sliding_puzzle import SlidingPuzzle, BLANK


class TestSlidingPuzzleHeuristics(unittest.TestCase):
    def setUp(self) -> None:
        self.goal = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, BLANK)
        )

    def test_mismatches_heuristics(self):
        env = SlidingPuzzle()
        state = (
            (1, 2, 3),
            (4, 5, 6),
            (BLANK, 7, 8)
        )

        cost = mismatches_heuristics(env, state, self.goal)
        self.assertEqual(2, cost)

    def test_mismatches_heuristics_hard(self):
        env = SlidingPuzzle()
        state = (
            (7, 2, 4),
            (5, 3, 6),
            (8, BLANK, 1)
        )

        cost = mismatches_heuristics(env, state, self.goal)
        self.assertEqual(6, cost)


    def test_manhatan_distance_heuristics(self):
        env = SlidingPuzzle()
        state = (
            (7, 2, 4),
            (5, BLANK, 6),
            (8, 3, 1)
        )
        goal = (
            (BLANK, 1, 2),
            (3, 4, 5),
            (6, 7, 8)
        )

        cost = manhattan_distance_heuristics(env, state, goal)
        # 3 + 1 + 2 + 2 + 2 + 3 + 3 + 2
        self.assertEqual(18, cost)

