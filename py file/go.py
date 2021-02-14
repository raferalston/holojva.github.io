def drawing_field(x, y, hm, person, field) :
    for i in range(hm) :
            if y == i :
                for j in range(hm) :
                    if x == j :
                        print(str(field * j) + person + (hm - x - 1) * field)
            else :
                print(str(field * hm))
def move_person(x, y, to, hm) :
        if to == 0 :  
            if x != 0:
                x -= 1
            else :
                print("Туда нельзя!")
        elif to == 1 :
            if x != hm - 1:
                x += 1
            else :
                print("Туда нельзя!")
        elif to == 2 or to == 4 :
            if y != hm - 1:
                y += 1
            else :
                print("Туда нельзя!")
        elif to == 3 :
            if y != 0:
                y -= 1
            else :
                print("Туда нельзя!")
        return [x, y]
def to_the() :
    
    """
    output: 0 if left, 1 if right, 2 if down, 3 if up, else 4
    """
    to = input("Куда вы хотите пойти? Варианты ответов: налево, направо, вниз, вверх. Если ошибетесь, автоматически пойдете вниз ")
    if to == "налево" : 
        return 0
    elif to == "направо" : 
        return 1
    elif to == "вниз" : 
        return 2
    elif to == "вверх" : 
        return 3
    else :
        return 4
def game() :
    
    x = 0
    y = 0
    hm = int(input("Какого размера будет поле? "))
    person = "me"
    field = "--"
    progress = True
    while progress :
        to = to_the()
       
        i = move_person(x, y, to, hm)
        x = i[0]
        y = i[1]
        drawing_field(x, y, hm, person, field)
game()