def push_and_fall(board):
    n_rows = len(board)
    n_cols = len(board[0])

    # Push boxes to the right
    for row in board:
        last_box_pos = None
        for i in range(n_cols - 1, -1, -1):
            if row[i] == '#':
                last_box_pos = i
            elif last_box_pos is not None:
                row[last_box_pos], row[i] = row[i], row[last_box_pos]
                last_box_pos -= 1

    # Push boxes down
    for col in range(n_cols):
        empty_row = n_rows - 1
        for row in range(n_rows - 1, -1, -1):
            if board[row][col] == '.':
                empty_row = row
            elif board[row][col] == '#' and empty_row != row:
                board[empty_row][col], board[row][col] = board[row][col], board[empty_row][col]
                empty_row -= 1

    return board

board = [
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['#', '.', '#', '#', '.'],
    ['#', '.', '.', '.', '#'],
]

result = push_and_fall(board)
for row in result:
    print(row)
