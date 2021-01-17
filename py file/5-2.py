x = int(input("Введите число "))
y = 1
while y * y != x :
    y = (x / y + y) / 2
print(y)    