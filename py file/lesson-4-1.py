a = input("Введите имя ")
b = len(a)
if b == 0:
    print("Вы ничего не ввели")
elif b > 0 and b < 4:
    print(f'Слишком короткое имя {a}')
elif b > 3 and b < 8:
    print(f"Идеальное имя {a}")
elif b > 7:
    print(f"Слишком длинное имя {a}")

