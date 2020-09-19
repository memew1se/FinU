import random

pr1 =('''Какую партию хотите сыграть?
1. Обычную 
2. Настраиваемую''')

pr2 = ('''Второй игрок?
1. Бот
2. Человек''')

pr3 = ('''За какую сторону хотите сыграть?
1. Белые
2. Черные''')

pr4 = ('''Показать запись ходов?
1. Да
2. Нет''')

def interptretator(command):
    if command.lower() == 'b1':
        return 0
    elif command.lower() == 'd1':
        return 1
    elif command.lower() == 'f1':
        return 2
    elif command.lower() == 'h1':
        return 3
    elif command.lower() == 'a2':
        return 4
    elif command.lower() == 'c2':
        return 5
    elif command.lower() == 'e2':
        return 6
    elif command.lower() == 'g2':
        return 7
    elif command.lower() == 'b3':
        return 8
    elif command.lower() == 'd3':
        return 9
    elif command.lower() == 'f3':
        return 10
    elif command.lower() == 'h3':
        return 11
    elif command.lower() == 'a4':
        return 12
    elif command.lower() == 'c4':
        return 13
    elif command.lower() == 'e4':
        return 14
    elif command.lower() == 'g4':
        return 15
    elif command.lower() == 'b5':
        return 16
    elif command.lower() == 'd5':
        return 17
    elif command.lower() == 'f5':
        return 18
    elif command.lower() == 'h5':
        return 19
    elif command.lower() == 'a6':
        return 20
    elif command.lower() == 'c6':
        return 21
    elif command.lower() == 'e6':
        return 22
    elif command.lower() == 'g6':
        return 23
    elif command.lower() == 'b7':
        return 24
    elif command.lower() == 'd7':
        return 25
    elif command.lower() == 'f7':
        return 26
    elif command.lower() == 'h7':
        return 27
    elif command.lower() == 'a8':
        return 28
    elif command.lower() == 'c8':
        return 29
    elif command.lower() == 'e8':
        return 30
    elif command.lower() == 'g8':
        return 31
    else:
        return 42
    
def reverse_interpretator(command):
    if command == 0:
        return 'b1'
    elif command == 1:
        return 'd1'
    elif command == 2:
        return 'f1'
    elif command == 3:
        return 'h1'
    elif command == 4:
        return 'a2'
    elif command == 5:
        return 'c2'
    elif command == 6:
        return 'e2'
    elif command == 7:
        return 'g2'
    elif command == 8:
        return 'b3'
    elif command == 9:
        return 'd3'
    elif command == 10:
        return 'f3'
    elif command == 11:
        return 'h3'
    elif command == 12:
        return 'a4'
    elif command == 13:
        return 'c4'
    elif command == 14:
        return 'e4'
    elif command == 15:
        return 'g4'
    elif command == 16:
        return 'b5'
    elif command == 17:
        return 'd5'
    elif command == 18:
        return 'f5'
    elif command == 19:
        return 'h5'
    elif command == 20:
        return 'a6'
    elif command == 21:
        return 'c6'
    elif command == 22:
        return 'e6'
    elif command == 23:
        return 'g6'
    elif command == 24:
        return 'b7'
    elif command == 25:
        return 'd7'
    elif command == 26:
        return 'f7'
    elif command == 27:
        return 'h7'
    elif command == 28:
        return 'a8'
    elif command == 29:
        return 'c8'
    elif command == 30:
        return 'e8'
    elif command == 31:
        return 'g8'

        
class Cell():
    def __init__(self, state, index):
        self.state = state
        self.index = index


