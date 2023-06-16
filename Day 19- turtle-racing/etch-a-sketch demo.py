import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    timmy.forward(distance=10)


def move_backward():
    timmy.backward(distance=10)


def turn_left():
    # timmy.left(angle=10)
    new_heading = timmy.heading() + 10
    timmy.setheading(to_angle=new_heading)


def turn_right():
    # timmy.right(angle=10)
    new_heading = timmy.heading() - 10
    timmy.setheading(to_angle=new_heading)


def clear():
    # timmy.clear()
    # timmy.penup()
    # timmy.home()
    # timmy.pendown()
    timmy.reset()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
