import InsectClass as ic


def main():
    mosquito = ic.Insect('mosquito', 2, 6)

    mosquito.set_flight()

    print(
        f'the {mosquito.get_name()} can fly this many miles: {mosquito.get_length_of_flight()}')


main()
