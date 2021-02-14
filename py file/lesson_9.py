stages = int(input("Сколько тут этажей? Если будет четное, то я округлю его до нечетного! "))
if stages % 2 == 0 :
    stages += 1
for i in range(int(stages / 2 + 0.5)) :
    print(i * "*")
for i in range(int(stages / 2 + 0.5), 0, -1) :
    print(i * "*")
    
