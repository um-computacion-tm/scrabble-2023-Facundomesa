from game.models import Tile 

class Cell:
    def _init_(self, multiplier=1, multiplier_type=None, letter=None, active=True):  # Agregamos letter como argumento opcional
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter  # Establecemos el atributo letter con el valor pasado o None
        self.active = active

    def add_letter(self, letter: Tile):
        self.letter = letter