class Field():
    def __init__(self, state = 1, logs = []):
        if state == 1:
            self.logs = logs
            c = Cell
            self.field = [c(2,  0), c(2,  1), c(2,  2), c(2,  3), 
                          c(2,  4), c(2,  5), c(2,  6), c(2,  7),
                          c(2,  8), c(2,  9), c(2, 10), c(2, 11), 
                          c(0, 12), c(0, 13), c(0, 14), c(0, 15), 
                          c(0, 16), c(0, 17), c(0, 18), c(0, 19), 
                          c(1, 20), c(1, 21), c(1, 22), c(1, 23), 
                          c(1, 24), c(1, 25), c(1, 26), c(1, 27), 
                          c(1, 28), c(1, 29), c(1, 30), c(1, 31)]
            
        elif state == 2:
            self.logs = logs
            c = Cell
            self.field = [c(0,  0), c(0,  1), c(0,  2), c(0,  3), 
                          c(0,  4), c(0,  5), c(0,  6), c(0,  7),
                          c(0,  8), c(0,  9), c(0, 10), c(0, 11), 
                          c(0, 12), c(0, 13), c(0, 14), c(0, 15), 
                          c(0, 16), c(0, 17), c(0, 18), c(0, 19), 
                          c(0, 20), c(0, 21), c(0, 22), c(0, 23), 
                          c(0, 24), c(0, 25), c(0, 26), c(0, 27), 
                          c(0, 28), c(0, 29), c(0, 30), c(0, 31)]
            
            
            position_for_white = 42
            while position_for_white != '':
                self.draw()
                position_for_white = input('Куда поставить белую шашку? ')
                if position_for_white == '':
                    print(chr(27) + "[2J")
                    continue
                if interptretator(position_for_white) == 42:
                    print(chr(27) + "[2J")
                    continue
                    
                self.field[interptretator(position_for_white)].state = 1
                print(chr(27) + "[2J")
                
            position_for_black = 42
            while position_for_black!= '':
                self.draw()
                position_for_black = input('Куда поставить черную шашку?  ')
                if position_for_black == '':
                    print(chr(27) + "[2J")
                    continue
                if interptretator(position_for_black) == 42:
                    print(chr(27) + "[2J")
                    continue
                    
                self.field[interptretator(position_for_black)].state = 2
                print(chr(27) + "[2J")
                          
    def diagonals(self):
        self.a4d1 = [self.field[12], self.field[8], self.field[5], self.field[1]]
        self.a6f1 = [self.field[20], self.field[16], self.field[13], self.field[9], self.field[6], self.field[2]]
        self.a8h1 = [self.field[28], self.field[24], self.field[21], self.field[17], self.field[14], self.field[10], self.field[7], self.field[3]]
        self.d8h3 = [self.field[29], self.field[25], self.field[22], self.field[18], self.field[15], self.field[11]]
        self.e8h5 = [self.field[30], self.field[26], self.field[23], self.field[19]]
        
        self.c8a6 = [self.field[29], self.field[24], self.field[20]]
        self.e8a4 = [self.field[30], self.field[25], self.field[21], self.field[16], self.field[12]]
        self.g8a2 = [self.field[31], self.field[26], self.field[22], self.field[17], self.field[13], self.field[8], self.field[4]]
        self.h7b1 = [self.field[27], self.field[23], self.field[18], self.field[14], self.field[9], self.field[5], self.field[0]]
        self.h5d1 = [self.field[19], self.field[15], self.field[10], self.field[6], self.field[1]]
        self.h3f1 = [self.field[11], self.field[7], self.field[2]]
        
        self.cheeki_breeki_v_damki_for_black = [self.field[28], self.field[29], self.field[30], self.field[31]]
        self.cheeki_breeki_v_damki_for_white = [self.field[0], self.field[1], self.field[2], self.field[3]]
        
        self.all_diagonals = [self.a4d1, self.a6f1, self.a8h1, self.d8h3, self.e8h5, 
                              self.c8a6, self.e8a4, self.g8a2, self.h7b1, self.h5d1, self.h3f1]
        
    def conditions_to_win(self, team):
        self.diagonals()
        
        condition1 = False
        condition2 = False
        condition3 = False
        
        for cell in self.cheeki_breeki_v_damki_for_white:
            if cell.state == 1:
                condition1 = True
                
        for cell in self.cheeki_breeki_v_damki_for_black:
            if cell.state == 2:
                condition1 = True
                    
                
        white_counter = 0
        black_counter = 0                
        for cell in self.field:
            if cell.state == 2:
                black_counter += 1
            elif cell.state == 1:
                white_counter += 1
                
        if team == True:
            team = 1
        else:
            team = 2
        
        if (white_counter == 0) or (black_counter) == 0:
            condition2 = True
            
        if self.shoud_u_eat(team)[0] == False:
            if self.can_u_do_it(0, 0, 0, 1, team) == []:
                condition3 = True
                
        return (condition1 or condition2 or condition3)
    
    def can_u_theoretically_do_it(self, frm, to):
        possible_turns = dict()
        possible_turns[0] = [4, 5, 9]
        possible_turns[1] = [5, 6, 8, 10]
        possible_turns[2] = [6, 9, 7, 11]
        possible_turns[3] = [7, 10]
        possible_turns[4] = [0, 8, 13]
        possible_turns[5] = [0, 1, 8, 12, 9, 14]
        possible_turns[6] = [1, 2, 9, 10, 13, 15]
        possible_turns[7] = [2, 3, 10, 11, 14]
        possible_turns[8] = [4, 5, 12, 13, 17]
        possible_turns[9] = [5, 6, 13, 14, 0, 2, 16, 18]
        possible_turns[10] = [1, 6, 3, 7, 15, 19, 17, 14]
        possible_turns[11] = [2, 7, 15, 18]
        possible_turns[12] = [8, 5, 16, 21]
        possible_turns[13] = [4, 8, 16, 20, 17, 22, 9, 6]
        possible_turns[14] = [5, 9, 10, 7, 17, 21, 18, 23]
        possible_turns[15] = [11, 19, 18, 10, 6, 22]
        possible_turns[16] = [12, 20, 13, 9, 21, 25]
        possible_turns[17] = [21, 24, 22, 26, 14, 10, 8, 13]
        possible_turns[18] = [22, 25, 23, 27, 14, 9, 15, 11]
        possible_turns[19] = [23, 26, 15, 10]
        possible_turns[20] = [24, 29, 16, 13]
        possible_turns[21] = [24, 28, 25, 30, 16, 12, 17, 14]
        possible_turns[22] = [26, 31, 25, 29, 18, 15, 17, 13]
        possible_turns[23] = [27, 19, 26, 30, 18, 14]
        possible_turns[24] = [28, 29, 20, 21, 17]
        possible_turns[25] = [29, 30, 21, 22, 16, 18]
        possible_turns[26] = [30, 31, 22, 23, 17, 19]
        possible_turns[27] = [31, 23, 18]
        possible_turns[28] = [24, 21]
        possible_turns[29] = [24, 20, 25, 22]
        possible_turns[30] = [26, 23, 25, 21]
        possible_turns[31] = [27, 26, 22]
        
        if interptretator(to) in possible_turns[interptretator(frm)]:
            return True
        else:
            return False
        
    def can_u_do_it(self, team, frm, to, for_bot = 0, bot_team = None):
        possible_turns_for_black = dict()
        possible_turns_for_white = dict()
        
        possible_turns_for_black[0] = [4, 5]
        
        possible_turns_for_black[1] = [5, 6]
        
        possible_turns_for_black[2] = [6, 7]
        
        possible_turns_for_black[3] = [7]
        
        possible_turns_for_black[4] = [8]
        possible_turns_for_white[4] = [0]
        
        possible_turns_for_black[5] = [8, 9]
        possible_turns_for_white[5] = [0, 1]
        
        possible_turns_for_black[6] = [9, 10]
        possible_turns_for_white[6] = [1, 2]
        
        possible_turns_for_black[7] = [10, 11]
        possible_turns_for_white[7] = [2, 3]
        
        possible_turns_for_black[8] = [12, 13]
        possible_turns_for_white[8] = [4, 5]
        
        possible_turns_for_black[9] = [13, 14]
        possible_turns_for_white[9] = [5, 6]
        
        possible_turns_for_black[10] = [14, 15]
        possible_turns_for_white[10] = [6, 7]
        
        possible_turns_for_black[11] = [15]
        possible_turns_for_white[11] = [7]
        
        possible_turns_for_black[12] = [16]
        possible_turns_for_white[12] = [8]
        
        possible_turns_for_black[13] = [16, 17]
        possible_turns_for_white[13] = [8, 9]
        
        possible_turns_for_black[14] = [17, 18]
        possible_turns_for_white[14] = [9, 10]
        
        possible_turns_for_black[15] = [18, 19]
        possible_turns_for_white[15] = [10, 11]
        
        possible_turns_for_black[16] = [20, 21]
        possible_turns_for_white[16] = [12, 13]
        
        possible_turns_for_black[17] = [21, 22]
        possible_turns_for_white[17] = [13, 14]
        
        possible_turns_for_black[18] = [22, 23]
        possible_turns_for_white[18] = [14, 15]
        
        possible_turns_for_black[19] = [23]
        possible_turns_for_white[19] = [15]
        
        possible_turns_for_black[20] = [24]
        possible_turns_for_white[20] = [16]
        
        possible_turns_for_black[21] = [24, 25]
        possible_turns_for_white[21] = [16, 17]
        
        possible_turns_for_black[22] = [25, 26]
        possible_turns_for_white[22] = [17, 18]
        
        possible_turns_for_black[23] = [26, 27]
        possible_turns_for_white[23] = [18, 19]
        
        possible_turns_for_black[24] = [28, 29]
        possible_turns_for_white[24] = [20, 21]
        
        possible_turns_for_black[25] = [29, 30]
        possible_turns_for_white[25] = [21, 22]
        
        possible_turns_for_black[26] = [30, 31]
        possible_turns_for_white[26] = [22, 23]
        
        possible_turns_for_black[27] = [31]
        possible_turns_for_white[27] = [23]
        
        possible_turns_for_white[28] = [24]
        
        possible_turns_for_white[29] = [24, 25]
        
        possible_turns_for_white[30] = [25, 26]
        
        possible_turns_for_white[31] = [26, 27]
        
        
        if for_bot == 0:
            statement = False
            
            if team == 1:
                
                if interptretator(to) in possible_turns_for_white[interptretator(frm)] and (self.field[interptretator(to)].state == 0) and (self.field[interptretator(frm)].state == 1):
                    statement = True
                    
            elif team == 2:
                
                if interptretator(to) in possible_turns_for_black[interptretator(frm)] and (self.field[interptretator(to)].state == 0) and (self.field[interptretator(frm)].state == 2):
                    statement = True
                
            return statement
        
        else:
            positions = []
            if bot_team == 1:
                
                for i in range(0, 28):
                    if self.field[i].state == bot_team:
                        for j in possible_turns_for_white[i]:
                            if self.field[j].state == 0:
                                positions.append([i, j])                   
                        
            else:
                
                for i in range(4, 32):
                    if self.field[i].state == bot_team:
                        for j in possible_turns_for_black[i]:
                            if self.field[j].state == 0:
                                positions.append([i, j])
            
            return positions
               
    def shoud_u_eat(self, team):
        positions = []
        statement = False
        self.diagonals()
        
        for diagonal in self.all_diagonals:
            for cell_index in range(len(diagonal)):
                
                if cell_index == 0:
                    if (diagonal[0].state == team) and (diagonal[1].state != team) and (diagonal[1].state != 0) and (diagonal[2].state == 0):
                        if [diagonal[0].index, diagonal[1].index, diagonal[2].index] not in positions:
                            positions.append([diagonal[0].index, diagonal[1].index, diagonal[2].index])
                            statement = True
                            
                elif cell_index == len(diagonal) - 1:
                    if (diagonal[len(diagonal) - 1].state == team) and (diagonal[len(diagonal) - 2].state != team) and (diagonal[len(diagonal) - 2].state != 0) and (diagonal[len(diagonal) - 3].state == 0):
                        if [diagonal[len(diagonal) - 1].index, diagonal[len(diagonal) - 2].index, diagonal[len(diagonal) - 3].index] not in positions:
                            positions.append([diagonal[len(diagonal) - 1].index, diagonal[len(diagonal) - 2].index, diagonal[len(diagonal) - 3].index])
                            statement = True
                        

                elif (cell_index == 1) and (len(diagonal) != 3):
                    if (diagonal[1].state == team) and (diagonal[2].state != team) and (diagonal[2].state != 0) and (diagonal[3].state == 0):
                        if [diagonal[1].index, diagonal[2].index, diagonal[3].index] not in positions:
                            positions.append([diagonal[1].index, diagonal[2].index, diagonal[3].index])
                            statement = True
                
                elif (cell_index == len(diagonal) - 2) and (len(diagonal) != 3):
                    if (diagonal[len(diagonal) - 2].state == team) and (diagonal[len(diagonal) - 3].state != team) and (diagonal[len(diagonal) - 3].state != 0) and (diagonal[len(diagonal) - 4].state == 0):
                        if [diagonal[len(diagonal) - 2].index, diagonal[len(diagonal) - 3].index, diagonal[len(diagonal) - 4].index] not in positions:
                            positions.append([diagonal[len(diagonal) - 2].index, diagonal[len(diagonal) - 3].index, diagonal[len(diagonal) - 4].index])
                            statement = True
                
                elif len(diagonal) != 3:
                    if (diagonal[cell_index].state == team) and (diagonal[cell_index + 1].state != team) and (diagonal[cell_index + 1].state != 0) and (diagonal[cell_index + 2].state == 0):
                        if [diagonal[cell_index].index, diagonal[cell_index + 1].index, diagonal[cell_index + 2].index] not in positions:
                            positions.append([diagonal[cell_index].index, diagonal[cell_index + 1].index, diagonal[cell_index + 2].index])
                            statement = True
                            
                    if (diagonal[cell_index].state == team) and (diagonal[cell_index - 1].state != team) and (diagonal[cell_index - 1].state != 0) and (diagonal[cell_index - 2].state == 0):
                        if [diagonal[cell_index].index, diagonal[cell_index - 1].index, diagonal[cell_index - 2].index] not in positions:
                            positions.append([diagonal[cell_index].index, diagonal[cell_index - 1].index, diagonal[cell_index - 2].index])             
                            statement = True
            
        return [statement, positions]
    
    def draw(self):
        
        characters = []
        for cell in self.field:
            if cell.state == 0:
                characters.append('x')
            elif cell.state == 1:
                characters.append('Б')
            elif cell.state == 2:
                characters.append('Ч')
        
        how_it_looks = '''   A  |  B  |  C  |  D  |  E  |  F  |  G  |  H  
|-----------------------------------------------|
|     |  {}  |     |  {}  |     |  {}  |     |  {}  | 1
|-----+-----+-----+-----+-----+-----+-----+-----|
|  {}  |     |  {}  |     |  {}  |     |  {}  |     | 2
|-----+-----+-----+-----+-----+-----+-----+-----|
|     |  {}  |     |  {}  |     |  {}  |     |  {}  | 3
|-----+-----+-----+-----+-----+-----+-----+-----|
|  {}  |     |  {}  |     |  {}  |     |  {}  |     | 4
|-----+-----+-----+-----+-----+-----+-----+-----|
|     |  {}  |     |  {}  |     |  {}  |     |  {}  | 5 
|-----+-----+-----+-----+-----+-----+-----+-----|
|  {}  |     |  {}  |     |  {}  |     |  {}  |     | 6 
|-----+-----+-----+-----+-----+-----+-----+-----|
|     |  {}  |     |  {}  |     |  {}  |     |  {}  | 7 
|-----+-----+-----+-----+-----+-----+-----+-----|
|  {}  |     |  {}  |     |  {}  |     |  {}  |     | 8
|-----------------------------------------------|'''.format(*characters)    
        print(how_it_looks)         
            
    def log(self):
        
        if len(self.logs) % 2 == 1:
            self.logs.append('X')
        else:
            self.logs[len(self.logs) - 1] = self.logs[len(self.logs) - 1] + 'X' 
        
        j = 1
        for i in range(0, len(self.logs), 2):
            print(f'{j}: {self.logs[i]} {self.logs[i+1]}')
            j += 1
                
    def bot(self, team):
        if team == True:
            team = 1
        else:
            team = 2
            
        check = self.shoud_u_eat(team)
        if check[0] == False:
            pos_list = self.can_u_do_it(0, 0, 0, 1, team)
            
            choice_list = pos_list[random.randint(0, len(pos_list) - 1)]
            self.field[choice_list[0]].state = 0
            self.field[choice_list[1]].state = team
            
            self.logs.append(f'{reverse_interpretator(choice_list[0])}-{reverse_interpretator(choice_list[1])}')
            self.draw()
            lol = input(f'Бот сделал свой ход.. ({reverse_interpretator(choice_list[0])}-{reverse_interpretator(choice_list[1])}) ')
            
        else:
            pos_list = check[1]
            choice_list = pos_list[random.randint(0, len(pos_list) - 1)]
            self.field[choice_list[0]].state = 0
            self.field[choice_list[1]].state = 0
            self.field[choice_list[2]].state = team
            
            self.logs.append(f'{reverse_interpretator(choice_list[0])}:{reverse_interpretator(choice_list[2])}')
            self.draw()
            lol = input(f'Бот сделал свой ход.. ({reverse_interpretator(choice_list[0])}:{reverse_interpretator(choice_list[2])}) ')
                  
    
