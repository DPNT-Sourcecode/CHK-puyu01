# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    def sum(a, b):
    """
    Sums two positive integers between 0 and 100.

    :param a: a positive integer between 0-100
    :param b: a positive integer between 0-100
    :return: an integer representing the sum of the two numbers
    """
    if 0 <= a <= 100 and 0 <= b <= 100:
        return a + b
    else:
        raise ValueError("Both parameters must be between 0 and 100")
