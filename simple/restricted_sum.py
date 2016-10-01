def checkio(data):
    """
    calculate the sum of numbers avoiding word: sum, import, for, while, reduce
    Parameters
    ----------
    data
    A list of numbers
    Returns
    -------
    The sum of numbers
    """
    if not data:
        return 0
    else:
        return data[0] + checkio(data[1:])


data = [1,2,3,4,5]
print(checkio(data))
