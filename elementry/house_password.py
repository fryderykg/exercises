def checkio(data):
    import re
    upper = re.findall(r'([A-Z]+)', data)
    lower = re.findall(r'([a-z]+)', data)
    number = re.findall(r'([0-9]+)', data)
    return True if upper and lower and number and len(data) >= 10 else False


#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
