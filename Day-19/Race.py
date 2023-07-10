from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, orange, "
                                                          "yellow, green, blue, purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(len(colors)):
    turt = Turtle(shape="turtle")
    turt.pu()
    turt.color(colors[turtle_index])
    turt.goto(-230, -100 + (turtle_index * 50))
    all_turtles.append(turt)

race_on = False
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle was the winner!")
            else:
                print(f"You've lost! The {winner} turtle was the winner!")

        distance = random.randint(0, 10)
        turtle.fd(distance)

screen.exitonclick()
