from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        """
        The Ball for the game Pong.
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_acceleration = 10
        self.y_acceleration = 10
        self.movement_acceleration = .1

    def move(self) -> None:
        """
        The function for moving the ball.
        """
        self.setpos(x=self.xcor() + self.x_acceleration, y=self.ycor() + self.y_acceleration)

    def bounce(self) -> None:
        """
        The function for bouncing the ball from the walls.
        """
        self.y_acceleration *= -1

    def paddle_bounce(self) -> None:
        """
        The function for bouncing the ball from the paddles.
        """
        self.movement_acceleration *= .9
        self.x_acceleration *= -1

    def reset_position(self) -> None:
        """
        The function returns the ball to the center of the field.
        """
        self.movement_acceleration = .1
        self.home()
        self.paddle_bounce()
