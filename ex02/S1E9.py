from abc import ABC, abstractmethod


class Character(ABC):
    """ Parent class """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """ Character is instantiated """
        self._first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """ Character method is called """
        if self.is_alive:
            self.is_alive = not self.is_alive


class Stark(Character):
    """ Child class: Stark """
    def __init__(self, first_name, is_alive=True):
        """ Stark is instantiated: Stark """
        super().__init__(first_name, is_alive)

    def die(self):
        """ Child method calls the parent's one : Stark """
        super().die()
