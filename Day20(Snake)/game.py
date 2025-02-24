import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import ScoreBoard


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake the game")
screen.tracer(0)  # setting screen update only on command

# initialize variable for snake, food and scoreboard
snake, food, scoreboard = Snake(), Food(), ScoreBoard()

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

    # collide with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.appear()

    # collide with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        break

screen.exitonclick()
