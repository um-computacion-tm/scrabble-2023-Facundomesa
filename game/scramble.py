from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.cell import Cell


class ScrabbleGame:
    def _init_(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
             self.players.append(Player(id=len(self.players) + 1))# Quitamos el argumento 'id'
        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif id(self.current_player) == id(self.players[(len(self.players)) -1]):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player)+ 1]