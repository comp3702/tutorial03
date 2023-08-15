import unittest

from src.grid_node import GridNode
from src.grid_world import UP, DOWN, LEFT


class TestGridNode(unittest.TestCase):
    def test_init(self):
        node = GridNode((8, 0), (UP, DOWN, LEFT))
        self.assertEqual((8, 0), node.state)
        self.assertEqual((UP, DOWN, LEFT), node.actions)

if __name__ == '__main__':
    unittest.main()