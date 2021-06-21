def binary():
    a_list = []
    a = input("number: ")
    aint = int(a)
    while aint != 0:
        add = aint % 2
        a_list.append(add)
        aint //= 2
    list.reverse(a_list)
    output = ""
    for digit in a_list:
        digitstr = str(digit)
        output += digitstr
    print(output)
