
from game.player import Player
from game.board import Board
from game.cell import Cell
from game.models import BagTiles


class ScrabbleGame:
    def __init__(self, players_count=3):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        self.players_count = players_count
        for _ in range(players_count):
            self.players.append(Player(id=len(self.players) + 1))
        self.current_player = None
    

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif id(self.current_player) == id(self.players[(len(self.players)) -1]):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player)+ 1]

    def test_next_turn_when_player_is_last():
    # Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]
    