import os
from multipledispatch import dispatch
from commands.command import Command


class Rm(Command):
    """Delete file or directory"""

    def __init__(self, file):
        self.file = file

    def execute(self):
        try:
            if os.path.isfile(self.file):
                os.remove(self.file)
            elif os.path.isdir(self.file):
                os.rmdir(self.file)
        except OSError:
            print('Директория %s не пуста' % self.file)

    @staticmethod
    def valuesAmount():
        return 1,
