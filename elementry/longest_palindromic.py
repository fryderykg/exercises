# def is_palindrome(text):
#     if text[::-1] == text:
#         return True
#     else:
#         return False


def longest_palindromic(text):
    longest_palin = ""
    for i in range(len(text)):
        for j in range(len(text)+1):
            if is_palindrome(text[i:j]) and len(text[i:j]) > len(longest_palin):
                longest_palin = text[i:j]

    return longest_palin


def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0].lower() == s[-1].lower():
        return is_palindrome(s[1:-1])
    else:
        return False

text = "artrartrt"
print(text[::-1])

print(longest_palindromic("artrartrt"))

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
