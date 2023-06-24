from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(name="turtle")
        self.setheading(to_angle=90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(distance=MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
