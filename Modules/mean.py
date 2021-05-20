from Modules.sum import summation


def mean(numbers):
    """
    Calculate the mean of a list of numbers
    Args:
        numbers: int, float

    Returns: float

    """
    return 1.0 * summation(numbers)/len(numbers)
