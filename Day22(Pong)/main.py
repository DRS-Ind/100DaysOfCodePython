from turtle import Screen
from paddle import Paddle


class PongTheGame:
    def __init__(self) -> None:
        """
        Legendary game Pong.
        """
        self.screen = Screen()
        self.display_setup()
        self.right_paddle = Paddle(x_cor=350)
        self.left_paddle = Paddle(x_cor=-350)

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
        self.screen.onkey(fun=self.right_paddle.go_up, key="Up")
        self.screen.onkey(fun=self.right_paddle.go_down, key="Down")
        self.screen.onkey(fun=self.left_paddle.go_up, key="w")
        self.screen.onkey(fun=self.left_paddle.go_down, key="s")

        while True:
            self.screen.update()

        self.screen.exitonclick()


if __name__ == '__main__':
    game = PongTheGame()
    game.game_start()
