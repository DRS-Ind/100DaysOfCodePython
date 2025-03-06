from turtle import Turtle


class HeroTurtle(Turtle):
    def __init__(self) -> None:
        """
        Class for turtle which is crossing the road.
        """
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.sety(-270)

    def move_up(self) -> None:
        """
        The function for moving up.
        """
        self.sety(y=self.ycor() + 10)

    def move_right(self) -> None:
        """
        The function for moving right.
        """
        if self.xcor() > 280:  # teleporting turtle if it bumps in the wall
            self.setx(x=-self.xcor())
        self.setx(x=self.xcor() + 10)

    def move_left(self) -> None:
        """
        The function for moving left.
        """
        if self.xcor() < -280:  # teleporting turtle if it bumps in the wall
            self.setx(x=-self.xcor())
        self.setx(x=self.xcor() - 10)

    def reset_pos(self) -> None:
        """
        The function of returning the turtle to the start.
        """
        self.setpos(x=0, y=-270)
