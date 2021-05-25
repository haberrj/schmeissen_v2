#!/usr/bin/python3

# Author: Ron Haber
# Date: 25.05.2021
# A class for creating each individual card and forming the deck.

import pygame 
import os, sys

class Card(object):
    def __init__(self, value, suit):
        self.value = value # The value 2, ... , 13 
        self.suit = suit # Clubs, Spades, Diamonds, Hearts
        self.picture = self.assign_pic()
    
    def assign_pic(self):
        '''Will assign a picture to the card based on its value and suit.
        @return pic_name: A string representing the path to a pic for the given card.
        '''
        # Come up with some way to reference pics here
        pic_name = str(self.value) + '_' + self.suit + '.png'
        return pic_name

class Deck(object):
    def __init__(self):
        self.length = 0
        self.cards = []

    def create_deck(self):
        '''Will create the deck with 52 cards and initialize each individual card.
        '''
        suits = ['clubs', 'spades', 'diamonds', 'hearts']
        for suit in suits:
            for i in range(2,14):
                new_card = Card(i, suit)
                self.cards.append(new_card)
                self.length += 1
    
    def deal_cards(self, num_of_cards):
        '''Will deal out cards to a given hand or pile
        @param num_of_cards: An integer representing the number of cards to deal.
        @return cards: A list representing the dealt cards
        '''
