import os
from .command import Command


class Rename(Command):
    """Rename file or directory"""

    def __init__(self, src, name):
        self.src = src
        self.name = name

    def execute(self):
        os.rename(self.src, self.name)

    @staticmethod
    def valuesAmount():
        return 2,

