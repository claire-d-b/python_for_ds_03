def d_dotproduct(func):
    def wrapper(V1, V2):
        iter(V1)
        iter(V2)
        res = 0
        for a, b in zip(V1, V2):
            res += func(a, b)
        print(f"Dot product is: {res}")
    return wrapper


def d_add_vec(func):
    def wrapper(V1, V2):
        iter(V1)
        iter(V2)
        res = []
        for a, b in zip(V1, V2):
            res.append(float(func(a, b)))
        print(f"Add Vector is: {res}")
    return wrapper


def d_sous_vec(func):
    def wrapper(V1, V2):
        iter(V1)
        iter(V2)
        res = []
        for a, b in zip(V1, V2):
            res.append(float(func(a, b)))
        print(f"Sous Vector is: {res}")
    return wrapper


def d_true_div(func):
    object != 0
    def wrapper(V1, V2):
        iter(V1)
        iter(V2)
        res = []
        for a, b in zip(V1, V2):
            res.append(float(func(a, b)))
        print(f"True Div Vector is: {res}")
    return wrapper


class calculator:

    @d_dotproduct
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Multiplication"""
        return V1 * V2

    @d_add_vec
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition"""
        return V1 + V2

    @d_sous_vec
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substraction"""
        return V1 - V2

    @d_true_div
    def true_div(V1: list[float], V2: list[float]) -> None:
        """Division"""
        return V1 / V2
