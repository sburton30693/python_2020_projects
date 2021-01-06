# Spencer Burton
# 1/6/2021
# Black Jack Game

# Some of the Rules:
# 1. Each player is dealt 2 cards at the beginning.
# 2. In order to win you have to be higher than the dealer.
# 3. Ace can be a 1 or 11.
# 4. Face cards are 10.
# 5. Cannot go over 21, or you lose automatically.
# 6. If you have black jack, a face card and an ace, you have to call it out.
# 7. When you bust, go over 21, you have to call it out.
# 8. If you have two of the same cards you can split.

import playing_cards as pc
import game_functions as gf


class BJCard(pc.PosCard):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.face_up:
            v = BJCard.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None

        return v


class BJDeck(pc.Deck):

    def populate(self):
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.add(BJCard(rank, suit))


class BJHand(pc.Hand):

    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name


# Testing Area
deck = BJDeck()
deck.populate()
deck.shuffle()

card = deck.cards[0]
print(card)
print(card.value)
