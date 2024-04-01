from colors_data import color_list
import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()


# timmy.setposition(-300, -300)
# for _ in range(12):
#     for _ in range(12):
#         color = random.choice(color_list)
#         timmy.dot(20, color)
#         timmy.forward(50)
#     position = timmy.position()
#     timmy.setposition(-300, position[1] + 50)

timmy.setheading(225)
number_of_dots_per_row = 10
timmy.forward(number_of_dots_per_row * 50 / 2)
timmy.setheading(0)

for dot_count in range(1, number_of_dots_per_row**2 + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % number_of_dots_per_row == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(50 * number_of_dots_per_row)
        timmy.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
