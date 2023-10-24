from game.scramble import ScrabbleGame

class GetPlayerCount:
    def get_count(self):
        while True:
            try:
                player_count = int(input('Ingrese la cantidad de jugadores (1-4): '))
                if 1 <= player_count <= 4:
                    return player_count
                else:
                    print('Por favor, ingrese un número entre 1 y 4.')
            except ValueError:
                print('Por favor, ingrese un número válido.')

# El código anterior es la implementación de la clase GetPlayerCount. Ahora vamos a probarla con las pruebas unitarias.

import unittest
from unittest.mock import patch

class TestCLI(unittest.TestCase):

    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        get_count = GetPlayerCount()
        self.assertEqual(
            get_count.get_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        get_count = GetPlayerCount()
        self.assertEqual(
            get_count.get_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['10', '1'])
    def test_get_player_count_control_max(self, input_patched, print_patched):
        get_count = GetPlayerCount()
        self.assertEqual(
            get_count.get_count(),
            1,
        )

if __name__ == '_main_':
    unittest.main()