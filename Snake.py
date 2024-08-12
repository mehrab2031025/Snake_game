from turtle import Turtle
import time
starting_coordinate = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):

        self.obj_list = []
        self.create_snake()


    def create_snake(self):
        for i in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(starting_coordinate[i])
            self.obj_list.append(tim)
        self.HEAD = self.obj_list[0]


    def move(self):
        for i in range(len(self.obj_list) - 1, 0, -1):
            (x, y) = self.obj_list[i - 1].pos()
            self.obj_list[i].goto(x, y)
        self.HEAD.forward(20)


    def up(self):
        if self.HEAD.heading() != DOWN:
            self.HEAD.setheading(UP)
    def down(self):
        if self.HEAD.heading() != UP:
            self.HEAD.setheading(DOWN)
    def right(self):
        if self.HEAD.heading() != LEFT:
            self.HEAD.setheading(RIGHT)
    def left(self):
        if self.HEAD.heading() != RIGHT:
            self.HEAD.setheading(LEFT)

    def extend(self):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(self.obj_list[-1].pos())
        self.obj_list.append(tim)

    def Reset(self):
        for i in self.obj_list:
            i.hideturtle()
        self.obj_list.clear()
        self.create_snake()
        time.sleep(2)






