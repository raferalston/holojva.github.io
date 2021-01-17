procent = int(input("Процент вклада: "))
years = int(input("Cколько лет ждать: "))
year = 1
money = int(input("Денег во вкладе: "))
for i in range(years) :
   
    money = money + (money / 100 * procent)
    print(f"Год {year}. Денег {money}")
    year = year + 1
