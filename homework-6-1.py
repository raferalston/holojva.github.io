def funk(linux) :

    for i in range(len(linux)) :
        j = []
        j = j + str(list(linux)[-i - 1])
    
        
    return j
linux = input("Linux word ")
print(funk(linux))