import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import ScoreBoard


class SnakeTheGame:
    def __init__(self) -> None:
        self.screen = Screen()
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = ScoreBoard()
        self.is_game = True

    def screen_setup(self) -> None:
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake the game")
        self.screen.tracer(0)  # setting screen update only on command

        # control movement of the snake
        self.screen.listen()
        self.screen.onkey(fun=self.snake.up, key="Up")
        self.screen.onkey(fun=self.snake.down, key="Down")
        self.screen.onkey(fun=self.snake.left, key="Left")
        self.screen.onkey(fun=self.snake.right, key="Right")

    def start(self) -> None:
        self.screen_setup()
        # start the game
        while self.is_game:
            self.screen.update()  # update the snake after every move
            time.sleep(0.1)  # pause for smooth moving
            self.snake.move()  # let`s move the snake

            # collide with food
            if self.snake.head.distance(self.food) < 15:
                self.scoreboard.increase_score()
                self.snake.add_segment()
                self.food.appear()

            # collide with wall
            if (self.snake.head.xcor() > 290 or self.snake.head.xcor() < -290 or
                    self.snake.head.ycor() > 290 or self.snake.head.ycor() < -290):
                self.scoreboard.game_over()
                self.is_game = False

            # collide with itself
            for segment in self.snake.body[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.scoreboard.game_over()
                    self.is_game = False

        self.screen.exitonclick()


if __name__ == '__main__':
    game = SnakeTheGame()
    game.start()
