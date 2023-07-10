from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.car_list = []

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(1, 2)
        new_car.pu()
        new_car.setposition(280, random.randint(-250, 250))
        new_car.left(180)
        new_car.color(COLORS[random.randint(0, 5)])
        self.car_list.append(new_car)

    def move(self):
        for i in range(len(self.car_list)):
            self.car_list[i].forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT


