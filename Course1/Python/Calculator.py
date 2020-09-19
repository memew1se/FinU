print('Чтобы прекратить ввод введите exit\nЧтобы получить значение с плавующей точкой введие to double\nЧтобы сохранить результат введите save "Наименование"\nЧтобы удалить результат введите del "Наименование"')
defoult_symbs = {'-','+','/','*',' ',')','(','\\',None} 
saves = {}

def anti_none(iter_list):
    '''Удаление элементов со значениями None'''
    for i in range(len(iter_list)-1,-1,-1):
        if iter_list[i] == None:
            del(iter_list[i])
    return(iter_list)

def calculations(equation):
    '''Математические операции. Возвращает кортеж из числителя и знаменателя'''
    new_equation = []
    bracket_flag = False
    left_bracket_count = 0
    right_bracket_count = 0
    
    for i in range(len(equation)):
        if equation[i] == '(' and bracket_flag == False:
            bracket_flag = True
            left_bracket_count += 1
            equation[i] = None
            continue
        if equation[i]  == '(':
            copy = equation[i][:]
            new_equation.append(copy)
            left_bracket_count += 1
            equation[i] = None
            continue
        if equation[i] == ')' and left_bracket_count == (right_bracket_count + 1):
            equation[i] = calculations(new_equation)[0]
            new_equation = []
            bracket_flag = False
            left_bracket_count = 0
            right_bracket_count = 0
            continue
        if equation[i] == ')':
            copy = equation[i][:]
            new_equation.append(copy)
            right_bracket_count += 1
            equation[i] = None
            continue
        if bracket_flag != False:
            copy = equation[i][:]
            new_equation.append(copy)
            equation[i] = None
            
    for i in range(len(equation)):
        if equation[i] == '*' or equation[i] == '/':
            if equation[i] == '*':
                left = 1
                right = 1
                while equation[i-left] == None:
                    left +=1
                while equation[i+right] == None:
                    right +=1
                equation[i] = (equation[i-left][0]*equation[i+right][0],equation[i-left][1]*equation[i+right][1])
                equation[i-left] = None
                equation[i+right] = None
            if equation[i] == '/':
                left = 1
                right = 1
                while equation[i-left] == None:
                    left +=1
                while equation[i+right] == None:
                    right +=1
                equation[i] = (equation[i-left][0]*equation[i+right][1],equation[i-left][1]*equation[i+right][0])
                equation[i-left] = None
                equation[i+right] = None  
                
    for i in range(len(equation)):
        if equation[i] == '+' or equation[i] == '-':
            if equation[i] == '+':
                left = 1
                right = 1
                while equation[i-left] == None:
                    left +=1
                while equation[i+right] == None:
                    right +=1
                equation[i] = (equation[i-left][0]*equation[i+right][1] + equation[i-left][1]*equation[i+right][0],equation[i-left][1]*equation[i+right][1])
                equation[i-left] = None
                equation[i+right] = None
            if equation[i] == '-':
                left = 1
                right = 1
                while equation[i-left] == None:
                    left +=1
                while equation[i+right] == None:
                    right +=1
                equation[i] = (equation[i-left][0]*equation[i+right][1] - equation[i-left][1]*equation[i+right][0],equation[i-left][1]*equation[i+right][1])
                equation[i-left] = None
                equation[i+right] = None    
                    
    equation = anti_none(equation)
    return(equation)

