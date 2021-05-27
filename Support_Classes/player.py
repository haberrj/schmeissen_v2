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

    def pick_up_deck_card(self, deck, num_of_cards):
        '''Will add a card to the player's hand from the main deck.
        @param deck: A Deck object that represents the main deck.
        @param num_of_cards: An integer representing the number of cards to pick up.
        '''
        cards_in_deck = deck.getDeckSize()
        if(cards_in_deck < num_of_cards):
            num_of_cards = cards_in_deck # reduce the number of cards picked up
        while(self.hand.getLength() < 2):
            cards = deck.deal_cards(1) # deal one card at a time
            self.hand.add_cards(cards)
    