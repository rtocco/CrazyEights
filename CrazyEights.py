from Card import Card
from Deck import Deck
from Hand import Hand

# Define useful functions.
#############################################################################

# Returns (Boolean) - True if the card is a valid play, False otherwise.
def isValidCard(_playedCard, _discardPile):
    topCard = _discardPile.topCard()
    # In Crazy Eights, the card played must have either the same suit or
    # the same value as the last card played, which will currently be on
    # the top of the discard pile.
    if _playedCard.suit == topCard.suit or _playedCard.getValue() == topCard.getValue():
        return True
    else:
        return False

# Adds the discard pile to the deck, ensuring that the top
# card in the discard pile remains and the deck is shuffled.
def addDiscardToDeck(_discardPile, _deck):
    discardTop = _discardPile.removeTop()
    while len(_discardPile.cards) > 0:
        _deck.addToTop(_discardPile.removeTop())
    _discardPile.addToTop(discardTop)
    _deck.shuffle()

# Play one turn. Note that this is kind of the meat of the program.
def playTurn(_hand, _discardPile, _deck):
    _hand.printCards()
    print('\nCurrent top of discard pile: ', end='')
    _discardPile.topCard().printCard()

    # We loop until the player correctly specifies
    # a card in his hand or to draw from the deck.
    while True:
        # Ask the player to select a card.
        playerInput = input('Select a card to play or type \'draw\': ')
        playerInput = playerInput.lower()

        # If the player has selected to draw a card from the deck.
        if playerInput.find('draw') > -1:
            # If the deck is out of cards, add the discard pile to it.
            if len(_deck.cards) == 0:
                addDiscardToDeck(_discardPile, _deck)
            _hand.addCard(_deck.removeTop())
            break
        else:
            # Find the specified card in the player's hand.
            playerCard = _hand.findCard(playerInput)

            # If the player didn't properly specify a card in his hand.
            if playerCard is None:
                print('That is not a card in your hand.')
                continue
            else:
                # Check if the card played is valid based on the rules of Crazy Eights.
                if isValidCard(playerCard, _discardPile) == True:
                    # Remove the card from the player's hand.
                    _hand.removeCard(playerCard)
                    # Place the card on the top of the discard pile.
                    _discardPile.addToTop(playerCard)
                    break
                else:
                    print('Either the suit or value must match the top card of the discard pile.');

# Initialize the game.
#############################################################################

def main():
    numPlayers = int(input('Please specify a number of players: '))

    # Initialize a deck of 52 cards.
    deck = Deck(False)
    deck.shuffle()

    # Deal cards.
    hands = []
    for i in range(numPlayers):
        hands.append(Hand())
        hand = hands[len(hands) - 1]

        for j in range(8):
            card = deck.removeTop()
            hand.addCard(card)

    # Initialize a discard pile with the first card of the deck.
    discardPile = Deck(True)
    discardPile.addToTop(deck.removeTop())

    # Begin gameplay.
    ############################################################################

    # Each round through the loop gives each player a turn.
    while True:
        # Allow each player to play a turn.
        for index, hand in enumerate(hands):
            # Prompt the player. We don't want to show their
            # hand while another player is still looking.
            for i in range(100):
                print()
            input('Player ' + str(index + 1) + ', press enter to play your turn.')

            # Play a turn.
            playTurn(hand, discardPile, deck)

            # Check if the player has just won.
            if len(hand.cards) == 0:
                print('Player', index + 1, 'has won!!!')
                # Exit the program.
                quit()

if __name__ == '__main__':
    main()
