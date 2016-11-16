def checkio(a, b, c):
    """
    You are given the lengths for each side on a triangle. You need to find all three angles for this triangle
    Parameters
    ----------
    a, b, c - The lengths of the sides of a triangle as integers

    Returns
    -------
    Angles of a triangle in degrees as sorted list of integers
    """
    import math

    try:
        assert a < b + c  # check if the given side lengths can form a triangle
        assert b < a + c
        assert c < a + b
    except AssertionError:
        return [0, 0, 0]

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    alfa = math.degrees(math.asin((2 * area) / (b * c)))
    beta = math.degrees(math.asin((2 * area) / (a * c)))
    gamma = 180 - (alfa + beta)
    angles = [alfa, beta, gamma]
    return sorted(map(round, angles))


#  These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio(10, 20, 30))
    # assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    # assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    # assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
