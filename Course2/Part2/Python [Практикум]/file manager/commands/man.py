from commands.command import Command
from multipledispatch import dispatch


class Man(Command):
    """Documentation viewer"""

    @dispatch(str)
    def __init__(self, command: str):
        self.command = command

    @dispatch()
    def __init__(self):
        self.command = None

    def execute(self):
        if self.command:
            if self.command not in self.commands_dict.keys():
                print(f"Команда {self.command} не найдена")
            else:
                print(self.commands_dict[self.command].__doc__)
        else:
            print("Список доступных команд:")
            for key in self.commands_dict.keys():
                print(key)

    @classmethod
    def setCommands(cls, commands_dict: dict):
        cls.commands_dict = commands_dict

    @staticmethod
    def valuesAmount():
        return 0, 1

