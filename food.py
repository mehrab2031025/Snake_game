from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.penup()
        self.Move_Food()

    def Move_Food(self):
        new_x = randint(-330, 330)
        new_y = randint(-330, 330)
        self.goto(x=new_x, y=new_y)

