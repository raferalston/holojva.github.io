def calc_savings(s, i=2, t=1) :
    """
    This function is calculating deposite.
    s - money in the deposite
    i - procent of the deposite
    t - time of the deposite
    input: money, procent, time
    output: money in the future
    """
    year = 1
    for j in range(t):
        s += s * (i / 100)
        print(f"Год {year}. Денег {s}")
        year += 1
    return s

def inputs() :
    """
    Takes user input.
    output: tuple with variables of money, procent and time.
    """
    money = int(input("Сколько денег положите на вклад??? "))
    procent = int(input("Сколько процентов положите на вклад??? "))
    time = int(input("Сколько времени на вклад??? "))
    tuple1 = (money, procent, time)
    return tuple1 


inp = inputs()

calc_savings(inp[0], inp[1], inp[2])
