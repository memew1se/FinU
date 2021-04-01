import os
from commands.command import Command
from multipledispatch import dispatch


class Echo(Command):
    """Display a line of text; can write it into the file"""

    @dispatch(str, str)
    def __init__(self, file, text):
        self.file = file
        self.text = text

    @dispatch(str)
    def __init__(self, text):
        self.text = text
        self.file = None

    @dispatch()
    def __init__(self):
        self.text = ''
        self.file = None

    @staticmethod
    def valuesAmount():
        return 0, 1, 2

    def execute(self):
        try:
            if self.file:
                file = open(self.file, 'w')
                file.write(self.text)
                file.close()
            else:
                print(self.text)
        except IsADirectoryError:
            print('%s является директорией' % self.file)
