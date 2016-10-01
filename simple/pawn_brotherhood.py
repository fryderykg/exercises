def safe_pawns(pawns):
    safe = 0
    column = 'zabcdefghz'

    for pawn in pawns:
        col = column.index(pawn[0])
        row = pawn[1]
        new_col1 = column[(col - 1)]
        new_col2 = column[col + 1]
        new_row = str(int(row) - 1)
        x = (new_col1 + new_row)
        x2 = (new_col2 + new_row)

        if x in pawns or x2 in pawns:
            safe += 1

    return safe



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"a4", "d4", "f4", "c3", "e3", "h5", "d2"}) == 5
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

