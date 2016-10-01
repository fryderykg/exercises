def checkio(numbers):
    """
    You are given the list of numbers with exactly the same length and you must find the shortest chain
    of numbers to link the first number to the last
    Parameters
    ----------
    numbers
    Numbers as a list of integers
    Returns
    -------
    The shortest chain from the first to the last number as a list of integers
    """
    digits_tree = {}
    first_element = numbers.pop(0)
    last_element = numbers[-1]

    parent_node = [first_element]
    child_node = []

    while numbers:
        for parent in parent_node:
            numbers_to_remove = []
            for number in numbers:
                if parent % 100 == number % 100 or parent // 10 == number // 10 or \
                        (parent // 100 == number // 100 and parent % 10 == number % 10):
                    digits_tree[number] = parent
                    child_node.append(number)
                    if number == last_element:
                        value = last_element
                        path = [last_element]
                        while value != first_element:
                            value = digits_tree[value]
                            path.append(value)
                        return path[-1::-1]
                    else:
                        numbers_to_remove.append(number)
            for number in numbers_to_remove:
                numbers.remove(number)
        parent_node, child_node = child_node, []


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # print(checkio([456, 455, 454, 654]))
    # print(checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]))
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"