while True:
    eq = input()                                             
    if eq == 'exit':
        break
    if eq == 'to double':
        try:
            print(exp[0]/exp[1])
            continue
        except NameError:
            print('Выражение еще не было введено!')
            continue
    if eq.find('save ') != -1:
        try:
            saves[eq[eq.find('save ')+len('save '):]] = answer
            print('Save was successful')
            continue
        except NameError:
            print('Выражения еще нет!')
            continue
    if eq.find('del ') != -1:
        try:
            saves.pop(eq[eq.find('del ')+len('del '):])
            print('Delete was successful')
            continue
        except KeyError:
            print('Такого сохранения нет!')
            continue     
    for k,v in saves.items():
        while eq.find(k) != -1:
            eq = eq[:eq.find(k)] + v + eq[eq.find(k)+len(k):]
            
    flag_err = False
    c_left = 0
    c_right = 0
    for i in range(len(eq)-1):
        if eq[i] == '(' and i != 0:
            if eq[i-1].isdigit() == True:
                eq = eq[:i] + '+' + eq[i:]
    for i in eq:
        if i == '(':
            c_left += 1
        if i == ')':
            c_right += 1
        if i.isdigit() == False:
            if i not in defoult_symbs:
                flag_err = True
                break
    if c_left != c_right:
        flag_err = True
    if flag_err == True:
        print('Ошибка: неправильно введено выражание')
        continue
    while eq.find(' ') != -1:
        eq = eq[:eq.find(' ')] + eq[eq.find(' ') + 1:]     
    
    chislo = []                                                  
    dig = 0
    exp = []    
    for i in eq:
        if i.isdigit() == True:
            chislo.append(int(i))
        else:
            for j in range(len(chislo)):
                dig = dig + chislo[j] * 10**(len(chislo)-1-j)
            chislo = []
            if dig != 0:
                exp.append((dig,1))
            exp.append(i)
            dig = 0
    if len(chislo)!=0:
        for j in range(len(chislo)):
                dig = dig + chislo[j] * 10**(len(chislo)-1-j)
        exp.append((dig,1)) 
    
    for i in range(len(exp)):                                                   
        if exp[i] == '(' and exp[i+1] == '-' and exp[i+3] == ')':
            exp[i] = None
            exp[i+1] = None
            exp[i+3] = None
            exp[i+2] = (exp[i+2][0] * -1, 1)
            
    exp = anti_none(exp)            
    exp = calculations(exp)
    exp = [exp[0][0],exp[0][1]]
    if exp[0] < 0 and exp[1] < 0:
        exp[0] = exp[0] * -1
        exp[1] = exp[1] * -1
    if exp[0] % exp[1] == 0:
        if exp[0] < 0 or exp[1] < 0:
            if exp[0] < 0:
                exp[0] *= -1
            if exp[1] < 0:
                exp[1] *= -1
            print(f'Ответ: -{exp[0]//exp[1]}')
            answer = '(' + str(-1) + ')' + '*' + str(exp[0] // exp[1])
        else:
            print(f'Ответ: {exp[0]//exp[1]}')
            answer = str(exp[0] // exp[1])
    elif exp[0] // exp[1] == 0:
        if exp[0] < 0 or exp[1] < 0:
            if exp[0] < 0:
                exp[0] *= -1
            if exp[1] < 0:
                exp[1] *= -1
            print(f'Ответ: -{exp[0]//exp[1]}')
            answer = '(' + str(-1) + ')' + '*' + str(exp[0] // exp[1])
        else:
            print(f'Ответ: {exp[0]//exp[1]}')
            answer = str(exp[0] // exp[1])
    else:
        if exp[0] > 0 and exp[1] > 0:
            for i in range(exp[1]+1,1,-1):
                if exp[0] % i == 0 and exp[1] % i == 0:
                    exp[0] //= i
                    exp[1] //= i
            print(f'Ответ: {exp[0]//exp[1]}({exp[0]%exp[1]}/{exp[1]})')
            answer = str(exp[0]) + '/' + str(exp[1])
        elif exp[0] < 0:
            exp[0] *= -1
            for i in range(exp[1]+1,1,-1):
                if exp[0] % i == 0 and exp[1] % i == 0:
                    exp[0] //= i
                    exp[1] //= i
            print(f'Ответ: -{exp[0]//exp[1]}({exp[0]%exp[1]}/{exp[1]})')
            answer = '(' + str(-1) + ')' + '*' + str(exp[0]) + '/' + str(exp[1])
        elif exp[1] < 0:
            exp[1] *= -1
            for i in range(exp[1]+1,1,-1):
                if exp[0] % i == 0 and exp[1] % i == 0:
                    exp[0] //= i
                    exp[1] //= i
            print(f'Ответ: -{exp[0]//exp[1]}({exp[0]%exp[1]}/{exp[1]})')
            answer = '(' + str(-1) + ')' + '*' + str(exp[0]) + '/' + str(exp[1])