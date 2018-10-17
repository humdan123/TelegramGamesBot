#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 17:29:15 2018

@author: humza
"""
from Card_Classes import Card, Deck, Player


class Table:
    '''
    A class with the orientation of the players relative to each other.
    '''
    def __init__(self, player1, player2, player3, player4):
        self.bottom = player1
        self.left = player2
        self.top = player3
        self.right = player4
        
    def __repr__(self):
        return " {}, {}, {}, {} ".format(self.bottom, self.left, self.top, self.right)


class Bot(Player):
    '''
    A bot for the Hearts Game.
    '''
    def __init__(self, name):
        Player.__init__(self, name, True)
        
    # TODO: Create an algorithm for the bot to run


class Game_Hearts:
    '''
    Instance of the game of hearts
    '''
    def __init__(self, num_players, points_to_end):
        '''
        Makes a game instance with num_players amount of players and
        how many points required to end the game.
        '''
        self.num_players = num_players
        self.points = points_to_end
        self.players = []
        n = num_players
        while n > 0:
            p = Player('Player {}'.format(n), False)
            self.players.append(p)
            n -= 1
        if len(self.players) < 4:
            n = 4 - num_players
            while n < 0:
                p = Bot('Player {}'.format(n))
                self.players.append(p)
                n -= 1
        self.deck = Deck(52, ['Spades', 'Clubs', 'Hearts', 'Diamonds'])
        self.deck.fill()
        self.deck.shuffle()
    
    def distribute_cards(self):
        '''
        Distribute the cards to all players
        '''
        cards_to_deal = self.deck.cards[:]
        while len(cards_to_deal) > 0:
            self.players[0].deal(cards_to_deal.pop())
            self.players[1].deal(cards_to_deal.pop())
            self.players[2].deal(cards_to_deal.pop())
            self.players[3].deal(cards_to_deal.pop())

    def play_game(self):
        '''
        Starts the game.
        '''
        card_pass = ['L', 'R', 'A', 'N']
        n = 0
        while (self.players[0].score < self.points) and\
        (self.players[1].score < self.points) and\
        (self.players[2].score < self.points) and\
        (self.players[3].score < self.points):
             pass           


if __name__ == '__main__':
    # TODO: Create the game
    num = input("Number players? ")
    game = Game_Hearts(int(num), 50)
    game.distribute_cards()
    print(game.deck)


