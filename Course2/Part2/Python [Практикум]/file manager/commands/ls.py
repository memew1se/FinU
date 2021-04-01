import os
from multipledispatch import dispatch
from commands.command import Command
from termcolor import colored


class Ls(Command):
    """Lists files of current directory"""

    @dispatch(str)
    def __init__(self, path):
        self.path = path

    @dispatch()
    def __init__(self):
        self.path = os.getcwd()

    @staticmethod
    def valuesAmount():
        return 0, 1

    def execute(self):
        dirs = []
        files = []

        for file in os.listdir(self.path):
            if os.path.isdir(file):
                dirs.append(file)
            else:
                files.append(file)

        for file in dirs:
            print(colored(file, 'blue'))

        for file in files:
            print(file)





