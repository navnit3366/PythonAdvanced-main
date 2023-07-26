from math import ceil


def sign_choice(player):
    choice = input(f"{player}, would you like to play with 'X' or 'O'?")
    if choice in ["X", "O"]:
        return choice
    else:
        print("Only 'X' and 'O' are allowed signs !")
        sign_choice(player)


def setup():
    global player_one, player_two
    player_one_name = input("Player one name : ")
    player_two_name = input("Player two name : ")
    # player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'?")
    player_one_sign = sign_choice(player_one_name)
    player_two_sign = "X" if player_one_sign == "O" else "O"
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("This is numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{player_one_name} starts first!")


def draw_board(board):
    for row in board:
        print('| ', end="")
        print(' | '.join([str(x) for x in row]), end="")
        print('| ')


def check_if_won(curr, board):
    global loop
    first_row = all([x == current[1] for x in board[0]])
    second_row = all([x == current[1] for x in board[1]])
    third_row = all([x == current[1] for x in board[2]])
    first_col = all([board[ro][0] == current[1] for ro in range(len(board))])
    second_col = all([board[ro][1] == current[1] for ro in range(len(board))])
    third_col = all([board[ro][2] == current[1] for ro in range(len(board))])
    first_diagonal = all(x == current[1] for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == current[1] for x in [board[0][2], board[1][1], board[2][0]])
    if any([first_row, second_row, third_row,
            first_col, second_col, third_col,
            first_diagonal, second_diagonal]):
        print(f"{current[0]} won!")
        loop = False


def field_choice(f_pos):
    f_choice = int(input(f"{current[0]} choose a free position [{', '.join([str(x) for x in f_pos])}]: "))

    while f_choice not in f_pos:
        print("*" * 50)
        print(f"field {f_choice} is not free - available are numbers [{', '.join([str(x) for x in free_positions])}]")
        print("*" * 50)
        f_choice = int(input(f"Player {current[0]}, choose a free position [{', '.join([str(x) for x in f_pos])}]: "))

    f_pos.remove(f_choice)
    return f_choice


def play(current, board, free_positions):
    # choice = int(input(f"{current[0]} choose a free position [1-9]: "))
    # #this is the original game question without field_choice function
    choice = field_choice(free_positions)
    row = ceil(choice / 3 - 1)
    col = choice % 3 - 1
    board[row][col] = current[1]
    draw_board(board)
    check_if_won(current, board)


player_one = None
player_two = None
board = [[" ", " ", " "] for x in range(3)]
free_positions = {1, 2, 3, 4, 5, 6, 7, 8, 9}

setup()
current = player_one
other = player_two
loop = True

while loop:
    play(current, board, free_positions)
    current, other = other, current
