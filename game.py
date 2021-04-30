from typing import List

from player import Player
from table import Table


class Game:
    table: Table
    players: List[Player]

    def __init__(self, players: List[Player]):
        self.table = Table()
        self.players = players

        for _ in [1, 2]:
            for player in self.players:
                player.take(self.table.take())

    def flop(self):
        return self.table.flop()

    def turn(self):
        return self.table.turn()

    def river(self):
        return self.table.river()
