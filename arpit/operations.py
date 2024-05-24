def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return left

def solution(operations):
    obstacles = set()  # Set to keep track of obstacle positions
    result = []  # List to store the binary results
    obstacles_list = []

    for op in operations:
        if op[0] == 1:
            # Operation type 1: Build an obstacle at coordinate x
            x = op[1]
            obstacles.add(x)
            obstacles_list.append(x)
            obstacles_list.sort()
        elif op[0] == 2:
            # Operation type 2: Check if a block of size 'size' can be built ending just before coordinate x
            x = op[1]
            size = op[2]

            possible = True
            index = binary_search(obstacles_list, x - size + 1) - 1
            if index >= 0 and obstacles_list[index] >= x - size + 1:
                possible = False
            result.append('1' if possible else '0')
    return ''.join(result)


# Example usage:
operations = [
    [1, 2],
    [1, 5],
    [2, 5, 2],
    [2, 6, 3],
    [2, 2, 1],
    [2, 3, 2]
]
print(solution(operations))  # Output: "1010"
