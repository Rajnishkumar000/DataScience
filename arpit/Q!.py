def solution(numbers, threshold):
    # Iterate over the array from the start to the third last element
    for i in range(len(numbers) - 2):
        # Check if three consecutive elements meet the threshold condition
        if numbers[i] > threshold and numbers[i + 1] > threshold and numbers[i + 2] > threshold:
            # Return the index i if the condition is met
            return i
    # If no such index is found, return -1
    return -1

# Example usage:
numbers = [0, 1, 4, 3, 2, 5]
threshold = 1
print(solution(numbers, threshold))  # Output: 2