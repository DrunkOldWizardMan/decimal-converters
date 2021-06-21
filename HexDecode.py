a = input("enter hexadecimal input: ")
alist = []
blist = []
finalnumber = 0
for char in a:
    alist.append(char)
print(alist)
list.reverse(alist)
print(alist)
for digit in alist:
    if digit == '0':
        number = 0
    elif digit == '1':
        number = 1
    elif digit == '2':
        number = 2
    elif digit == '3':
        number = 3
    elif digit == '4':
        number = 4
    elif digit == '5':
        number = 5
    elif digit == '6':
        number = 6
    elif digit == '7':
        number = 7
    elif digit == '8':
        number = 8
    elif digit == '9':
        number = 9
    elif digit == 'A':
        number = 10
    elif digit == 'B':
        number = 11
    elif digit == 'C':
        number = 12
    elif digit == 'D':
        number = 13
    elif digit == 'E':
        number = 14
    elif digit == 'F':
        number = 15
    blist.append(number)
print(blist)
timesran = 0
for x in blist:
    power = 16 ** timesran
    finalnumber += x * power
    timesran += 1
    print(finalnumber)
print(finalnumber)