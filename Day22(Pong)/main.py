import time
from ball import Ball
from turtle import Screen
from paddle import Paddle
from scorepoard import ScoreBoard


class PongTheGame:
    def __init__(self) -> None:
        """
        Legendary game Pong.
        """
        self.screen = Screen()
        self.display_setup()
        self.right_paddle = Paddle(x_cor=350)
        self.left_paddle = Paddle(x_cor=-350)
        self.ball = Ball()
        self.scoreboard = ScoreBoard()

    def display_setup(self) -> None:
        """
        Display setting, like background color, title, etc.
        """
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)

    def game_start(self) -> None:
        """
        Used to start the game.
        """
        self.screen.listen()
        self.screen.onkeypress(fun=self.right_paddle.go_up, key="Up")
        self.screen.onkeypress(fun=self.right_paddle.go_down, key="Down")
        self.screen.onkeypress(fun=self.left_paddle.go_up, key="w")
        self.screen.onkeypress(fun=self.left_paddle.go_down, key="s")

        while True:  # let the endless game begin
            time.sleep(self.ball.movement_acceleration)
            self.screen.update()
            self.ball.move()

            # the ball bounces off walls
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce()

            # and bounces off paddles
            if ((self.ball.distance(self.right_paddle) < 50 and self.ball.xcor() > 320) or
                    (self.ball.distance(self.left_paddle) < 50 and self.ball.xcor() < -320)):
                self.ball.paddle_bounce()

            # the ball is out of bounds
            if self.ball.xcor() > 400:  # left gets a point
                self.ball.reset_position()
                self.scoreboard.point_to_left()
            elif self.ball.xcor() < -400:  # right gets a point
                self.ball.reset_position()
                self.scoreboard.point_to_right()


if __name__ == '__main__':
    game = PongTheGame()
    game.game_start()
