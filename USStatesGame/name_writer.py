from turtle import Turtle


class NameWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

    def write_name(self, name, x, y):
        self.goto(x, y)
        self.write(name)
