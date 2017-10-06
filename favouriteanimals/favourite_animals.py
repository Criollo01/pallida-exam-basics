# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them
import sys

class Controller(object):

    def argument_reader(self):
        print_help = Display()
        add_animals = AddAnimal()
        if len(sys.argv) == 1:
            print_help.usage()
        elif len(sys.argv) > 1:
            animals = sys.argv[1:]            


class Display(object):
    def usage(self):
        print("fav_animals [animal] [animal]")


class AddAnimal(object):
    def add_animal(self):
        with open ("favourites.txt", "a") as file:
            file.write(animals)


run = Controller()
run.argument_reader()