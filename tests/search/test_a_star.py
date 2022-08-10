import unittest

from src.grid_world import GridWorldWithObstacles
from src.search.grid_world_heuristics import grid_world_manhattan_distance


class TestAStar(unittest.TestCase):
    def test_grid_world_manhattan_distance(self):
        env = GridWorldWithObstacles()
        distance = grid_world_manhattan_distance(env, (8, 0), (0, 8))

        self.assertEqual(16, distance)
