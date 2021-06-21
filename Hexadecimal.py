import os
def hexadecimal(a):
    a_list = []
    aint = int(a)
    while aint != 0:
        add = aint % 16
        a_list.append(add)
        aint //= 16
    list.reverse(a_list)
    output = ""
    for digit in a_list:
        if digit <= 9:
            output += str(digit)
        elif digit == 10:
            output += "A"
        elif digit == 11:
            output += "B"
        elif digit == 12:
            output += "C"
        elif digit == 13:
            output += "D"
        elif digit == 14:
            output += "E"
        elif digit == 15:
            output += "F"
    return output
i = open("input.txt", "r")
os.remove("output.txt")
f = open("output.txt", "a")
for line in i:
    f.write(hexadecimal(line))
    f.write(" ")
f.close()
i.close()