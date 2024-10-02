class Vehicle:
    """ Base Class for all vehicles """

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print('Turing', self.name, 'to', direction)

    def brake(self):
        print(self.name, "is stopping!")


# if __name__ == "__main__":
#     v1 = Vehicle('Fusion360', "braa", 'purple')
#     v2 = Vehicle('Musion361', "praa", 'purble')
#     v3 = Vehicle('Tusion361', "Hraa", 'Kurble')
#
#
#     v1.drive()
#     v2.drive()
#
#     v3.turn("left")
#
#     v1.brake()


class Car(Vehicle):
    """ Car Class """

    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = 2017
        self.wheels = 4
        print("A new car has been created. Name:", self.name)
        print("It has", self.wheels, "Wheels")
        print("The car was built in ",self.year)

    def change_gear(self, gear):
        """Method of changing gear"""
        print(self.name, "is Changing gear to ", gear)


if __name__ == "__main__":
    c = Car("Hello","PST", "Lavender", "2024")

