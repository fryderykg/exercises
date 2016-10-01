import time


def checkio2(board):
    # First we put everything together into a single string
    x = "".join(board)

    # Next we outline the 8 possible winning combinations.
    combos = ["012", "345", "678", "036", "147", "258", "048", "246"]

    # We go through all the winning combos 1 by 1 to see if there are any
    # all Xs or all Os in the combos
    for i in combos:
        if x[int(i[0])] == x[int(i[1])] == x[int(i[2])] and x[int(i[0])] in "XO":
            return x[int(i[0])]
    return "D"


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

game_result = ["X.O",
               "XX.",
               "XOO"]

start_1 = time.time()
# first function
checkio2(game_result)
stop_1 = time.time()


start_2 = time.time()
#  second function
checkio(game_result)
stop_2 = time. time()

function1_time = stop_1 - start_1
function2_time = stop_2 - start_2
diference = function1_time - function2_time
print('function 1 execution time is: %f' % function1_time)
print('function 2 execution time is: %f' % function2_time)
print('Diference is: %f' % diference)
