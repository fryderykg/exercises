def find_message(text):
    """Find a secret message"""
    secret_message = ""

    for letter in text:
        if letter.isupper():
            secret_message += letter
    return secret_message

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD"
