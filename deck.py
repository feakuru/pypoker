import itertools
import random

from card import (
    Card,
    Nominal,
    Suit,
)


class Deck:
    cards: list

    def __init__(self):
        self.cards = list()
        card_attr_pairs = list(itertools.product(Suit, Nominal))
        random.shuffle(card_attr_pairs)
        for card_attrs in card_attr_pairs:
            self.cards.append(Card(*card_attrs))

    def take(self) -> Card:
        try:
            return self.cards.pop()
        except IndexError:
            return None
