def lose_speech() :
    '''
    output: None, it's used just built-in print() function
    '''
    print("Ты проиграл!")
def win_speech() :
    '''
    output: None, it's used just built-in print() function
    '''
    print("Ты выиграл!")
def check_attempt(life) :
    """
    input: life (int)
    output: int, life -= 1
    """
   
    life = life - 1
    return life
def check_mistake(w, g) :
    """
    input: w - word_in_play (string), g - user_input (string)
    output: bool checks if user guess is wrong
        if no such g in w, return False, else True
    """
    flag = False
    for i in list(w) :
        if i == g :
            flag = True
    return flag

def check_win(g) :
    """
    input: g = template (string)
    output: bool, if no "_" in g return false else true
    """
    for i in list(g) :
        if i == "_" :
            return True
    return False
def print_result(g) :
    """
    input: g - template (string)
    output: return None, used at just built-in function print(g)
    """
    print(f"Вот: {g}")
def build_template(t, w, g) :
    """
    input: t - template (list), w - word (string) g - guess (string)
    output: t - template (list) with replaced characters in template
    if character in word == guess
        "character"
    else
        "_"
    """
    for i in range(len(w)) :
        if t[i] == "_" :
            if w[i] == g :
                t[i] = g
            else :    
                t[i] = "_"
    return t  
    
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
def welcome_speech(t, l) :
    """
    input: t - template (string), lifes (integer)
    output: return None, it's just usedby built-in function print()    
    """
    print(f'''
        Добро пожаловать в виселицу!
        Вы должны отгадать слово из {len(t)} букв за {l} жизней,
        иначе вам конец!
        Начинайте: {t}
    ''')
def get_word(w) :
    import random
    return w[random.randint(0, len(w) - 1)]
def game() :
    progress = True

    word = ["iphone", "imac", "ipod", "macintosh", "ipad", "steve", "jobs", "apple"]
    word_in_play = get_word(word)
    lifes = round(len(word_in_play) / 4 * 3)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template), lifes)
   
    while progress : 
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_string_convert(template)
        print_result(guessed)
        progress = check_win(guessed)
        if not check_mistake(word_in_play, user_guess) :
            lifes = check_attempt(lifes)
            print(f"Осталось {lifes} попыток")
        if lifes == 0 :
            lose_speech()
            break
        if not progress :
            win_speech()
game()
