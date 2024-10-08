from S1E9 import Character


# A Class Decorator is declared just before a class declaration
def decorator(func):
    def wrapper(self, firstname, is_alive=True):
        result = func(self, firstname, is_alive)
        return result
    return wrapper


# A Python object has several special methods that provide
# specific behavior. There are two similar special methods
# that describe the object using a string representation.
# These methods are .__repr__() and .__str__().
# The .__repr__() method returns a detailed description
# for a programmer who needs to maintain and debug the code.
# The .__str__() method returns a simpler description with
# information for the user of the program.
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

    @decorator
    def create_Baratheon(self, first_name, is_alive=True):
        """Baratheon created"""
        return Baratheon(self, first_name)


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

    @decorator
    def create_lannister(self, first_name, is_alive=True):
        """Lannister created"""
        return Lannister(self, first_name)