class Game():
    def __init__(self):
        print(pr1)
        self.state = int(input())
        if self.state not in [1, 2]:
            print('Введены неправильные данные!')
            self.__init__()
                
    def start(self):
        if self.state == 1:
            f = Field()
            print(pr2)
            second_player = int(input()) 
            if second_player == 1:
                print(pr3)
                player_turn = int(input())
                self.gameplay_with_bot(f, player_turn)
                
            elif second_player == 2:
                self.gameplay_with_player(f)
            
                
        elif self.state == 2:
            print(chr(27) + "[2J")
            f = Field(2)
            print(pr2)
            second_player = int(input()) 
            if second_player == 1:
                print(pr3)
                player_turn = int(input())
                self.gameplay_with_bot(f, player_turn)
                
            elif second_player == 2:
                self.gameplay_with_player(f)
                           
    def gameplay_with_bot(self, field, player_turn):
        flag = True
        print(chr(27) + "[2J")
        field.draw()
        while field.conditions_to_win(flag) == False:
                        
            if player_turn == 1 and flag == True:
                turn = input('Ход белых: ')
                
                if '->' not in turn:
                    print('Введены неправильные данные! Попробуте снова\n')
                    continue
                turn = turn.split('->')
                
                if (interptretator(turn[0]) and interptretator(turn[1]) != 42) and (turn[0] != turn [1]):
                    
                    if field.can_u_theoretically_do_it(turn[0], turn[1]) == True:
                        check = field.shoud_u_eat(player_turn)
                        check_list = check[1]
                        
                        if check[0] == False:
                            if field.can_u_do_it(player_turn, turn[0], turn[1]) == True:
                                
                                field.field[interptretator(turn[0])].state = 0 
                                field.field[interptretator(turn[1])].state = player_turn
                                field.logs.append(f'{turn[0].upper()}-{turn[1].upper()}')
                                print(chr(27) + "[2J")
                                field.draw()
                                flag = not flag
                                
                            else:
                                print('Вы не можете так походить! Попробуте снова 1\n')
                                continue
                                
                        else:
                            statement = False
                            for pos_list in check_list:
                                if (interptretator(turn[0]) and interptretator(turn[1]) in pos_list) and (interptretator(turn[0]) == pos_list[0]) and (interptretator(turn[1]) == pos_list[2]):
                                    eaten = pos_list[1]
                                    statement = True
                                    
                            if statement == True:
                                field.field[interptretator(turn[0])].state = 0 
                                field.field[eaten].state = 0 
                                field.field[interptretator(turn[1])].state = player_turn
                                field.logs.append(f'{turn[0].upper()}:{turn[1].upper()}')
                                print(chr(27) + "[2J")
                                field.draw()
                                flag = not flag
                                
                            else:
                                print('Вы не можете так походить! Попробуте снова 2\n')
                                continue
                        
                    else:
                        print('Вы не можете так походить! Поробуйте снова 3\n')
                        continue
                
                else:
                    print('Введены неправильные данные! Попробуте снова 4\n')
                    continue 
            
            elif player_turn == 2 and flag == False:
                turn = input('Ход черных: ')
                
                if '->' not in turn:
                    print('Введены неправильные данные! Попробуте снова\n')
                    continue
                turn = turn.split('->')
                
                if (interptretator(turn[0]) and interptretator(turn[1]) != 42) and (turn[0] != turn [1]):
                    
                    if field.can_u_theoretically_do_it(turn[0], turn[1]) == True:
                        check = field.shoud_u_eat(player_turn)
                        check_list = check[1]
                        
                        if check[0] == False:
                            if field.can_u_do_it(player_turn, turn[0], turn[1]) == True:
                                
                                field.field[interptretator(turn[0])].state = 0 
                                field.field[interptretator(turn[1])].state = player_turn
                                field.logs.append(f'{turn[0].upper()}-{turn[1].upper()}')
                                print(chr(27) + "[2J")
                                field.draw()
                                flag = not flag
                                
                            else:
                                print('Вы не можете так походить! Попробуте снова 1\n')
                                continue
                                
                        else:
                            statement = False
                            for pos_list in check_list:
                                if (interptretator(turn[0]) and interptretator(turn[1]) in pos_list) and (interptretator(turn[0]) == pos_list[0]) and (interptretator(turn[1]) == pos_list[2]):
                                    eaten = pos_list[1]
                                    statement = True
                                    
                            if statement == True:
                                field.field[interptretator(turn[0])].state = 0 
                                field.field[eaten].state = 0 
                                field.field[interptretator(turn[1])].state = player_turn
                                field.logs.append(f'{turn[0].upper()}:{turn[1].upper()}')
                                print(chr(27) + "[2J")
                                field.draw()
                                flag = not flag
                                
                            else:
                                print('Вы не можете так походить! Попробуте снова 2\n')
                                continue
                                    
                    else:
                        print('Вы не можете так походить! Поробуйте снова 3\n')
                        continue
                
                else:
                    print('Введены неправильные данные! Попробуте снова 4\n')
                    continue
                
            else:
                print(chr(27) + "[2J")
                field.bot(flag)
                print(chr(27) + "[2J")
                field.draw()
                flag = not flag
                
        if flag == True:
            print('Черные победили!')
        else:
            print('Белые победили!')                         
            
        print(pr4)
        decision = int(input())
        if decision == 1:
            field.log()
        elif decision == 2:
            print('Спасибо за игру!')
                    
    def gameplay_with_player(self, field):
        flag = True
        print(chr(27) + "[2J")
        field.draw()
        while field.conditions_to_win(flag) == False:
                        
            if flag == True:
                player_turn = 1
                turn = input('Ход белых: ')
                
                if '->' not in turn:
                    print('Введены неправильные данные! Попробуте снова\n')
                    continue
                turn = turn.split('->')
                
                if (interptretator(turn[0]) and interptretator(turn[1]) != 42) and (turn[0] != turn [1]):
                    
                    if field.can_u_theoretically_do_it(turn[0], turn[1]) == True:
                        check = field.shoud_u_eat(player_turn)
                        check_list = check[1]
                        
                        if check[0] == False:
                            if field.can_u_do_it(player_turn, turn[0], turn[1]) == True:
                                
                                field.field[interptretator(turn[0])].state = 0 
                                field.field[interptretator(turn[1])].state = player_turn
                                field.logs.append(f'{turn[0].upper()}-{turn[1].upper()}')
                                print(chr(27) + "[2J")
                                field.draw()
                                flag = not flag
                                
                            else:
                                print('Вы не можете так походить! Попробуте снова 1\n')
                                continue
                                
                        else:
                            statement = False
                            for pos_list in check_list:
                                if (interptretator(turn[0]) and interptretator(turn[1]) in pos_list) and (interptretator(turn[0]) == pos_list[0]) and (interptretator(turn[1]) == pos_list[2]):
                                    eaten = pos_list[1]
                                    statement = True
                                    
                            if statement == True:
                                field.field[interptretator(turn[0])].state = 0 
                                field.field[eaten].state = 0 
                                field.field[interptretator(turn[1])].state = player_turn
                                field.logs.append(f'{turn[0].upper()}:{turn[1].upper()}')
                                print(chr(27) + "[2J")
                                field.draw()
                                flag = not flag
                                
                            else:
                                print('Вы не можете так походить! Попробуте снова 2\n')
                                continue
                        
                    else:
                        print('Вы не можете так походить! Поробуйте снова 3\n')
                        continue
                
                else:
                    print('Введены неправильные данные! Попробуте снова 4\n')
                    continue 
            
            else:
                player_turn = 2
                turn = input('Ход черных: ')
                
                if '->' not in turn:
                    print('Введены неправильные данные! Попробуте снова\n')
                    continue
                turn = turn.split('->')
                
                if (interptretator(turn[0]) and interptretator(turn[1]) != 42) and (turn[0] != turn [1]):
                    
                    if field.can_u_theoretically_do_it(turn[0], turn[1]) == True:
                        check = field.shoud_u_eat(player_turn)
                        check_list = check[1]
                        
                        if check[0] == False:
                            if field.can_u_do_it(player_turn, turn[0], turn[1]) == True:
                                
                                field.field[interptretator(turn[0])].state = 0 
                                field.field[interptretator(turn[1])].state = player_turn
                                field.logs.append(f'{turn[0].upper()}-{turn[1].upper()}')
                                print(chr(27) + "[2J")
                                field.draw()
                                flag = not flag
                                
                            else:
                                print('Вы не можете так походить! Попробуте снова 1\n')
                                continue
                                
                        else:
                            statement = False
                            for pos_list in check_list:
                                if (interptretator(turn[0]) and interptretator(turn[1]) in pos_list) and (interptretator(turn[0]) == pos_list[0]) and (interptretator(turn[1]) == pos_list[2]):
                                    eaten = pos_list[1]
                                    statement = True
                                    
                            if statement == True:
                                field.field[interptretator(turn[0])].state = 0 
                                field.field[eaten].state = 0 
                                field.field[interptretator(turn[1])].state = player_turn
                                field.logs.append(f'{turn[0].upper()}:{turn[1].upper()}')
                                print(chr(27) + "[2J")
                                field.draw()
                                flag = not flag
                                
                            else:
                                print('Вы не можете так походить! Попробуте снова 2\n')
                                continue
                                    
                    else:
                        print('Вы не можете так походить! Поробуйте снова 3\n')
                        continue
                
                else:
                    print('Введены неправильные данные! Попробуте снова 4\n')
                    continue
        

        if flag == True:
            print('Черные победили!')
        else:
            print('Белые победили!')
        
        print(pr4)
        decision = int(input())
        if decision == 1:
            field.log()
        elif decision == 2:
            print('Спасибо за игру!')    
        
    
if __name__ == '__main__':
    game = Game()
    game.start()