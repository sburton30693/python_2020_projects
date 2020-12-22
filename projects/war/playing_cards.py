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
        self.face_up = True

    def flip_down(self):
        self.face_up = False

    def flip_up(self):
        self.face_up = True

    def __str__(self):
        rank = self.rank
        suit = self.suit

        if not self.face_up:
            rank = " "
            suit = " "

        rep = str.format("""+------+
|{0:<2}{1}   |
|      |
|   {1}{0:>2}|
+------+""", rank, suit,)

        return rep


class Hand(object):

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = "+------+ " * len(self.cards) + "\n"

            for card in self.cards:
                if card.face_up:
                    rep += str.format("|{0:<2}{1}   | ", card.rank, card.suit)
                else:
                    rep += "|      | "

            rep += "\n" + "|      | " * len(self.cards) + "\n"
            
            for card in self.cards:
                if card.face_up:
                    rep += str.format("|   {1}{0:>2}| ", card.rank, card.suit)
                else:
                    rep += "|      | "

            rep += "\n" + "+------+ " * len(self.cards)
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

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def card_count(self):
        return len(self.cards)

    def is_empty(self):
        return len(self.cards) == 0

    def get_top(self):
        return self.cards[0]

    def get_bottom(self):
        return self.cards[len(self.cards) - 1]

    def flip_all_up(self):
        for card in self.cards:
            card.flip_up()


class Deck(Hand):

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
                    self.deal(hands, per_hand)
