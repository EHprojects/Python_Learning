from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim = Turtle(shape="turtle")
# tim.color("red")
# tim.penup()
# tim.goto(x=-230, y=-100)

all_turtles = []

start_y = -120
for i in range(len(colors)):
    all_turtles.append(Turtle(shape="turtle"))
    all_turtles[i].color(colors[i])
    all_turtles[i].penup()
    all_turtles[i].goto(x=-230, y=start_y)
    start_y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
