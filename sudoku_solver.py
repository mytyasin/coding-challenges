board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]

]

board_len = range(len(board))


def print_board(brd):
    for row in board_len:
        if row % 3 == 0 and row != 0:
            print('-----------------------')
        for col in board_len:
            if col % 3 == 0 and col != 0:
                print(' | ', end='')
            if col == 8:
                print(brd[row][col])
            else:
                print(str(brd[row][col]) + ' ', end='')


def empty(brd):
    for row, value in enumerate(board_len):
        for col, value2 in enumerate(board_len):
            if brd[row][col] == 0:
                return row, col

    return None


def validate_grid(brd, number, position):
    x = position[1] // 3
    y = position[0] // 3

    for row in range(y * 3, y * 3 + 3):
        for col in range(x * 3, x * 3 + 3):
            if brd[row][col] == number:
                return False
    return True


def validate_row(brd, number, position):
    for row in board_len:
        if brd[position[0]][row] == number:
            return False
    return True


def validate_col(brd, number, position):
    for col in board_len:
        if brd[col][position[1]] == number:
            return False
    return True


def valid(brd, number, position):
    grid = validate_grid(brd, number, position)
    row = validate_row(brd, number, position)
    col = validate_col(brd, number, position)

    if row and col and grid:
        return True
    else:
        return False


def complete(brd):
    is_empty = empty(brd)
    if is_empty:
        row, col = is_empty
    else:
        return True

    for num in range(1, 10):
        if valid(brd, num, (row, col)):
            brd[row][col] = num

            if complete(brd):
                return True
            brd[row][col] = 0

    return False

import time
print_board(board)
start = time.perf_counter()
complete(board)

print(f'runtime = {time.perf_counter() - start:.3f}s')
print('#########################')
print('Solution')
print('#########################')
print_board(board)
