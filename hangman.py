def create_down_things(a, b) :
    for i in list(b) :
        a += "_"
        i = i
    c = "".join(a) 
    return a

otvet = "виселица"
ne_otvet = []
p_otvet = create_down_things(ne_otvet, otvet)
 
print(f"Это игра про виселицу, тут надо писать буквы, у вас 3 неправильных попытки, слово из {len(otvet)}. " )
popytky = 3
for i in range(len(otvet) + 3) :
    bukva_naidena = False
    bukva = -1
    inp = input("Bukva: ")
    for j in list(otvet):
        bukva += 1
        if inp == j :
            bukva_naidena = True
            p_otvet = list(p_otvet)
            p_otvet[bukva] = inp
            p_otvet = "".join(p_otvet)
            print(p_otvet)
        if otvet == p_otvet: 
            pobeda = True
            print(f"Вы ПОБЕДИЛИ!!!")
            break 
    if bukva_naidena == False:    
        popytky -= 1
        if popytky != 0 :
            print(f"У вас осталось {popytky} попыток " )
        else :
            print("Ты проиграл(((")
    if otvet == p_otvet :
        break 

            
