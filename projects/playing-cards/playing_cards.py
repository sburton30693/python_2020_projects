# Spencer Burton
# 12/20
# Playing Cards Class

class Card(object):
    RANKS = ("A", "2", "3", "4", "5", "6" , "7",
             "8", "9", "10", "J", "Q", "K")
    SUITS = ("♠", "♣", "♢", "♡")

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rep = str.format("""+----------+
| {0:<2}{1}      |
|          |
|          |
|          |
|          |
|      {1}{0:>2} |
+----------+""", self.rank, self.suit,)

        return rep


class Hand(object):

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\n"
        else:
            rep = "<EMPTY>"

        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards")
                    self.clear()
                    self.populate()
                    self.shuffle()
                    for hand in hands:
                        hand.clear()
                    self.shuffle()


class PosCard(Card):
    def __init__(self, rank, suit):
        super(PosCard, self).__init__(rank, suit)
        self.face_up = True

    def flip(self):
        self.face_up = not self.face_up

    def __str__(self):
        if self.face_up:
            rep = super(PosCard, self).__str__()
        else:
            rep = """+----------+
|          |
|  +----+  |
|  |  --|  |
|  |--  |  |
|  +----+  |
|          |
+----------+"""

        return rep


if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\nPress enter to exit.")
