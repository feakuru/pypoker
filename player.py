from typing import List

from card import Card

class Player:
    name: str
    hand: List[Card]

    def __init__(self, name: str = "John Doe"):
        self.name = name
        self.hand = []

    def take(self, card: Card):
        self.hand.append(card)
