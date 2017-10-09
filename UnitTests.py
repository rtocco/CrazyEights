import unittest
from Card import Card
from Deck import Deck
from Hand import Hand
from CrazyEights import isValidCard
from CrazyEights import addDiscardToDeck
from CrazyEights import playTurn

class CardTests(unittest.TestCase):

    def test_init(self):
        card = Card(2, 'Hearts')
        self.assertEqual(card.value, 2)
        self.assertEqual(card.suit, 'Hearts')

    def test_getValue(self):
        card = Card(2, 'Diamonds')
        self.assertEqual(card.getValue(), '2')
        card = Card(11, 'Spades')
        self.assertEqual(card.getValue(), 'Jack')


class HandTests(unittest.TestCase):

    def test_init(self):
        hand = Hand()
        self.assertEqual(len(hand.cards), 0)

    def test_addCard(self):
        hand = Hand()
        card1 = Card(3, 'Clubs')
        card2 = Card(4, 'Spades')
        hand.addCard(card1)
        hand.addCard(card2)

        self.assertEqual(len(hand.cards), 2)

        self.assertEqual(hand.cards[0].value, 3)
        self.assertEqual(hand.cards[0].suit, 'Clubs')

        self.assertEqual(hand.cards[1].value, 4)
        self.assertEqual(hand.cards[1].suit, 'Spades')

    def test_removeCard(self):
        hand = Hand()
        card1 = Card(3, 'Clubs')
        card2 = Card(4, 'Spades')
        card3 = Card(5, 'Hearts')
        hand.addCard(card1)
        hand.addCard(card2)

        self.assertFalse(hand.removeCard(card3))

        self.assertTrue(hand.removeCard(card1))
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(hand.cards[0].value, 4)
        self.assertEqual(hand.cards[0].suit, 'Spades')

        self.assertTrue(hand.removeCard(card2))
        self.assertEqual(len(hand.cards), 0)

    # Note that this will only pass if addCard works.
    def test_findCard(self):
        hand = Hand()
        card1 = Card(2, 'Spades')
        card2 = Card(10, 'Diamonds')
        card3 = Card(4, 'Diamonds')
        card4 = Card(8, 'Clubs')
        card5 = Card(13, 'Hearts')
        hand.addCard(card1)
        hand.addCard(card2)
        hand.addCard(card3)
        hand.addCard(card4)
        hand.addCard(card5)

        foundCard1 = hand.findCard("10 of Diamonds")
        self.assertEqual(foundCard1.getValue(), "10")
        self.assertEqual(foundCard1.suit, "Diamonds")

        foundCard2 = hand.findCard("king of hearts")
        self.assertEqual(foundCard2.getValue(), "King")
        self.assertEqual(foundCard2.suit, "Hearts")

        foundCard3 = hand.findCard("8 of clubs")
        self.assertEqual(foundCard3.getValue(), "8")
        self.assertEqual(foundCard3.suit, "Clubs")


class DeckTests(unittest.TestCase):

    def test_init(self):
        emptyDeck = Deck(True)
        self.assertEqual(len(emptyDeck.cards), 0)

        fullDeck = Deck(False)
        self.assertEqual(len(fullDeck.cards), 52)

        hearts = [x for x in fullDeck.cards if x.suit == 'Hearts']
        self.assertEqual(len(hearts), 13)
        self.assertTrue(any(x.value == 2 for x in hearts))
        self.assertTrue(any(x.value == 11 for x in hearts))

        diamonds = [x for x in fullDeck.cards if x.suit == 'Diamonds']
        self.assertEqual(len(diamonds), 13)
        self.assertTrue(any(x.value == 5 for x in diamonds))
        self.assertTrue(any(x.value == 12 for x in diamonds))

        clubs = [x for x in fullDeck.cards if x.suit == 'Clubs']
        self.assertEqual(len(clubs), 13)
        self.assertTrue(any(x.value == 7 for x in clubs))
        self.assertTrue(any(x.value == 13 for x in clubs))

        spades = [x for x in fullDeck.cards if x.suit == 'Spades']
        self.assertEqual(len(spades), 13)
        self.assertTrue(any(x.value == 9 for x in spades))
        self.assertTrue(any(x.value == 14 for x in spades))

    def test_shuffle(self):
        deck = Deck(False)
        deck.shuffle()
        self.assertEqual(len(deck.cards), 52)

        numConsecutive = 0
        suit = 0
        num = 0
        previousCard = None
        for card in deck.cards:
            if previousCard == None:
                previousCard = card
                continue
            if card.suit == previousCard.suit and abs(card.value - previousCard.value) == 1:
                numConsecutive += 1
            previousCard = card

        self.assertTrue(numConsecutive < 10)

    # Note that this test will fail if the deck is initialized
    # in the wrong order or with the wrong number of cards.
    def test_removeTop(self):
        deck = Deck(False)
        card = deck.removeTop()
        self.assertEqual(card.suit, 'Spades')
        self.assertEqual(card.value, 14)
        self.assertEqual(len(deck.cards), 51)

    # Note that this test will fail if the deck is initialized
    # in the wrong order or with the wrong number of cards.
    def test_topCard(self):
        deck = Deck(False)
        card = deck.topCard()
        self.assertEqual(card.suit, 'Spades')
        self.assertEqual(card.value, 14)
        self.assertEqual(len(deck.cards), 52)

    # Note that this test will fail if deck initialization
    # with an empty deck doesn't work.
    def test_addToTop(self):
        deck = Deck(True)
        card = Card(5, 'Diamonds')
        deck.addToTop(card)
        self.assertEqual(len(deck.cards), 1)
        self.assertEqual(deck.cards[0].suit, 'Diamonds')
        self.assertEqual(deck.cards[0].value, 5)


class GamePlayTests(unittest.TestCase):

    def test_isValidCard(self):
        discardPile = Deck(True)

        deckCard = Card(2, 'Spades')
        playerCard = Card(5, 'Spades')
        discardPile.addToTop(deckCard)
        self.assertTrue(isValidCard(playerCard, discardPile))

        deckCard = Card(13, 'Spades')
        playerCard = Card(13, 'Hearts')
        discardPile.addToTop(deckCard)
        self.assertTrue(isValidCard(playerCard, discardPile))

        deckCard = Card(8, 'Diamonds')
        playerCard = Card(12, 'Clubs')
        discardPile.addToTop(deckCard)
        self.assertFalse(isValidCard(playerCard, discardPile))

    def test_addDiscardToDeck(self):
        discardPile = Deck(False)
        deck = Deck(True)
        discardPile.shuffle()
        suit = discardPile.topCard().suit
        value = discardPile.topCard().value

        addDiscardToDeck(discardPile, deck)
        self.assertEqual(len(discardPile.cards), 1)
        self.assertEqual(len(deck.cards), 51)
        self.assertEqual(discardPile.cards[0].value, value)
        self.assertEqual(discardPile.cards[0].suit, suit)


    # Todo
    def test_playTurn(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
