import os
from .command import Command


class Mkdir(Command):
    """Make directory"""

    def __init__(self, dirName):
        self.dirName = dirName

    def execute(self):
        try:
            os.mkdir(self.dirName)
        except FileExistsError:
            print('Папка уже существует')

    @staticmethod
    def valuesAmount():
        return 1,
