class calculator:

    def __init__(self, object):
        """Your docstring for Constructor"""
        self.object = object.copy()

    """to iterate over two iterables, we use zip"""
    def __add__(self, object) -> None:
        for i in range(len(self.object)):
            self.object[i] += object
        print(self.object)

    def __mul__(self, object) -> None:
        for i in range(len(self.object)):
            self.object[i] *= object
        print(self.object)

    def __sub__(self, object) -> None:
        for i in range(len(self.object)):
            self.object[i] -= object
        print(self.object)

    def __truediv__(self, object) -> None:
        try:
            assert object != 0, "Error: division by 0"
            for i in range(len(self.object)):
                self.object[i] /= object
            print(self.object)
        except AssertionError as e:
            print(f"AssertionError: {e}")