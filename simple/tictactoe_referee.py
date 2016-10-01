def checkio(game_result):
    grid_size = len(game_result)
    win_combination = []

    for x in range(grid_size):  # append list of rows
        win_combination.append([game_result[x][y] for y in range(grid_size)])

    for y in range(grid_size):  # append lis of columns
        win_combination.append([game_result[x][y] for x in range(grid_size)])

    # append first diagonal to win combination
    win_combination.append([game_result[x][x] for x in range(grid_size)])

    # append second diagonal to win combination
    xx, xy = 0, grid_size - 1
    diag_value = [] # temporary list of diagonal diag_value
    while xy > -1:
        diag_value.extend([game_result[xx][xy]])
        xx += 1
        xy -= 1
    win_combination.append(diag_value)

    # check each list in win_combination for 3 the same value
    for item in win_combination:
        if item.count('X') == 3:
            return "X"
        elif item.count('O') == 3:
            return "O"
    return "D"



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
