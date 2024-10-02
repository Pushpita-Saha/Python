# class Vehicle:
#     """ Base Class for all vehicles """
#
#     def __init__(self, name, manufacturer, color):
#         self.name = name
#         self.manufacturer = manufacturer
#         self.color = color
#
#     def turn(self, direction):
#         print('Turing', self.name, 'to', direction)
#
#
# class Car(Vehicle):
#     """ Car Class """
#
#     def __init__(self, name, manufacturer, color, year):
#         self.name = name
#         self.manufacturer = manufacturer
#         self.color = color
#         self.year = 2017
#         self.wheels = 4
#
#     def change_gear(self, gear):
#         """Method of changing gear"""
#         print(self.name, "is Changing gear to ", gear)
#
#     def turn(self, direction):
#         print(self.name, 'is turning', direction)
#
#
#
#
#     v = Vehicle("namaste", "PST", "Lavender", )
#
#     c.turn("Right")
#     v.turn("Left")

class Vehicle:
    """ Base Class for all vehicles """

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

class Car(Vehicle):
    """ Car Class """

    def __init__(self, name, manufacturer, color, year):
        print("Creating a car")
        super().__init__(name, manufacturer, color )
        self.year = 2017
        self.wheels = 4
if __name__ == "__main__":
    c = Car("Hello", "PST", "Lavender", "2024")
    print(c.name, c.year, c.wheels)
