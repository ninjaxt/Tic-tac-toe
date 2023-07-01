# Tic-Tac-Toe

# Create an empty board
board = [' ' for _ in range(9)]

# Define the winning combinations
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
]

# Function to display the board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check for a win
def check_win(player):
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

# Function to check for a tie
def check_tie():
    return ' ' not in board

# Function to make a move
def make_move(position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

# Function to play the game
def play_game():
    player = 'X'
    while True:
        display_board()
        position = int(input("Player " + player + ", enter your move (0-8): "))
        if position < 0 or position > 8:
            print("Invalid move. Please try again.")
            continue
        if make_move(position, player):
            if check_win(player):
                display_board()
                print("Player " + player + " wins!")
                break
            elif check_tie():
                display_board()
                print("It's a tie!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Please try again.")

# Start the game
play_game()
