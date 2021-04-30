from enum import (
    Enum,
    IntEnum,
)


class Nominal(IntEnum):
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14


class Suit(Enum):
    clubs = 'clubs'
    diamonds = 'diamonds'
    hearts = 'hearts'
    spades = 'spades'


class Card:
    suit: Suit
    nominal: Nominal

    def __init__(self, suit: Suit, nominal: Nominal):
        self.suit = suit
        self.nominal = nominal

    def __str__(self):
        return f'{self.nominal.name} of {self.suit.name}'
