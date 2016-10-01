def checkio(text):
    text = text.lower()
    letters_count = 0
    find_letter = ''
    letters = 'abcdefghijklmnopqrstuwxyz'

    for letter in letters:
        if 0 < text.count(letter) > letters_count:
            find_letter = letter
            letters_count = text.count(letter)

    return find_letter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
