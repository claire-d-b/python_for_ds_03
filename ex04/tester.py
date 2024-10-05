from ft_calculator import calculator


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)
    i = [1, 1, 1]
    j = [1, 0.5, 4]
    calculator.true_div(i, j)


if __name__ == "__main__":
    main()
