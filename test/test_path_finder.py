import unittest
from path_finder import KnightPathFinder

class PathFinderTests(unittest.TestCase):
    def setUp(self):
        self.knight = KnightPathFinder((3,2))
    
    def test_should_set_initial_position(self):
        self.assertEqual(self.knight._root.value, (3,2))

class PathFinderPossibleMoves(unittest.TestCase):
    def test_should_find_all_moves(self):
        knight = KnightPathFinder((4,5))
        self.assertSetEqual(knight.get_valid_moves((5,4)), set([(6, 2), (4, 6), (4, 2), (7, 3), (3, 3), (6, 6), (7, 5), (3, 5)]))

    def test_should_not_return_moves_off_board(self):
        knight = KnightPathFinder((4,5))
        self.assertSetEqual(knight.get_valid_moves((0,0)), set([(1,2),(2,1)]))
        self.assertSetEqual(knight.get_valid_moves((7,7)), set([(5,6),(6,5)]))

class PathfinderNewMovePosition(unittest.TestCase):
    def test_should_return_possible_moves(self):
        knight = KnightPathFinder((4,5))
        self.assertSetEqual(knight.new_move_positions((5,4)), set([(6, 2), (4, 6), (4, 2), (7, 3), (3, 3), (6, 6), (7, 5), (3, 5)]))

    def test_should_filter_considered_positions(self):
        knight = KnightPathFinder((4,5))
        knight._considered_positions = set([(4,6), (3,3)])
        self.assertSetEqual(knight.new_move_positions((5,4)), set([(6, 2), (4, 2), (7, 3), (6, 6), (7, 5), (3, 5)]))
