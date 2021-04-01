import os
from termcolor import colored
from commands import PYSHELL_COMMANDS


def shell():
    while True:
        commands_dict = PYSHELL_COMMANDS
        text = colored(os.getcwd(), 'green') + ":~$ "
        command = input(text).split()

        # for blank input
        if not command:
            continue

        # to exit from shell
        if command[0] == 'exit':
            break

        if command[0] not in commands_dict.keys():
            print(f"Команда \"{command[0]}\" не найдена")

        else:
            if len(command) > 1:
                if command[1][0] == "-":
                    params = command[1]
                    del(command[1])

                    if 'q' in params:
                        command = " ".join(command).split(' "')
                        command[-1] = command[-1][0: -1]
                        quotes = command[-1]
                        command = command[0:-1]
                        command = " ".join(command).split()
                        command.append(quotes)

            if len(command) - 1 in commands_dict[command[0]].valuesAmount():
                if len(command) == 1:
                    executor = commands_dict[command[0]]()
                else:
                    executor = commands_dict[command[0]](*command[1:])
                executor.execute()

            else:
                print('Неправильное количество аргументов')
