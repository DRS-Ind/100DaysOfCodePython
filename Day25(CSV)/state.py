from turtle import Turtle


class PinState(Turtle):
    def __init__(self, name: str, x_cor: float, y_cor: float) -> None:
        """
        The class for pinning the state`s name.
        :param name: get the name of the state
        :param x_cor: get x coordinate on the map
        :param y_cor: get y coordinate on the map
        """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(x=x_cor, y=y_cor)
        self.write(name)
