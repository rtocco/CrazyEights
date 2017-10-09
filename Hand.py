
class Hand:

    def __init__(self):
        # An array of card objects.
        self.cards = []

    # card - A Card object.
    def addCard(self, card):
        self.cards.append(card)

    # input (string) - String containing a value and suit.
    # Returns (Card) - A Card object from the hand matching the
    # value and suit in the input string.
    def findCard(self, userInput):
        userInput = userInput.lower()
        index = -1
        for i, card in enumerate(self.cards):
            if (userInput.find(card.getValue().lower()) > -1) and (userInput.find(card.suit.lower()) > -1):
                index = i
                break

        if index == -1:
            return None
        else:
            matchingCard = self.cards[index]
            return matchingCard

    # card (Card) - A card object.
    # Removes the card from the hand matching the card argument.
    # Returns (Boolean) - True if the card is found, False otherwise.
    def removeCard(self, card):
        index = -1
        for i, handCard in enumerate(self.cards):
            if handCard.getValue() == card.getValue() and handCard.suit == card.suit:
                index = i
        if index > -1:
            self.cards.pop(index)
            return True
        else:
            return False

    def printCards(self):
        for card in self.cards:
            card.printCard()
