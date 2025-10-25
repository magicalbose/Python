class Parrot:

    species = "bird"

    def __init__(self, name, age):

        self.name = name
        self.age = age

bluparrot = Parrot("Blu", 10)

print("Blu is a {}.".format(bluparrot.species))

print("{} is {} years old.".format(bluparrot.name, bluparrot.age))