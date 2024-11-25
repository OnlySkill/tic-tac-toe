field = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
flag_move = True # Маркер для определения череды хода


def clean_field(): # Очистка игрового поля
    global field
    global flag_move
    field = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    flag_move = True
    show_field(field)

def check_winner(fields:list): # Проверка на завершенность игры
    for i in fields: # Проверка победы по строкам
        if i[0] == i[1] == i[2] and i[0] != '-':
            print(f'Победили {i[0]}')
            clean_field()
            return
    for i in range(3): # Проверка победы по столбцам
        if fields[0][i] == fields[1][i] == fields[2][i] and fields[0][i] != '-':
            print(f'Победили {fields[0][i]}')
            clean_field()
            return
    if ((fields[0][0] == fields[1][1] == fields[2][2]) or (fields[2][0] == fields[1][1] == fields[0][2])) and fields[1][1] != '-': # Проверка победы по диагоналям
        print(f'Победили {fields[1][1]}')
        clean_field()
        return
    for i in fields: # Проверка на оконченность игры
        if '-' in i:
            return
    print('Ничья.')
    clean_field()
    return

def show_field(fields: list): # Отображение поля в консоль
    print('  0 1 2')
    for i in range(3):
        print(i, *fields[i])
    return

print('Всегда первыми ходят X')
show_field(field)

while True:
    try: # Проверка ввода
        print('Ход X') if flag_move else print('Ход O')
        move = list(map(int, input().split()))
        if not((0 <= move[0] <= 2) and (0 <= move[1] <= 2) and len(move) == 2):
            print('Неверные координаты')
            continue
        if field[move[0]][move[1]] != '-':
            print('Это поле уже занято')
            continue
    except:
        print('Некорректный тип ввода')
        continue
    else:
        field[move[0]][move[1]] = 'x' if flag_move else 'o'
        flag_move = not flag_move
        show_field(field)
        check_winner(field)