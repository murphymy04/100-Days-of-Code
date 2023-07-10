import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle-Crossy Road")
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "space")

car_counter = 0
first_refresh = 6
second_refresh = 3
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create cars
    if scoreboard.level < 3:
        if car_counter == first_refresh:
            car_manager.create_car()
            car_counter = 0
        else:
            car_counter += 1
    elif scoreboard.level >= 3:
        if car_counter == second_refresh:
            car_manager.create_car()
            car_counter = 0
        else:
            car_counter += 1

    # move cars
    car_manager.move()

    # checks if turtle reached finish line or not
    if player.check_finish():
        player.level_up()
        car_manager.increase_speed()
        scoreboard.refresh()
    else:
        pass

    # collision
    for i in range(len(car_manager.car_list)):
        if player.distance(car_manager.car_list[i]) < 15:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
