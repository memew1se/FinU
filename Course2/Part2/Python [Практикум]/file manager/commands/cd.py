import os
from .command import Command
from multipledispatch import dispatch
from dotenv import load_dotenv


class Cd(Command):
    """Change directory"""

    load_dotenv()
    _HOME = str(os.getenv('PYSHELL_HOME'))

    @dispatch(str)
    def __init__(self, path):
        self.path = path

    @dispatch()
    def __init__(self):
        self.path = self._HOME

    @staticmethod
    def valuesAmount():
        return 0, 1

    def execute(self):
        absolute_path = os.getcwd() + '/' + self.path
        relative_path = self.path

        if os.path.isdir(absolute_path) and self._HOME in absolute_path:
            os.chdir(absolute_path)
        elif os.path.isdir(relative_path) and self._HOME in relative_path:
            os.chdir(relative_path)
        else:
            print('Нет такого каталога или к нему нету доступа')
