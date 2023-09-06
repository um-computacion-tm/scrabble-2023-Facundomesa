import unittest
from game.player import Player
from game.models import Tile
from unittest.mock import Mock

class MockCell:
    def __init__(self, calculated_value):
        self.calculated_value = calculated_value

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player('Aldana')
        self.assertEqual(player.name, 'Aldana')
        self.assertEqual(len(player.tiles), 0)

    def test_rack_property(self):
        player = Player('Bruno')
        tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        player.tiles = tiles
        self.assertEqual(player.rack, tiles)

    def test_validate_word_valid(self):
        player = Player('Miguel')
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        self.assertTrue(player.validate_word('ABC'))


    def test_validate_word_invalid(self):
        player = Player('Fausto')
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        self.assertFalse(player.validate_word('ABCD'))  

    def test_pass_turn(self):
        player = Player('Laura')
        player.pass_turn()  

    def test_get_score(self):
        player= Player('Alex')
        player.board = Mock()  
        mock_cell_1 = MockCell(3)
        mock_cell_2 = MockCell(2)
        player.board.played_cells = [mock_cell_1, mock_cell_2]

        self.assertEqual(player.get_score(), 5) 

class MockCell:
    def __init__(self, value):
        self.value = value

    def calculate_value(self): 
        return self.value


if __name__ == '__main__':
    unittest.main()