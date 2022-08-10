import unittest

from src.grid_node import GridNode


class TestGridNode(unittest.TestCase):
    def test_init(self):
        node = GridNode((8, 0), (UP, DOWN, LEFT))
        self.assertEqual((8, 0), node.state)
        self.assertEqual((UP, DOWN, LEFT), node.actions)
