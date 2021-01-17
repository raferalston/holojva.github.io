hero_name = 'Айфон'
princess_name1 = "Зарядку MagSafe"
princess_name = "Зарядка MagSafe"
villian_name = "Cамсунг"
items = ["зарядка", "чехол"]
hero_actions = ["кинуть", "ударил"]
villian_actions = ["взорвался"]

print(f'''Наша история начнется с героя - {hero_name}а
Он жил в далеком-далеком королевстве и однажды встретил принцессу - {princess_name1}.
Но злой Тим Кук не разрешил им быть вместе и приказал {hero_name}у победить злодея - {villian_name}а
Герой отправился на поиски злодея и взял с собой - {items}
Найдя злодея, герой попытался {hero_actions[0]} {items[0]}й в {villian_name}. Но злодей оказался сильнее чем думал {hero_name} и {villian_actions[0]} в ответ!
{hero_name} использовал {items[1]} и успешно {hero_actions[1]} {villian_name}а. Он повержен!!! И герою досталось его оружие''')

items.append ("Rak'zul Sword")
print (f'''Теперь у героя есть {items}
Добравшись обратно до королевства
{princess_name} и {hero_name} стали жить долго и счастливо!
Конец.''')
