import unittest

from src.grid_world import ACTIONS
from src.search.a_star_search import a_star_search
from src.search.sliding_puzzle_heuristics import mismatches_heuristics, manhattan_distance_heuristics
from src.sliding_puzzle import SlidingPuzzle, BLANK


class TestQ33(unittest.TestCase):
    def test_q33c_misplaced(self):
        env = SlidingPuzzle()

        start = (
            (7, 2, 4),
            (5, 3, 6),
            (8, BLANK, 1)
        )
        goal = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, BLANK)
        )

        actions, cost = a_star_search(env, start, goal, mismatches_heuristics)

        self.assertEqual(19, len(actions)) # same as BFS in tutorial 02
        print(f"Actions took: {tuple(ACTIONS[action] for action in actions)}")

    def test_q33c_manhattan(self):
        env = SlidingPuzzle()

        start = (
            (7, 2, 4),
            (5, 3, 6),
            (8, BLANK, 1)
        )
        goal = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, BLANK)
        )

        actions, cost = a_star_search(env, start, goal, manhattan_distance_heuristics)

        self.assertEqual(19, len(actions)) # same as BFS in tutorial 02
        print(f"Actions took: {tuple(ACTIONS[action] for action in actions)}")
