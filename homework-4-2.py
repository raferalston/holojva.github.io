print("Пицца стоит 500 рублей")
people = int(input("Сколько человек? "))
money = int(input("Сколько денег? "))
pizza = int(money / 500)
piz_for_person = pizza / people
if pizza < 1:
    print("Денег на пиццу не хватит")
elif piz_for_person < 0.2 :
    print("Маловато пиццы!")
elif piz_for_person < 0.6 :
    print("Средне так пиццы!")
elif piz_for_person < 1 :
    print("Много пиццы!")
elif piz_for_person > 0.999999 :
    print("Отдай мне всю пиццу, я доем!")