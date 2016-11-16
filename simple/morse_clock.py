def checkio(time_string):
    morse_dict = {'0': '.', '1': '-'}
    time_string = time_string.split(':')
    bin_time = ['00', '0000', '000', '0000', '000', '0000']  # mask of morse digit

    counter = 0     # index of bin_time
    for number in time_string:
        if len(number) == 1:
            number = '0' + number   # add missing leading zero
        for digit in number:
            digit_len = len(bin_time[counter])
            bin_time[counter] += bin(int(digit))[2:]    # add binary form of digit to bin_time, without leading '0b'
            for digit_bin in bin_time[counter]:
                # replace binary form with morse form
                bin_time[counter] = (bin_time[counter] + morse_dict[digit_bin])[-digit_len:]
            counter += 1

    return '%s %s : %s %s : %s %s' % (bin_time[0], bin_time[1], bin_time[2], bin_time[3], bin_time[4], bin_time[5])





if __name__ == '__main__':
    print(checkio("00:1:02"))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    # assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    # assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    # assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
