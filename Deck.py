import random

from Card import Card

class Deck:

    # empty - boolean specifying if the deck should start out empty.
    # Initialize a deck, either empty or with 52 cards.
    def __init__(self, empty):
        # An array of Card objects.
        self.cards = []
        if empty == True:
            return

        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            for i in range(2, 11):
                self.cards.append(Card(i, suit))
            self.cards.append(Card(11, suit))
            self.cards.append(Card(12, suit))
            self.cards.append(Card(13, suit))
            self.cards.append(Card(14, suit))

    # Shuffle the deck (pseudo) randomly.
    def shuffle(self):
        for i in range(1000):
            pos1 = random.randint(0, len(self.cards) - 1)
            pos2 = random.randint(0, len(self.cards) - 1)
            temp = self.cards[pos1]
            self.cards[pos1] = self.cards[pos2]
            self.cards[pos2] = temp

    # Returns - the top Card.
    def removeTop(self):
        return self.cards.pop()

    # Returns - the top Card
    def topCard(self):
        return self.cards[len(self.cards) - 1]

    def addToTop(self, card):
        self.cards.append(card)

    def printCards(self):
        for card in self.cards:
            card.printCard()
