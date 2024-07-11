from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
#your code here
    """Derives from 2 different classes."""
    def __init__(self, first_name):
        super().__init__(first_name)
    def __str__(self):
        return super().__str__()
        # return f"{str(self.family_name)}, {str(self.eyes)}, {str(self.hairs)}"
    def __repr__(self):
        return super().__repr__()
        # return f"{repr(self.family_name)}, {repr(self.eyes)}, {repr(self.hairs)}"
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

