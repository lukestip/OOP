import InsectClass as ic


def main():
    bug = ic.Insect()
    bug.set_flight()
    print('Insect can fly this many miles: ', bug.get_length_of_flight())


main()