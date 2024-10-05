def dotproduct(func):
    def wrapper(V1, V2):
        res = 0
        for a, b in zip(V1, V2):
            res += a * b
        print(f"Dot product is: {res}")
    return wrapper


def add_vec(func):
    def wrapper(V1, V2):
        res = []
        for a, b in zip(V1, V2):
            res.append(float(a + b))
        print(f"Add Vector is: {res}")
    return wrapper


def sous_vec(func):
    def wrapper(V1, V2):
        res = []
        for a, b in zip(V1, V2):
            res.append(float(a - b))
        print(f"Sous Vector is: {res}")
    return wrapper

def true_div(func):
    try:
        object != 0
        def wrapper(V1, V2):
            res = []
            for a, b in zip(V1, V2):
                res.append(float(a / b))
            print(f"True Div Vector is: {res}")
    except Exception as e:
        print(f"AssertionError: {e}")
    return wrapper


class calculator:

    @dotproduct
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Multiplication"""

    @add_vec
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition"""

    @sous_vec
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substraction"""

    @true_div
    def true_div(V1: list[float], V2: list[float]) -> None:
        """Division"""

