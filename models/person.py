class Person:
    id_counter = 1

    def __init__(self, name):
        self.id = Person.id_counter
        Person.id_counter += 1
        self.name = name

        