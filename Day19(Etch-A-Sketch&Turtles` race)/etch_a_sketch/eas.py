from turtle import Turtle, Screen


class EtchTurtle(Turtle):
    """Modified Turtle class for the Etch-A-Sketch game."""
    def move_forward(self) -> None:
        """Moves the turtle forward for 20."""
        self.forward(20)

    def move_backward(self) -> None:
        """Moves the turtle forward for 20."""
        self.back(20)

    def turn_left(self) -> None:
        """Turns the turtle left by 10."""
        self.left(10)

    def turn_right(self) -> None:
        """Turns the turtle right by 10."""
        self.right(10)

    def etch_a_sketch(self) -> None:
        """
        Listen keys for Etch-A-Sketch game.

        Keys:
        W -- for move turtle forward for 20.
        S -- for move turtle backward for 20.
        A -- for turn turtle for 10.
        D -- for turn turtle for 10.
        C -- for clear a screen and reset turtle position.
        """
        screen = Screen()
        screen.listen()
        screen.onkey(key="w", fun=self.move_forward)
        screen.onkey(key="s", fun=self.move_backward)
        screen.onkey(key="a", fun=self.turn_left)
        screen.onkey(key="d", fun=self.turn_right)
        screen.onkey(key="c", fun=self.clear)
        screen.onkey(key="c", fun=self.reset)
        screen.exitonclick()


if __name__ == '__main__':
    lil_turtle = EtchTurtle()
    lil_turtle.etch_a_sketch()
