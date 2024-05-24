def solution(matrix, turns):
    n = len(matrix)

    # Normalize the number of turns to be in the range [0, 4)
    turns = turns % 4

    # Define the segments based on main diagonals
    diagonal1 = [matrix[i][i] for i in range(n)]  # Top-left to bottom-right
    diagonal2 = [matrix[i][n - 1 - i] for i in range(n)]  # Top-right to bottom-left
    upper_left = [matrix[i][j] for i in range(n) for j in range(i)]  # Upper triangle (excluding main diagonal)
    lower_right = [matrix[i][j] for i in range(n) for j in range(i + 1, n)]  # Lower triangle (excluding main diagonal)

    # Rotate segments based on turns
    if turns == 1:
        diagonal1, diagonal2, upper_left, lower_right = diagonal2, diagonal1, lower_right, upper_left
    elif turns == 2:
        diagonal1, diagonal2, upper_left, lower_right = diagonal2[::-1], diagonal1[::-1], lower_right[::-1], upper_left[
                                                                                                             ::-1]
    elif turns == 3:
        diagonal1, diagonal2, upper_left, lower_right = diagonal2, diagonal1, lower_right, upper_left

    # Reassemble the matrix using rotated segments
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        rotated_matrix[i][i] = diagonal1[i]  # Place elements on the first diagonal
        rotated_matrix[i][n - 1 - i] = diagonal2[i]  # Place elements on the second diagonal

    idx = 0
    for i in range(n):
        for j in range(i):
            rotated_matrix[i][j] = upper_left[idx]  # Fill upper left triangle
            rotated_matrix[j][i] = lower_right[idx]  # Fill lower right triangle
            idx += 1

    return rotated_matrix


# Test the function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
turns = 6
result = solution(matrix, turns)
print(result)
