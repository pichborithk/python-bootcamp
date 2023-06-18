import turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANT = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[index - 1].position()
            self.segments[index].goto(new_position)

        self.head.forward(MOVE_DISTANT)

    def up(self):
        direction = int(self.head.heading())
        if direction != DOWN:
            self.head.setheading(UP)

    def down(self):
        direction = int(self.head.heading())
        if direction != UP:
            self.head.setheading(DOWN)

    def left(self):
        direction = int(self.head.heading())
        if direction != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        direction = int(self.head.heading())
        if direction != LEFT:
            self.head.setheading(RIGHT)
