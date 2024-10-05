from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True, family_name='Baratheon',
                 eyes='brown', hairs='dark'):
        """Baratheon is instantiated"""
        self.first_name = first_name
        self.is_alive = True
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        # In Python, f"" denotes an f-string, which stands for
        # "formatted string literal." Introduced in Python 3.6,
        # f-strings provide a way to embed expressions inside string literals,
        # using curly braces {}
        """Print __str__: Baratheon"""
        return f"of Vector: ({str(self.family_name)}, {str(self.eyes)}, \
{str(self.hairs)})"

    def __repr__(self):
        """Print __repr__: Baratheon"""
        return f"of Vector: ({repr(self.family_name)}, {repr(self.eyes)}, \
{repr(self.hairs)})"

    def die(self):
        """Parent method is called (Baratheon)"""
        super().die()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True, family_name='Lannister',
                 eyes='blue', hairs='light'):
        """Lannister is instantiated"""
        self.first_name = first_name
        self.is_alive = True
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """Print __str__: Lannister"""
        return f"of vector: ({str(self.family_name)}, {str(self.eyes)}, \
                {str(self.hairs)})"

    def __repr__(self):
        """Print _repr__: Lannister"""
        return f"of Vector: ({repr(self.family_name)}, {repr(self.eyes)}, \
{repr(self.hairs)})"

    def die(self):
        """Parent method is called (Lannister)"""
        super().die()

    def decorator(func):
        def wrapper(self, firstname, is_alive=True):
            result = func(self, firstname, is_alive)
            return result
        return wrapper

    """Decorator mentioned"""
    @decorator
    def create_lannister(self, first_name, is_alive=True):
        """Lannister created"""
        return Lannister(self, first_name)
