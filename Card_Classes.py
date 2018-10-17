#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 16:26:46 2018

@author: humza
"""
import random


class Player:
    """
    A class with the player information
    """

    def __init__(self, name: str, is_bot: bool):
        self.name = name
        self.hand = []
        self.is_bot = is_bot
        self.score = 0

    def __repr__(self):
        return '{}'.format(self.hand)

    def deal(self, card):
        """
        Deal a card to this player
        """
        self.hand.append(card)

    def add_score(self, amount: int):
        """
        Adds an amount of score to the player
        """
        self.score += amount

    def is_bot(self):
        """
        Returns True if the player is a bot
        """
        return self.is_bot


class Card:
    """
    A card class with suit and number
    """

    def __init__(self, suit: str, value: str):
        """
        Make a card with a suit and a number
        """
        self.suit = suit
        self.value = value
        self.name = '{} {}'.format(self.value, self.suit)

    def __repr__(self):
        return self.name


class Deck:
    """
    A deck istance may contain cards
    """

    def __init__(self, number_cards: int, suits: list):
        """
        Make a deck with a number_cards amount of cards and with a list of suits.
        """
        self.num = number_cards
        self.suits = suits
        self.cards = []

    def __repr__(self):
        return str(self.cards)

    def fill(self):
        """
        Fills the deck with cards.
        """
        numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for value in numbers:
            index = 0
            while index < len(self.suits):
                suit = self.suits[index]
                self.cards.append(Card(suit, value))
                index += 1

    def shuffle(self):
        """
        Shuffles the deck of cards.
        Precondition: Deck is filled with cards
        """
        hold = self.cards[:]
        shuffled = []
        while hold != []:
            index = random.randrange(0, len(hold))
            shuffled.append(hold.pop(index))
        self.cards = shuffled

    def add_jokers(self):
        """
        Adds jokers to the deck
        """
        joker1 = Card('Red', 'Joker')
        joker2 = Card('Black', 'Joker')
        self.cards.append(joker1)
        self.cards.append(joker2)
