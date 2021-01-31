def build_template(t, w, g, l) :
    """
    input: t - template (list), w - word (string) g - guess (string) l - lifes (int)
    output: t - template (list) with replaced characters in template, lifes
    if character in word == guess
        "character"
    elif character in template != "_"
        "character"
    else
        "_"
    """
    i_found_letter = False
    for i in range(len(w)) :
        if list(w)[i] == g :
            t[i] = g
            i_found_letter = True
        elif t[i] != "_" :
            t[i] = t[i]
        else :    
            t[i] = "_"
    if i_found_letter == False :
        l -= 1
        print(f"У вас осталось {l} попыток")
    print(list_to_string_convert(t))
    return [t, l]   
    
def user_input() :
    """
    output: str, build-in input function
    """
    i = input("Введите букву... ")
    return i
def list_to_string_convert(t) :
    """
    input: t - template (list)
    output: s -  list converted to string
    """
    s = ''
    return s.join(t)
def start_template(w) : 
    t = []
    for l in w :
        t.append("_")
    return t
def welcome_speech(t) :
    """
    input: t - template (string)
    output: return None, it's just usedby built-in function print()    
    """
    print(f'''
        Добро пожаловать в виселицу!
        Вы должны отгадать слово из {len(t)} букв,
        иначе вам конец!
        Начинайте: {t}
    ''')
def get_word(w) :
    return w[0]
def game() :
    progress = True

    word = ["iphone"]
    lifes = 3
    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
   
    while progress : 
        user_guess = user_input()
        template_and_lifes = build_template(template, word_in_play, user_guess, lifes)
        template = template_and_lifes[0]
        lifes = template_and_lifes[1]
        if list_to_string_convert(template) == word_in_play :
            print("Вы победили!!!")
            break
        if lifes == 0 :
            print("Вы проиграли!!!")
            break
game()
