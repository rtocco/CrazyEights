
class Card:

    # value (int) - Value of the Card to be created.
    # suit (string) - Suit of the Card to be created.
    # Initialize a card with a specified value and suit.
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # Returns - the value of the card as a string (i.e. 2, Jack, etc.).
    def getValue(self):
        if self.value <= 10:
            return str(self.value)
        elif self.value == 11:
            return 'Jack'
        elif self.value == 12:
            return 'Queen'
        elif self.value == 13:
            return 'King'
        elif self.value == 14:
            return 'Ace'

    def printCard(self):
        print(self.getValue(), 'of', self.suit)
