from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.finish = FINISH_LINE_Y

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.goto(STARTING_POSITION)

    def check_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
