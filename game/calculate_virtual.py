from typing import List
from game.cell import Cell

class calculate_word_value:
    @staticmethod
    def Calculate_word_value(cells: List[Cell]) -> int:
        total_value = 0
        word_multiplier = 1

        for cell in cells:
            cell_value = cell.calculate_value()
            if cell.multiplier_type == "word":
                word_multiplier *= cell.multiplier
            total_value += cell_value
        return total_value * word_multiplier