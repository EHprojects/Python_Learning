from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2)  # stretch length to 40px
        self.penup()

        # Car buffer zone = 50 px from top & bottom of screen (-240 to 240 for 20px cars)
        # start cars just off screen (x = 320)
        self.goto(x=320, y=random.randint(-240, 240))

    def move(self):
        self.setx(self.xcor() - STARTING_MOVE_DISTANCE)
