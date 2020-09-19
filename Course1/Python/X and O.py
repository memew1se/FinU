pole = '''     |     |     
     |     |     
_____|_____|_____
     |     |     
     |     |     
_____|_____|_____
     |     |     
     |     |     
     |     |     '''

def paint(p,tu):                    # Визуализация игры
    p = p[:20] + field[0] + p[21:]
    p = p[:26] + field[1] + p[27:]
    p = p[:32] + field[2] + p[33:]
    p = p[:74] + field[3] + p[75:]
    p = p[:80] + field[4] + p[81:]
    p = p[:86] + field[5] + p[87:]
    p = p[:128] + field[6] + p[129:]
    p = p[:134] + field[7] + p[135:]
    p = p[:140] + field[8] + p[141:]
    stat(tu,True,p)
    

def checking(m,t,s,pole_checking):         # Проверка на введенное значение
    if m.isdigit() == True:
        if int(m) - 1 <= 8 and int(m) - 1 >= 0:
            if field[int(m) - 1] == ' ':
                field[int(m) - 1] = s
                paint(pole_checking,t)
        
            else:
                print('Клетка уже занята! Выберите другую')
                game(t,True,pole_checking)
        else:
            print('Введите значение от 1 до 9')
            game(t,True,pole_checking)
    else:
        print('Введите число')
        game(t,True,pole_checking)
        

def stat(turn,check,pole_end):            # Проверка существуюих выигрышных комбинаций
    if field[0] == field[1] == field[2] and field[0] != ' ' or field[3] == field[4] == field[5] and field[3] != ' ' or field[6] == field[7] == field[8] and field[6] != ' ' or field [0] == field[3] == field[6] and field[0] != ' ' or field[1] == field[4] == field[7] and field[1] != ' ' or field[2] == field[5] == field[8] and field[2] != ' ' or field[0] == field[4] == field[8] and field[0] != ' ' or field[2] == field[4] == field[6] and field[2] != ' ':
        print('-----' * 10)
        print(pole_end,'\nИгрок №{} победил!'.format(turn % 2 + 1))
        print('-----' * 10) 
        check = False
    if turn == 8 and check != False:
        print('-----' * 10)
        print(pole_end,'\nНичья!')
        print('-----' * 10) 
        check = False
    if check != False:
        print('-----' * 10) 
        game(turn+1,True,pole_end)
        
        
def game(turn,check,pole_begin):
    if check == True:              # Проверка на состояние игры
        print('-----' * 10) 
        if turn % 2 == 0:          # Проверка хода
            symb ='X'
        else:
            symb ='O'
        print('Куда поставить {} ? '.format(symb))
        print(pole_begin)
        move = input()
        checking(move,turn,symb,pole_begin)
        
            
while True:
    begin = input('Введите start для запуска игры, end для выхода из программы: ')
    if begin == 'start':
        field = []
        for i in range(0,10):
            field.append(' ')         # Создание или пересоздание нового чистого поля
        print('Инструкция: выберите значение от 1 до 9 чтобы поставить на поле X или O')
        game(0,True,pole)             # Инициализация начала игры
    elif begin == 'end':
        print('До свидания!')
        break
    else:
        print('Введена неправильная команда')