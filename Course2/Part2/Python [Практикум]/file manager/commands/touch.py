import os
from .command import Command


class Touch(Command):
    """Create file"""

    def __init__(self, file):
        self.file = file

    @staticmethod
    def valuesAmount():
        return 1,

    def execute(self):
        with open(self.file, 'w') as file:
            pass
