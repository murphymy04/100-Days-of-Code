from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.pu()
        self.goto(-210, 250)
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)

    def refresh(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)