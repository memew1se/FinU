from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    """
    Imitation of terminal command

    ...

    Methods
    -------
    execute()
        Executes command
    valuesAmount()
        Returns a tuple with a possible numbers of values
    """

    params = []

    @abstractmethod
    def execute(self):
        """Main method that describes behavior of the class"""
        pass

    @abstractmethod
    def valuesAmount(self):
        """
        Checks if correct number of values was received

        Returns
        -------
        tuple
        """
        return

    def setParams(self, params: list):
        self.params = params
