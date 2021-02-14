x = int(input("Введите число "))
if x % 2 == 1 :
    x += 1
for i in range(int(x / 2)) :
    print((i * "_") + "x" + ((x - 2 - (2 * i)) * "_") + "x" + (i * "_"))
for i in range(int(x / 2 - 1), 0, -1) :
    print((i * "_") + "x" + ((x - 2 - (2 * i)) * "_") + "x" + (i * "_"))
for i in range(int(1)) :
    print((i * "_") + "x" + ((x - 2 - (2 * i)) * "_") + "x" + (i * "_"))