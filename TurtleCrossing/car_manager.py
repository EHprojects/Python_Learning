from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        # new_car.hideturtle()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2)  # stretch length to 40px
        new_car.penup()
        # Car buffer zone = 50 px from top & bottom of screen (-240 to 240 for 20px cars)
        # start cars just off screen (x = 320)
        new_car.goto(x=320, y=random.randint(-240, 240))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.setx(car.xcor() - self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

