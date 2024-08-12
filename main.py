from turtle import Turtle, Screen
from Snake import Snake
from food import Food
from score import Score
import time


def Draw_Border():
    border = Turtle()
    border.pencolor("white")
    border.hideturtle()
    border.teleport(-350, -350)
    border.goto(350, -350)
    border.goto(350, 350)
    border.goto(-350, 350)
    border.goto(-350, -350)


screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=800)
screen.title("Snake Game")
screen.bgcolor("black")
Draw_Border()

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

snake_is_on = True
while snake_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.HEAD.distance(food) < 15:
        food.Move_Food()
        score.point()
        snake.extend()

    if snake.HEAD.xcor() <= -350 or snake.HEAD.xcor() >= 350 or snake.HEAD.ycor() <= -350 or snake.HEAD.ycor() >= 350:
        score.check_high_score()
        snake.Reset()

    for i in snake.obj_list[1:]:
        if snake.HEAD.distance(i) < 15:
            score.check_high_score()
            snake.Reset()

screen.exitonclick()
