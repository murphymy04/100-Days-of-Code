from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_on = False
        scoreboard.game_over()

    for segment in snake.snake:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
