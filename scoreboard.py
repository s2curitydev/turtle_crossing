from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(200, 260)
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def next_round(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)

