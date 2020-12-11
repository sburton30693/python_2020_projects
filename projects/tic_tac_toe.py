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

def legal_moves(board) :
    moves = []

    for square in range(NUM_SQUARES) :
        if board[square] == EMPTY :
            moves.append(square)
        
    return moves

def human_move(board, human) :
    """Get human move."""
    legal = legal_moves(board)
    move = None

    while move not in legal :
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)

        if move not in legal :
            print("\nThat square is already occupied, foolish human. Choose another. \n")

    print("Fine...")
    return move

def ask_number(question, low, high) :
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high) :
        try :
            response = int(input(question))
        except :
            continue

    return response
    
def winner(board) :
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2), # Horizontals
                   (3, 4, 5),
                   (6, 7, 8),
                   # Verticals
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   # Diagonals
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN :
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY :
            return board[row[0]]
        
    if EMPTY not in board :
        return TIE

    return None

def computer_move(board, computer, human) :
    """Make computer move."""
    # Make a copy so the actual board isn't messed with
    cboard = board[:]
    # The best position to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number", end=" ")
    # If computer can win, take that move
    for move in legal_moves(board) :
        cboard[move] = computer
        if winner(cboard) == computer :
            print(move)
            return move
        # Done checking this move, undo it
        cboard[move] = EMPTY
        
    # If human can win, block that move
    for move in legal_moves(board) :
        cboard[move] = human
        if winner(cboard) == human :
            print(move)
            return move
        # Done checking this move, undo it
        cboard[move] = EMPTY

    # Since no one can win on next move, pick best open square
    for move in BEST_MOVES :
        if move in legal_moves(board) :
            print(move)
            return move

# Main Game
####################################

def main() :
    display_instruct()
    turn = X
    computer, human = pieces()
    board = new_board()
    win = None
    
    while not win :
        if turn == human :
            move = human_move(board, human)
            board[move] = human
        else :
            move = computer_move(board, computer, human)
            board[move] = computer

        turn = next_turn(turn)
        display_board(board)
        win = winner(board)
    
    if win == human :
        print("\nCongratulations Human")
    elif win == computer :
        print("\nLooks like I win")
    elif win == TIE :
        print("\nYou won't be so lucky next time")

main()
