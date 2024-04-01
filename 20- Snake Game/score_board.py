import turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_score_board()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score_board()
