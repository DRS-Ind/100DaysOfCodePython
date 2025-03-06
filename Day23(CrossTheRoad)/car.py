from turtle import Turtle
from random import randint, choice


class Car(Turtle):
    def __init__(self) -> None:
        """
        Class for cars in the game.
        """
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(["red", "blue", "yellow", "gray", "cyan"]))
        self.penup()
        self.setpos(x=300, y=randint(-250, 250))
        self.move_accelerator = randint(5, 15)  # different speed for different cars

    def move(self) -> None:
        """
        The function of an endless stream of cars in the game.
        """
        if self.xcor() > -320:
            self.setx(x=self.xcor() - self.move_accelerator)
        else:
            self.setx(300)
