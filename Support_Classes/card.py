#!/usr/bin/python3

# Author: Ron Haber
# Date: 25.05.2021
# A class for creating each individual card and forming the deck.

import random
import os, sys

class Card(object):
    def __init__(self, value, suit):
        self.value = value # The value 2, ... , 13 
        self.suit = suit # Clubs, Spades, Diamonds, Hearts
        self.picture = self.assign_pic()
    
    def assign_pic(self):
        '''Will assign a picture to the card based on its value and suit.
        @return pic_name: A string representing the path to a pic for the given card.a
        '''
        # Come up with some way to reference pics here
        pic_name = str(self.value) + '_' + self.suit + '.png'
        return pic_name
    
    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getPicture(self):
        return self.picture

class Deck(object):
    def __init__(self):
        self.length = 0
        self.cards = []
        self.create_deck()

    def create_deck(self):
        '''Will create the deck with 52 cards and initialize each individual card.
        '''
        suits = ['clubs', 'spades', 'diamonds', 'hearts']
        for suit in suits:
            for i in range(2,15): # J = 11, Q = 12, K = 13, A = 14
                new_card = Card(i, suit)
                self.cards.append(new_card)
                self.length += 1
    
    def deal_cards(self, num_of_cards):
        '''Will deal out random cards to a given hand or pile
        @param num_of_cards: An integer representing the number of cards to deal.
        @return cards: A list representing the dealt cards
        '''
        cards = []
        for i in range(num_of_cards):
            random_card = random.randint(0,self.length)
            card_removed = self.cards.pop(random_card)
            self.length -= 1
            cards.append(card_removed)
        return cards
    
    def getDeckSize(self):
        return self.length

    def getRemainingCards(self):
        return self.cards

class Pile(object):
    '''This will be the class defined for each pile (trash, centre, hand, etc.)
    This is different than the deck in that this can only be specific sizes based on gameplay'''
    def __init__(self):
        self.cards = []
        self.length = 0
    
    def add_cards(self, cards):
        '''Will add cards to the specific pile.
        @param cards: A list of class type Card for the cards to add
        '''
        for card in cards:
            self.cards.append(card)
            self.length += 1
    
    def play_cards(self, cards):
        '''Will play specific cards from the pile.
        @param cards: A list of the class type Card for the cards to play.
        '''
        for card in cards:
            self.cards.remove(card)
            self.length -= 1
    
    def getLength(self):
        return self.length

    def getCards(self):
        return self.cards
