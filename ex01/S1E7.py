from S1E9 import Character


class Baratheon(Character):
    """ Representing the Baratheon family. """
    def __init__(self, first_name, is_alive=True, family_name='Baratheon',
                 eyes='brown', hairs='dark'):
        self.first_name = first_name
        self.is_alive = True
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """ In Python, f"" denotes an f-string, which stands for
        "formatted string literal." Introduced in Python 3.6,
        f-strings provide a way to embed expressions inside string literals,
        using curly braces {}. """
        return f"of Vector: ({str(self.family_name)}, {str(self.eyes)}, \
{str(self.hairs)})"

    def __repr__(self):
        return f"of Vector: ({repr(self.family_name)}, {repr(self.eyes)}, \
{repr(self.hairs)})"

    def die(self):
        """ Parent method is called by Baratheon """
        super().die()


class Lannister(Character):
    """ Representing the Lannister family. """
    def __init__(self, first_name, is_alive=True, family_name='Lannister',
                 eyes='blue', hairs='light'):
        self.first_name = first_name
        self.is_alive = True
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        return f"of vector: ({str(self.family_name)}, {str(self.eyes)}, \
                {str(self.hairs)})"

    def __repr__(self):
        return f"of Vector: ({repr(self.family_name)}, {repr(self.eyes)}, \
{repr(self.hairs)})"

    def die(self):
        """ Parent method is called by Lannister """
        super().die()

    def decorator(func):
        def wrapper(firstname, is_alive=True):
            result = func(firstname, is_alive)
            return result
        return wrapper

    @decorator
    def create_lannister(self, first_name):
        return Lannister(first_name)
