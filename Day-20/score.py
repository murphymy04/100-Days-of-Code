from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0, 260)
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
