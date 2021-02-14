when = {"Ada Lovelace": "10 december 1815", "Charles Babbidge": "26 december 1791", "Steve Jobs": "24 february 1955"}

def game(inp, when) :
    if inp in when :
        print(when[inp])
    else :
        print("No.")
while True :
    inp = input("Ada Lovelace, Charles Babbidge, Steve Jobs")
    game(inp, when)
    
