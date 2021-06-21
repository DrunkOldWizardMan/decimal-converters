import random
f = open("input.txt", "w")
a = random.randint(1, 20000)
b = random.randint(1, 20000)
c = random.randint(1, 20000)
f.write(str(a)\n str(b)\n str(c))
f.close()