from ft_calculator import calculator


def main():
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        calculator.dotproduct(a, b)
        calculator.add_vec(a, b)
        calculator.sous_vec(a, b)
        i = [1, 1, 1]
        j = [1, 0.5, 4]
        div = [3, 3]
        div_zero = [5, 0]
        calculator.true_div(i, j)
        # calculator.true_div(1, 0)
        calculator.true_div(div, div_zero)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
