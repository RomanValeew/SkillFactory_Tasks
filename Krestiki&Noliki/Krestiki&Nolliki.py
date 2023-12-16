# Изначальное игровое поле
field = [[" ", 0, 1, 2],
         [0, "-", "-", "-"],
         [1, "-", "-", "-"],
         [2, "-", "-", "-"]]
print()  # Пустая строка для красоты

print("!!!Добро пожаловать в игру Крестики-нолики!!! \n")

# Вывод на экран игрового поля
for row in field:
    for element in row:
        print(element, end="  ")
    print()

# Первым ходит игрок с 'x'
player = "x"


# Функция изменения и вывода игрового поля
def game_field(x, y, symbol):
    field[x + 1][y + 1] = symbol
    for row in field:
        for element in row:
            print(element, end="  ")
        print()


# Функция проверки игровой ситуации по строкам, столбцам и диагоналям
def game_check(symbol):
    for i in range(1, 4):
        if all(field[i][j] == symbol for j in range(1, 4)) or all(field[j][i] == symbol for j in range(1, 4)):
            return True

    if field[1][1] == field[2][2] == field[3][3] != "-" or field[1][3] == field[2][2] == field[3][1] != "-":
        return True

    return False

# Проверка на ничью
def draw_check():
    if all(field[i][j] != "-" for i in range(1, 4) for j in range(1, 4)):
        return True


# Основной цикл игры
while True:

    print()  # Пустая строка для красоты
    line = int(input(f"Игрок с '{player}', введите номер строки (0, 1, 2): "))
    col = int(input(f"Игрок с '{player}', введите номер столбца (0, 1, 2): "))

    # Проверка правильности ввода координат
    if line not in range(0, 3) or col not in range(0, 3):
        print(f"Вы ввели недопустимые координаты!")
        continue
    if field[line + 1][col + 1] != "-":
        print(f"Поле с координатами ({line}, {col}) уже занято!")
        continue

    # Вызов соответствующих функций
    game_field(line, col, player)
    res = game_check(player)
    draw = draw_check()

    # Смена игроков, вывод сообщения о выигрыше или ничье
    if draw:
        print("!!!Ничья!!!")
        break
    elif not draw and not res:
        player = "o" if player == "x" else "x"
    else:
        print(f"!!!Игрок с {player} выиграл!!! Поздравляю!:)")
        break
