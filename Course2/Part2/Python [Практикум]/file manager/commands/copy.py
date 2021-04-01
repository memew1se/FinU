import os
from .command import Command
import shutil
from dotenv import load_dotenv


class Copy(Command):
    """Copy file"""

    load_dotenv()
    _HOME = os.getenv('PYSHELL_HOME')

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def execute(self):
        if self.isDirectory(self.dst):
            shutil.copy(self.src, self.dst)
        else:
            print('%s не является директорией' % self.dst)

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
