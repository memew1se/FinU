import os
from .command import Command
from dotenv import load_dotenv
import shutil


class Move(Command):
    """Move file or directory to another place"""

    load_dotenv()
    _HOME = os.getenv('PYSHELL_HOME')

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def execute(self):
        try:
            if self.isDirectory(self.dst):
                shutil.copy(self.src, self.dst)
                os.remove(self.src)
            else:
                print('%s не является директорией' % self.dst)
        except FileNotFoundError:
            print('Файла %s не существует' % self.src)

    @staticmethod
    def valuesAmount():
        return 2,

    def isDirectory(self, path):
        absolute_path = os.getcwd() + '/' + path
        relative_path = path

        if os.path.isdir(absolute_path) and self._HOME in absolute_path:
            return True
        elif os.path.isdir(relative_path) and self._HOME in relative_path:
            return True
        else:
            return False
