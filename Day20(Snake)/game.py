import time
from snake import Snake
from turtle import Turtle, Screen


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake the game")
screen.tracer(0)  # setting screen update only on command

# initial snake setup
snake = Snake()

# command to update the screen
screen.update()

# control movement of the snake
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# start the game
while True:
    screen.update()  # update the snake after every move
    time.sleep(0.1)  # pause for smooth moving
    snake.move()  # let`s move the snake

# screen.exitonclick()
