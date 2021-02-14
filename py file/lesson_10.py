def printing(a) :
     with open("chislo.txt", "a") as f :
            write_data = a
            f.write(str(write_data) + " /n" )
from random import randint
with open("chislo.txt", "w+") as f :
    write_data = ""
    f.write(write_data)
rand = randint(1, 100)
inp = 0
while inp != rand :
    inp = int(input("Угадай число от 1 до 100 " ))
    printing(inp)
    if inp < rand :
        print(f"Это число больше чем {inp}")
        printing(f"Это число больше чем {inp}")
    elif inp > rand :
        print(f"Это число меньше чем {inp}")
        printing(f"Это число меньше чем {inp}")
    else :
        print(f"Ура! Победа!")
        printing(f"Ура! Победа!")


