from DiamondTrap import King


def main():
    try:
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.get_eyes.__doc__)
        print(Joffrey.get_hairs.__doc__)
        print(Joffrey.__dict__)

    except Exception as e:
        raise AssertionError(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
