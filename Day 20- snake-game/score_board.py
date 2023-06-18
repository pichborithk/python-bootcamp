import turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.update_score_board()

    def update_score_board(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
