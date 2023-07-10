from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.pu()
            segment.setpos(i * -30, 0)
            self.snake.append(segment)

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)
    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)
    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)
    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.pu()
        segment.goto(position)
        self.snake.append(segment)
