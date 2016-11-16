def verify_anagrams(first_word, second_word):
    """
    You are given two words or phrase. Try to verify are they anagrams or not.
    Parameters
    ----------
    first_word, second_word - two arguments as strings
    Returns
    -------
    boolean
    """
    first_word = sorted(first_word.lower().replace(' ', ''))    # list of lower letter in word without
    second_word = sorted(second_word.lower().replace(' ', ''))  # whitespaces, sorted ascending

    if len(first_word) != len(second_word):
        return False
    else:
        if first_word != second_word:
            return False
        else:
            return True


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    # assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
