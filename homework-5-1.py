num = int(input("Num: "))
listik = []
for i in range(num): 
    if num % (i + 1) == 0 :
        listik.append(i + 1)
print(listik)        
