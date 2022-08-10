import heapq
import unittest

from src.grid_node import GridNodeWithCost
from src.grid_world import GridWorldWithCost
from src.search.ucs import uniform_cost_search


class TestUcs(unittest.TestCase):
    def setUp(self) -> None:
        self.env = GridWorldWithCost()

    def test_heapq(self):
        cost1 = GridNodeWithCost((1, 2), (), 1)
        cost2 = GridNodeWithCost((1, 2), (), 2)
        cost3 = GridNodeWithCost((1, 2), (), 4)
        cost4 = GridNodeWithCost((1, 2), (), 5)

        heap = [cost4, cost2, cost3, cost1]
        heapq.heapify(heap)

        self.assertEqual([cost1, cost2, cost3, cost4], list(heap))

    def test_one_step(self):
        actions, costs = uniform_cost_search(self.env, (8, 0), (8, 1))
        self.assertEqual(1, len(actions))
        self.assertEqual(1, costs)
