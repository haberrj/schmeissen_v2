#!/usr/bin/python3

# Author: Ron Haber
# Date: 25.05.2021
# A class for creating each player and maintaining their attributes

import os, sys
import Support_Classes.card as card

class Player(object):
    def __init__(self, name):
        self.hand = card.Pile()
        self.face_down = card.Pile()
        self.face_up = card.Pile()
        self.name = name

    def show_hand(self):
        '''Will show the player their hand.
        '''
        cards = self.hand.getCards()
        return cards
    
    def show_face_up(self):
        cards = self.face_up.getCards()
        return cards