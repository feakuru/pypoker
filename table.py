from card import (
    Card,
    Nominal,
    Suit,
)
from deck import Deck


class Table:
    deck: Deck
    discard_pile: list
    on_table: list

    def __init__(self):
        self.deck = Deck()
        self.discard_pile = list()
        self.on_table = list()

    def discard(self):
        self.discard_pile.append(self.deck.take())

    def put_on_table(self):
        self.on_table.append(self.deck.take())

    def flop(self):
        self.discard()
        self.put_on_table()
        self.put_on_table()
        self.put_on_table()

    def turn(self):
        self.discard()
        self.put_on_table()

    def river(self):
        self.discard()
        self.put_on_table()

    def take(self):
        return self.deck.take()
