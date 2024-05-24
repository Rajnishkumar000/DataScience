def push_and_fall(board):
    if not board or not board[0]:
        return board

    rows = len(board)
    cols = len(board[0])

    # Perform gravity operation (push and fall) for each column
    for col in range(cols):
        # Gather all objects '#' in the current column
        objects = []
        for row in range(rows):
            if board[row][col] == '#':
                objects.append('#')

        # Determine the number of empty spaces needed below the objects
        num_empty_spaces = rows - len(objects)

        # Fill the column with '.' (empty spaces) from the bottom
        for row in range(rows - 1, -1, -1):
            if num_empty_spaces > 0:
                if board[row][col] == '#':
                    num_empty_spaces -= 1
            else:
                # Shift objects '#' downwards to fill empty spaces '.'
                if objects:
                    board[row][col] = objects.pop()
                else:
                    board[row][col] = '.'

    return board


# Example usage:
board = [
    ['.', '#', '.', '.','.'],
    ['.', '.', '.', '.','.'],
    ['#', '.', '#', '#','.'],
    ['#', '.', '.', '.','#']
]

result = push_and_fall(board)
for row in result:
    print(' '.join(row))