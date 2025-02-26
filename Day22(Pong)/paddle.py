from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor: int, y_cor: int = 0) -> None:
        """
        Class for create a paddle for game Pong.
        :param x_cor: set the x coordinate
        :param y_cor: set the y coordinate, 0 by default
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setpos(x=x_cor, y=y_cor)
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def go_up(self) -> None:
        """
        The function for move paddle up.
        """
        if self.ycor() < 230:
            self.setpos(x=self.xcor(), y=self.ycor() + 20)

    def go_down(self) -> None:
        """
        The function for move paddle down
        """
        if self.ycor() > -230:
            self.setpos(x=self.xcor(), y=self.ycor() - 20)
