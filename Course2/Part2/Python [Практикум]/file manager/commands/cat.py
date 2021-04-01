import os
from .command import Command


class Cat(Command):
    """Print file contents"""

    def __init__(self, file):
        self.file = file

    def execute(self):
        try:
            with open(self.file) as file:
                for line in file:
                    print(line)
        except IsADirectoryError:
            print('%s это каталог' % self.file)

    @staticmethod
    def valuesAmount():
        return 1,
