import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Definitely Not Frogger")
screen.tracer(0)

player = Player()
cars = []

screen.listen()
screen.onkey(player.move, "Up")

loop_pass = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    loop_pass += 1

    if loop_pass % 6 == 0:
        cars.append(CarManager())
        loop_pass = 0

    for car_obj in cars:
        car_obj.move()

    screen.update()



