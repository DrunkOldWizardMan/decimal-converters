def base64():
    a_list = []
    a = input("number: ")
    aint = int(a)
    while aint != 0:
        add = aint % 64
        a_list.append(add)
        aint //= 64
    list.reverse(a_list)
    output = ""
    for digit in a_list:
        if digit == 0:
            output += "A"
        elif digit == 1:
            output += "B"
        elif digit == 2:
            output += "C"
        elif digit == 3:
            output += "D"
        elif digit == 4:
            output += "E"
        elif digit == 5:
            output += "F"
        elif digit == 6:
            output += "G"
        elif digit == 7:
            output += "H"
        elif digit == 8:
            output += "I"
        elif digit == 9:
            output += "J"
        elif digit == 10:
            output += "K"
        elif digit == 11:
            output += "L"
        elif digit == 12:
            output += "M"
        elif digit == 13:
            output += "N"
        elif digit == 14:
            output += "O"
        elif digit == 15:
            output += "P"
        elif digit == 16:
            output += "Q"
        elif digit == 17:
            output += "R"
        elif digit == 18:
            output += "S"
        elif digit == 19:
            output += "T"
        elif digit == 20:
            output += "U"
        elif digit == 21:
            output += "V"
        elif digit == 22:
            output += "W"
        elif digit == 23:
            output += "X"
        elif digit == 24:
            output += "Y"
        elif digit == 25:
            output += "Z"
        elif digit == 26:
            output += "a"
        elif digit == 27:
            output += "b"
        elif digit == 28:
            output += "c"
        elif digit == 29:
            output += "d"
        elif digit == 30:
            output += "e"
        elif digit == 31:
            output += "f"
        elif digit == 32:
            output += "g"
        elif digit == 33:
            output += "h"
        elif digit == 34:
            output += "i"
        elif digit == 35:
            output += "j"
        elif digit == 36:
            output += "k"
        elif digit == 37:
            output += "l"
        elif digit == 38:
            output += "m"
        elif digit == 39:
            output += "n"
        elif digit == 40:
            output += "o"
        elif digit == 41:
            output += "p"
        elif digit == 42:
            output += "q"
        elif digit == 43:
            output += "r"
        elif digit == 44:
            output += "s"
        elif digit == 45:
            output += "t"
        elif digit == 46:
            output += "u"
        elif digit == 47:
            output += "v"
        elif digit == 48:
            output += "w"
        elif digit == 49:
            output += "x"
        elif digit == 50:
            output += "y"
        elif digit == 51:
            output += "z"
        elif digit == 52:
            output += "0"
        elif digit == 53:
            output += "1"
        elif digit == 54:
            output += "2"
        elif digit == 55:
            output += "3"
        elif digit == 56:
            output += "4"
        elif digit == 57:
            output += "5"
        elif digit == 58:
            output += "6"
        elif digit == 59:
            output += "7"
        elif digit == 60:
            output += "8"
        elif digit == 61:
            output += "9"
        elif digit == 62:
            output += "+"
        elif digit == 63:
            output += "/"
    print(output)
