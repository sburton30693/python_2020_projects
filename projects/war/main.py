# Spencer Burton
# 12/21/2020
# Game of War in Python

import playing_cards
import random

STATUS_START = "===== CURRENT STATS ====="
STATUS_END   = "========================="
STATUS_FORMAT = "{}\n - You: {:2>} cards\n - Com: {:2>} cards\n{}"

# This will determine whether to shuffle the cards when giving them to a player
SHUFFLE_AFTER_ROUND = False

TITLE_ART = """
 ____    __    ____  ___      .______      
 \   \  /  \  /   / /   \     |   _  \     
  \   \/    \/   / /  ^  \    |  |_)  |    
   \            / /  /_\  \   |      /     
    \    /\    / /  _____  \  |  |\  \-.
     \__/  \__/ /__/     \__\ | _| `.__|
"""

TITLE_EXPLAIN = """
The game of War is simple. The rules are as follow:
 1. The deck is divided in half between each player.
 2. At the start of each round both players play one card face up.
 3. The card with the higher rank wins and the winner puts both cards at the bottom of their hand.
 4. But if both card's ranks are the same a "War" is started.
 5. For a war, each player places 3 cards face down, or less if they can't, then one face up. It 
    then repeats, so double or more wars can possibly occur. The winner gets all the cards.
 6. If a player runs out of cards during a war, then the last card they placed is used.
 7. The game ends when one player gets all 52 cards. That player is then declared the winner.

DISCLAIMER: This game can take a really long time to end.
"""


def start_screen():
    title = str.format("--Program created by Spencer Burton--\n\nWelcome to the game of{}\n{}", TITLE_ART, TITLE_EXPLAIN)
    print(title)
    input("Press Enter to Start...")


def ask_shuffle():
    global SHUFFLE_AFTER_ROUND
    
    # Ask whether they want shuffling after rounds on
    print("\nWould you like to have the cards shuffled before being given\nto the winning player, it should help minimize infinite loops.")
    choice = input("(y or n)? ")

    if choice.lower() in ("y", "yes"):
        SHUFFLE_AFTER_ROUND = True


def status_screen(player1, player2):
    status_screen = str.format(STATUS_FORMAT, STATUS_START, player1.card_count(), player2.card_count(), STATUS_END)
    print(status_screen)


def print_vs(hand1, hand2):
    print("\nYou:")
    print(hand1)
    print("\n - vs - \n")
    print(hand2, "\n")


def give_all_cards(player, hands):
    all_cards = playing_cards.Hand()

    # Add all cards from the hands into one hand
    for hand in hands:
        while not hand.is_empty():
            hand.give(hand.get_top(), all_cards)

    if SHUFFLE_AFTER_ROUND:
        all_cards.shuffle()

    while not all_cards.is_empty():
        all_cards.give(all_cards.get_top(), player)


def card_value(rank):
    if rank in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
        return int(rank)
    else:
        if rank == "J":
            return 11
        elif rank == "Q":
            return 12
        elif rank == "K":
            return 13
        elif rank == "A":
            return 14


def do_round(player1, player2):
    # Create the "Table's Hands"
    table1 = playing_cards.Hand()
    table2 = playing_cards.Hand()
    
    # Give the top card of each players hand to the table
    player1.give(player1.get_top(), table1)
    player2.give(player2.get_top(), table2)

    # Print them
    print_vs(table1, table2)

    # Determine if there is a war or who the winner is
    rank1 = card_value(table1.get_top().rank)
    rank2 = card_value(table2.get_top().rank)

    if rank1 == rank2:
        # Do a war
        print("War!")
        input("\nPress Enter to Continue...")
        do_war(player1, player2, table1, table2)
    elif rank1 > rank2:
        # Declare player1 the winner
        print("You Won!")
        give_all_cards(player1, [table1, table2])
    elif rank1 < rank2:
        # Declare player1 the loser
        print("You Lost.")
        give_all_cards(player2, [table1, table2])

    # Flip all the cards up so they display properly
    player1.flip_all_up()
    player2.flip_all_up()

    
def do_war(player1, player2, table1, table2):
    # Check if one player has an empty hand then they use the last card played
    # for the next war(s). If both players are out then it is a draw, and they
    # are both left with zero for the check_winner function to check for.
    if player1.is_empty() and player2.is_empty():
        return
    elif player1.is_empty():
        print("You're all out of cards, You use the last card played.")
    elif player2.is_empty():
        print("The other player is all out of cards, they will use the last card played.")

    # Give the each table three face down cards and a face up card from the players
    # And only put down cards if the player has enough 
    for i in range(3):
        if player1.card_count() > 1:
            player1.get_top().flip_down()
            player1.give(player1.get_top(), table1)
        if player2.card_count() > 1:
            player2.get_top().flip_down()
            player2.give(player2.get_top(), table2)

    if not player1.is_empty():
        player1.give(player1.get_top(), table1)
    if not player2.is_empty():
        player2.give(player2.get_top(), table2)

    # Print it
    print_vs(table1, table2)

    # Determine the winner
    rank1 = card_value(table1.get_bottom().rank)
    rank2 = card_value(table2.get_bottom().rank)

    if rank1 == rank2:
        # Do another war
        print("War!")
        input("\nPress Enter to Continue...")
        do_war(player1, player2, table1, table2)
    elif rank1 > rank2:
        # Declare player1 the winner
        print("You Won!")
        give_all_cards(player1, [table1, table2])
    elif rank1 < rank2:
        # Declare player1 the loser
        print("You Lost.")
        give_all_cards(player2, [table1, table2])



def check_winner(player1, player2):
    if (player1.card_count() == 52) and (player2.card_count() == 0):
        return 0
    elif (player1.card_count() == 0) and (player2.card_count() == 52):
        return 1
    elif (player1.card_count() == 0) and (player2.card_count() == 0):
        return 2 # A draw
    else: 
        return -1


def main():
    # Print start screen to explain the game
    start_screen()

    # Ask if the user want the cards shuffled after each round
    ask_shuffle()
    
    # Create both players
    player_user = playing_cards.Hand()
    player_com  = playing_cards.Hand()
    players = [player_user, player_com]

    # Create deck and deal each player half the deck, one card at a time
    deck = playing_cards.Deck()
    deck.populate()
    deck.shuffle()
    deck.deal(players, 26)

    # Loop until someone wins
    win = -1
    round = 1

    while win == -1:
        # Do one round of War
        print("\nRound:", round)
        do_round(player_user, player_com)
        print()
        
        # Print the status
        status_screen(player_user, player_com)
        
        # Check for a winner
        win = check_winner(player_user, player_com)
        
        # Wait for user to continue
        input("\nPress Enter to Continue...")
        
        round += 1

    # Print the win or loss message
    if win == 0:
        print("\n Congratulations! You Won")
    elif win == 1:
        print("\n Unfortunately, You Lost")
    elif win == 2:
        print("\n Wow, You got a Draw")

    # Wait for input before closing
    input("\nPress Enter to Exit...")


main()
