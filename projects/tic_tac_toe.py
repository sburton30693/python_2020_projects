# Spencer Burton
# 11/13/20
# Tic-Tac-Toe Game and AI

# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

# Build Functions
####################################

def display_instruct() :
    """Display game instructions."""
    print("""
    Welcome to the greatest intelletual challenge of all time: Tic-Tac-Toe.
    This will be a showdown betwween your human brain and my silicon processor.

    You will make your move known by entering a number, 0 - 8. The number
    will correspond to the board position as illustrated:

                            0 | 1 | 2
                            ---------
                            3 | 4 | 5
                            ---------
                            6 | 7 | 8

    Prepare yourself, human. The ultimate battle is about to begin. \n
    """)

def next_turn(turn) :
    """This function switches the turn in the game."""
    if turn == X :
        return O
    else :
        return X

def pieces() :
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")

    if go_first == "y" or go_first == "yes" :
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else :
        print("\nYour bravery will be your undoing... I will go first.")
        human = O
        computer = X
        
    return computer, human

def ask_yes_no(question) :
    """Ask a yes or no question and get back a yes or no answer."""
    response = None
    while response not in ("y", "n", "yes", "no") :
        response = input(question).lower()

    return response

def new_board() :
    """Create new game board."""
    board = []
    for i in range(NUM_SQUARES) :
        board.append(EMPTY)

    return board

def display_board(board) :
    """Display game board on screen."""
    print("\t", board[0], "|",  board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|",  board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|",  board[7], "|", board[8])

def human_move(board, human) :
    """Get human move."""
    move = None

    while move == None :
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)

    return move

def ask_number(question, low, high) :
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high) :
        response = int(input(question))

    return response
    

# Main Game
####################################

def main() :
    display_instruct()
    turn = X
    computer, human = pieces()
    board = new_board()
    while True :
        display_board(board)
        move = human_move(board, human)
        board[move] = human


main()
