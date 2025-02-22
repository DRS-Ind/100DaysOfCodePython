import time
from turtle import Turtle, Screen


# screen setup
screen, x_pos, y_pos = Screen(), 0, 0
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake the game")
screen.tracer(0)  # setting screen update only on command

# initial snake setup
snake = [Turtle(shape="square") for _ in range(3)]
for segment in snake:
    segment.color("white")
    segment.penup()
    segment.setpos(x=x_pos, y=y_pos)
    x_pos -= 20

# command to update the screen
screen.update()

# test for snake move
while True:
    screen.update()  # update the snake after every move
    time.sleep(0.1)  # pause for smooth moving
    for i_segment in range(len(snake) - 1, 0, -1):
        new_x_pos = snake[i_segment - 1].xcor()
        new_y_pos = snake[i_segment - 1].ycor()
        snake[i_segment].setpos(x=new_x_pos, y=new_y_pos)
    snake[0].forward(20)
    snake[0].left(90)

# screen.exitonclick()
