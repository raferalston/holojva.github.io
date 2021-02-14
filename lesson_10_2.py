import pickle

game_data = [
    ("Name", "Kostya"),
    ("Class", "Creator of Kostya-OS.ru"),
    ("Items", ["iphone", "macbook"]),
    ("Windows XP", 9000)
]
with open("save.dat", "wb") as sf :
    pickle.dump(game_data, sf)
with open("save.dat", "rb") as lf :
    load_data = pickle.load(lf)

print(load_data)