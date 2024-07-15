class calculator:

    def __init__(self, object):
        """ Calculator is instantiated """
        self.object = object.copy()

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
