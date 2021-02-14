with open("lyrics.txt", encoding="utf8") as f:
    lyrics = f.read()
lyrics = lyrics.lower()
lyrics2 = []
banned = [" ", ",", ".", "!", "?"]
words = 0 
lyrics_word = ""
for i in lyrics :
    if w == "\n" :
        if lyrics_word :
            lyrics2.append(lyrics_word)
    elif w not in banned :
        lyrics_word += w
    else :
        if lyrics_word :
            lyrics2.append(lyrics_word)
        lyrics_word = ""