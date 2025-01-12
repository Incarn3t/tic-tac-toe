import random

# Board setup
board = [["_", "\t|\t", "_", "\t|\t", "_"],
         ["_", "\t|\t", "_", "\t|\t", "_"],
         ["_", "\t|\t", "_", "\t|\t", "_"]]

# Function to print the board
def print_board():
    for i in range(3):
        for j in range(5):
            print(board[i][j], end="")
        print()
    print()

# Bot move
def bot():
    while True:
        x = random.randint(0, 2)
        y = random.choice([0, 2, 4])
        if board[x][y] == "_":
            board[x][y] = to1
            break

# Player 1 move
def player1():
    while True:
        try:
            x = int(input("Player 1: Enter the row (0, 1, 2): "))
            y = int(input("Player 1: Enter the column (0, 2, 4): "))
            if board[x][y] == "_":
                board[x][y] = to2
                break
            else:
                print("Invalid move! The position is already taken.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter valid row and column numbers.")

# Player 2 move
def player2():
    while True:
        try:
            x = int(input("Player 2: Enter the row (0, 1, 2): "))
            y = int(input("Player 2: Enter the column (0, 2, 4): "))
            if board[x][y] == "_":
                board[x][y] = to1
                break
            else:
                print("Invalid move! The position is already taken.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter valid row and column numbers.")

# Check for win
def win():
    # Horizontal
    for row in board:
        if row[0] == row[2] == row[4] != "_":
            return True
    # Vertical
    for col in [0, 2, 4]:
        if board[0][col] == board[1][col] == board[2][col] != "_":
            return True
    # Diagonal
    if board[0][0] == board[1][2] == board[2][4] != "_" or board[0][4] == board[1][2] == board[2][0] != "_":
        return True
    return False

# Check for draw
def is_draw():
    for row in board:
        if "_" in row:
            return False
    return True

# Main game
print_board()
ch = int(input("1) Computer\n2) Co-player\nChoose an option: "))

if ch == 1:
    sy2 = int(input("Choose your symbol:\n1) X\n2) O\nEnter choice: "))
    to2, to1 = ("X", "O") if sy2 == 1 else ("O", "X")

    while True:
        player1()
        if win():
            print("You win!!")
            break
        if is_draw():
            print("It's a draw!")
            break
        bot()
        print_board()
        if win():
            print("You lose!")
            break
        if is_draw():
            print("It's a draw!")
            break

elif ch == 2:
    sy2 = int(input("Player 1: Choose your symbol:\n1) X\n2) O\nEnter choice: "))
    to2, to1 = ("X", "O") if sy2 == 1 else ("O", "X")

    while True:
        player1()
        print_board()
        if win():
            print("Player 1 wins!!")
            break
        if is_draw():
            print("It's a draw!")
            break
        player2()
        print_board()
        if win():
            print("Player 2 wins!!")
            break
        if is_draw():
            print("It's a draw!")
            break
