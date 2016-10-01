def checkio(data):
    roman_number = ""

    thousands = data // 1000
    data %= 1000

    hundrets = data // 100
    data %= 100

    tens = data // 10
    data %= 10

    if thousands:
        roman_number += thousands * "M"
    if hundrets:
        if hundrets == 1:
            roman_number += "C"
        elif hundrets == 2:
            roman_number += "CC"
        elif hundrets == 3:
            roman_number += "CCC"
        elif hundrets == 4:
            roman_number += "CD"
        elif hundrets == 5:
            roman_number += "D"
        elif hundrets == 6:
            roman_number += "DC"
        elif hundrets == 7:
            roman_number += "DCC"
        elif hundrets == 8:
            roman_number += "DCCC"
        elif hundrets == 9:
            roman_number += "CM"

    if tens:
        if tens == 1:
            roman_number += "X"
        elif tens == 2:
            roman_number += "XX"
        elif tens == 3:
            roman_number += "XXX"
        elif tens == 4:
            roman_number += "XL"
        elif tens == 5:
            roman_number += "L"
        elif tens == 6:
            roman_number += "LX"
        elif tens == 7:
            roman_number += "LXX"
        elif tens == 8:
            roman_number += "LXXX"
        elif tens == 9:
            roman_number += "XC"

    if data:
        if data == 1:
            roman_number += "I"
        elif data == 2:
            roman_number += "II"
        elif data == 3:
            roman_number += "III"
        elif data == 4:
            roman_number += "IV"
        elif data == 5:
            roman_number += "V"
        elif data == 6:
            roman_number += "VI"
        elif data == 7:
            roman_number += "VII"
        elif data == 8:
            roman_number += "VIII"
        elif data == 9:
            roman_number += "IX"

    return roman_number

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(3200) == 'MMMCC', '2000'
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'

print(checkio(3888))