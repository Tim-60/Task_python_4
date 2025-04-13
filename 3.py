def file(text: str, name: str):
    with open("C:\\Users\\tim\\Desktop\\" + name, "a", encoding="ANSI") as file:
        file.write('\n' + text)
        file.close()
    with open("C:\\Users\\tim\\Desktop\\" + name, "r", encoding="ANSI") as file:
        lines = file.readlines()
        even_lines = list(enumerate(lines, start = 0))
        for i in range(0, len(even_lines), 2):
            print(even_lines[i][1].rstrip('\n'))
        file.close()

file_name = input('Введите имя файла, который будет открыт: ')
file_text = input('Введите текст, который будет дописан в файл: ')
file(file_text, file_name + '.txt')

