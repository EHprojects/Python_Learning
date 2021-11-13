from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping? Pong!")


# Right Paddle: wid = 20, hei = 100, xpos = 350, ypos = 0
# up / dn to control paddle 20 px mvmnt

def forward():
    r_paddle.forward(20)


def backward():
    r_paddle.backward(20)


r_paddle = Turtle()
r_paddle.color("white")
r_paddle.shape("square")
r_paddle.penup()
r_paddle.setheading(90)
r_paddle.shapesize(stretch_len=5)
r_paddle.setpos(x=350, y=0)
screen.listen()
screen.onkey(r_paddle.forward, "Up")
screen.onkey(r_paddle.backward, "Down")

screen.exitonclick()
