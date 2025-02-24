from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self) -> None:
        """
        Food class for snake.
        """
        super().__init__()
        self.shape(name="circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed(speed="fastest")
        self.appear()

    def appear(self) -> None:
        """
        Generate new portion of the food.
        """
        new_ycor, new_xcor = randint(-270, 270), randint(-270, 270)
        self.setpos(x=new_xcor, y=new_ycor)

