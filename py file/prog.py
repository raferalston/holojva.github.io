for p in range(100) :
    small = list("qwertyuiopasdfghjklzxcvbnmñйцукенгшщзхъфывапролджэёячсмитьбю")
    s_num = 0
    big = list("QWERTYUIOPASDFGHJKLZXCVBNMÑЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТЬБЮ")
    b_num = 0
    znaki = list('''§±<>?/.,;:'"[]{}\|+=-_!@#№$%^&*()''')
    z_num = 0
    probel = " "
    p_num = 0
    nums = list("1234567890")
    n_num = 0

    inp = input("String ")
    for i in list(inp) :
        for j in small :
            if j == i :
                s_num += 1
        for k in big :
            if k == i :
                b_num += 1
        for l in znaki :
            if l == i :
                z_num += 1
        if probel == i :
            p_num += 1
        for m in nums :
            if m == i :
                n_num += 1    
    print(f"Эта строка состоит из {s_num} маленьких букв, {b_num} больших букв, {z_num} знаков, {p_num} пробелов, {n_num} цифр.")