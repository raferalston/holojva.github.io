with open("kostya_os_ru.txt", "w+") as f :
    write_data = "Запускаем Kostya-OS.ru, launch Kostya-OS.ru"
    f.write(write_data)
with open("kostya_os_ru.txt", "r") as f :
    write_data = f.read()
    print(write_data)