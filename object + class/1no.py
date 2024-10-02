# import turtle
# nonte = turtle.Turtle()
# fonte = turtle.Turtle()
#
# nonte.shape("circle")
# fonte.shape("square")
# nonte.left(62)
# fonte.forward(100)
#
# turtle.exitonclick()


# li = [1, 2, 3, 4, 5]
# print(dir(li))

# class Car:
#     name = "RollsRoyce"
#     color = "Lavender"
#
#     def start():
#         print('Starting the engine')
#
#
# print("Name of the car:", Car.name)
# print("colour:", Car.color)
#
# Car.start()

class Car:
    name = ""
    color = ""

    def start():
        print("Starting the engine")


Car.name = "Axio"
Car.color = "Black"
print('Name of the car:', Car.name)
print('Color:', Car.color)

Car.start()

print(dir(Car))

