def funk(amd) :

    for i in range(len(amd)) :
        j = []
        j = j + str(list(amd)[-i - 1])
    
    if amd == j :
        return "Yes!"
    else :
        return "No!"    

amd = input("Amd word ")
print(funk(amd))