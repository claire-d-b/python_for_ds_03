def dotproduct(func):
    def wrapper(V1, V2):
        func(V1, V2)
    return wrapper

def add_vec(func):
    def wrapper(V1, V2):
        func(V1, V2)
    return wrapper
    
def sous_vec(func):
    def wrapper(V1, V2):
        func(V1, V2)
    return wrapper

class calculator:

    @dotproduct
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = 0
        for a,b in zip(V1, V2):
            res += a * b
        print(f"Dot product is: {res}")

    @add_vec
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = []
        for a,b in zip(V1, V2):
            res.append(float(a + b))
        print(f"Add Vector is: {res}")

    @sous_vec
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = []
        for a,b in zip(V1, V2):
            res.append(float(a - b))
        print(f"Sous Vector is: {res}")
