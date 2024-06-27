def check_win(row1, row2, row3):
    count = 0
    # Rows for X
    if row1[0] == "X" and row1[1] == "X" and row1[2] == "X":
        return "xwin"
    elif row2[0] == "X" and row2[1] == "X" and row2[2] == "X":
        return "xwin"
    elif row3[0] == "X" and row3[1] == "X" and row3[2] == "X":
        return "xwin"
    # Columns for X
    elif row1[0] == "X" and row2[0] == "X" and row3[0] == "X":
        return "xwin"
    elif row1[1] == "X" and row2[1] == "X" and row3[1] == "X":
        return "xwin"
    elif row1[2] == "X" and row2[2] == "X" and row3[2] == "X":
        return "xwin"
    # Diagonals for X
    elif row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
        return "xwin"
    elif row3[0] == "X" and row2[1] == "X" and row1[2] == "X":
        return "xwin"
    # Rows for O
    elif row1[0] == "O" and row1[1] == "O" and row1[2] == "O":
        return "owin"
    elif row2[0] == "O" and row2[1] == "O" and row2[2] == "O":
        return "owin"
    elif row3[0] == "O" and row3[1] == "O" and row3[2] == "O":
        return "owin"
    # Columns for O
    elif row1[0] == "O" and row2[0] == "O" and row3[0] == "O":
        return "owin"
    elif row1[1] == "O" and row2[1] == "O" and row3[1] == "O":
        return "owin"
    elif row1[2] == "O" and row2[2] == "O" and row3[2] == "O":
        return "owin"
    # Diagonals for O
    elif row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
        return "owin"
    elif row3[0] == "O" and row2[1] == "O" and row1[2] == "O":
        return "owin"
    # Return no win
    return "nowin"

def print_grid():
    print(row1[0], end = " ")
    print(row1[1], end = " ")
    print(row1[2])
    print(row2[0], end = " ")
    print(row2[1], end = " ")
    print(row2[2])
    print(row3[0], end = " ")
    print(row3[1], end = " ")
    print(row3[2])

row1 = ["--","--","--"]
row2 = ["--","--","--"]
row3 = ["--","--","--"]

while True:
    print_grid()
    playerXrow = int(input("What row player X? "))
    playerXColumn = int(input("What column player X? "))
    if playerXrow == 1:
        row1[playerXColumn - 1] = "X"
    if playerXrow == 2:
        row2[playerXColumn - 1] = "X"
    if playerXrow == 3:
        row3[playerXColumn - 1] = "X"
    win_checker = check_win(row1, row2, row3)
    if win_checker == "xwin":
        print("X you won!")
        break
    elif win_checker == "owin":
        print("O you won!")
        break
    print_grid()
    playerOrow = int(input("What row player O? "))
    playerOColumn = int(input("What column player O? "))
    if playerOrow == 1:
        row1[playerOColumn - 1] = "O"
    if playerOrow == 2:
        row2[playerOColumn - 1] = "O"
    if playerOrow == 3:
        row3[playerOColumn - 1] = "O"
    win_checker = check_win(row1, row2, row3)
    if win_checker == "xwin":
        print("X you won!")
        break
    elif win_checker == "owin":
        print("O you won!")
        break
