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

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

loop_pass = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    loop_pass += 1

    car_manager.move_cars()

    # add new cars
    if loop_pass % 6 == 0:
        car_manager.create_car()
        loop_pass = 0

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # check if player has reached the other side
    if player.ycor() > 280:
        scoreboard.update_scoreboard()
        car_manager.increase_speed()
        player.reset_position()

    screen.update()

screen.exitonclick()
