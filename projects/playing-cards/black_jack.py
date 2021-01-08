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

    def __str__(self):
        print("###################################")
        for card in self.cards:
            print(card)
        rep = "###################################"
        rep += "\n" + self.name
        rep += "\n" + self.total
        return rep

    @property
    def total(self):
        # If a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None

        # Add up  card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value

        # Determine if hand contains Ace
        has_ace = False
        for card in self.cards:
            if card.value == BJCard.ACE_VALUE
                has_ace = True

        # If hand contains Ace and total is low enough, treat Ace as 11
        if has_ace and t <= 11:
            t += 10 # Only add ten since we already added 1 for Ace

        return t

    def is_busted(self):
        return self.total > 21


class BJPlayer(BJHand):

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")

    def is_hitting(self):
        response = gf.get_yes_no("\n" + self.name + ", do you want to hit? (Y/N): ")
        return response


class BJDealer(BJHand):

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.)

    def flip_first_card(self):
        self.cards[0].flip()


class Game(object):

    def __init__(self, names):
        self.deck = BJDeck()
        self.deck.populate()
        self.deck.shuffle()
        self.dealer = BJDealer("Dealer Tim")
        self.players = []
        
        for name in names:
            self.players.append(BJPlayer(name))

    @property
    def still_playing(self):
        sp = []

        for player in self.players:
            if not player.is_busted():
                sp.append(player)

        return sp
        


# Testing Area
deck = BJDeck()
deck.populate()
deck.shuffle()

card = deck.cards[0]
print(card)
print(card.value)
