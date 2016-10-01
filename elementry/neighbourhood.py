def count_neighbours(grid, row, col):
    grid_width = len(grid[0])
    grid_height = len(grid)
    new_row = [row - 1, row, row + 1]  # surrounding cells
    new_col = [col - 1, col, col + 1]  # surrounding cells
    chips = 0  # numbers of chips found
    if grid[row][col] == 1:
        chips -= 1
    for row in new_row:
        if 0 <= row < grid_height:  # to prevent go out the grid
            for col in new_col:
                if 0 <= col < grid_width:  # to prevent go out the grid
                    if grid[row][col] == 1:
                        chips += 1
    return chips


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary
    # for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
