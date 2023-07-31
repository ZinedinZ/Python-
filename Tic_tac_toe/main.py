import os

board_x = [
    ["a1", "a2", "a3"],
    ["b1", "b2", "b3"],
    ["c1", "c2", "c3"]
]
game_on = True


def show_board():
    row1 = " | ".join(board_x[0])
    row2 = " | ".join(board_x[1])
    row3 = " | ".join(board_x[2])
    print(row1)
    print(row2)
    print(row3)


def check_winner(row, player):
    global board_x
    for i in range(3):
        if row[i][0] == row[i][1] == row[i][2] == player:
            return True
    for n in range(3):
        if row[0][n] == row[1][n] == row[2][n] == player:
            return True
    if row[0][0] == row[1][1] == row[2][2] == player:
        return True

    elif row[0][2] == row[1][1] == row[2][0] == player:
        return True
    else:
        return False


def x_sign(x_input):
    global board_x, game_on
    # Function to add X sign in players field
    for n in range(len(board_x)):
        for i in range(len(board_x[n])):
            if board_x[n][i] == x_input:
                board_x[n][i] = "\033[31mX\033[0m"
    os.system("cls")
    show_board()


def o_sign(o_input):
    global board_x, game_on
    # Function to add O sign in players field
    for col in range(len(board_x)):
        for row in range(len(board_x)):
            if board_x[col][row] == o_input:
                board_x[col][row] = "\033[32mO\033[0m"
    os.system("cls")
    if check_winner(board_x, "\033[32mO\033[0m"):
        game_on = False
        print("Player O Wins")
    show_board()


show_board()

while game_on:
    x_player = input("X Player is on move: Where you want to put a sign? ")
    if check_winner(board_x, "\033[31mX\033[0m"):
        print("Player X Wins")
        game_on = False
    elif x_player in board_x[0] or x_player in board_x[1] or x_player in board_x[2]:
        x_sign(x_player)
        if check_winner(board_x, "\033[32mO\033[0m"):
            print("Player O Wins")
            game_on = False
            break
        elif check_winner(board_x, "\033[31mX\033[0m") is not True:
            o_player = input(" O Player is on move: Where you want to put a sign? ")
            if o_player in board_x[0] or o_player in board_x[1] or o_player in board_x[2]:
                o_sign(o_player)
            else:
                break
        else:
            print("Player X Wins")
            break
    else:
        print("That field doesn't exis please try again")
