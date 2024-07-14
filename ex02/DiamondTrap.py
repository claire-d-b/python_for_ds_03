from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Derives from 2 different classes."""
    def __init__(self, first_name):
        super().__init__(first_name)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    def die(self):
        """Your docstring for Method"""
        super().die()

    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hairs = color

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs

# C3 linearization is a way to figure out the order in which a program
# should look at classes to find a method or attribute
# when multiple inheritance is used. Here's a simple explanation:

# Purpose: When a class inherits from multiple other classes,
# C3 linearization helps to decide the order in which these
# parent classes are checked for methods or attributes.
# This order is called the Method Resolution Order (MRO).

# Rules:
#   - Local First: A class is checked before its parent classes.
#   - Inheritance Order: If one class inherits from another,
#   the parent class should come after the child class in the MRO.
#   - Respect Parent Order: The order of parents as defined in the class is
#   preserved.

# How It Works:
#   - Start with the class itself.
#   - Merge the MROs of the parent classes and the list of parents,
#   following the rules above.
#   - In the merge process, pick the first class from the lists that
#   doesn’t appear later in any list
#   (this ensures no parent class is skipped or taken out of order).

# see ChatGPT simple explanation of C3 linearization to counter the pb
# of inheritance in diamand.
