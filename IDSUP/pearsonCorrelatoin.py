import numpy as np


def pearson_correlation(x, y):
    """
    Calculate Pearson correlation coefficient between two lists x and y.

    Args:
        x: List of numerical values.
        y: List of numerical values.

    Returns:
        Pearson correlation coefficient between x and y.
    """
    # Convert lists to numpy arrays
    x_array = np.array(x)
    y_array = np.array(y)

    # Calculate means
    x_mean = np.mean(x_array)
    y_mean = np.mean(y_array)

    # Calculate Pearson correlation coefficient
    numerator = np.sum((x_array - x_mean) * (y_array - y_mean))
    denominator = np.sqrt(np.sum((x_array - x_mean) ** 2) * np.sum((y_array - y_mean) ** 2))
    pearson_coefficient = numerator / denominator

    return pearson_coefficient


# Example usage:
x = [600,800,1000]
y = [1200,1000,2000]

print("Pearson correlation coefficient:", pearson_correlation(x, y))
