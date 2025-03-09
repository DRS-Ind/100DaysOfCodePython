from turtle import Turtle
from random import randint, choice


class Car(Turtle):
    def __init__(self) -> None:
        """
        Class for car in the game.
        """
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(["red", "blue", "green", "yellow", "gray", "orange"]))
        self.penup()
        self.setpos(x=300, y=randint(-250, 250))
        self.move_accelerator = randint(7, 12)  # different speed for different cars

    def move(self) -> None:
        """
        The function of not an endless stream of the car in the game.
        """
        if self.xcor() > -320:
            self.backward(self.move_accelerator)


class CarLine:
    def __init__(self):
        """
        Class for group cars in the game.
        """
        self.garage = list()

    def add_car_to_the_line(self) -> None:
        """
        The function adds a new car to the stream.
        """
        if randint(1, 6) == 1:
            self.garage.append(Car())

    def move_the_line(self) -> None:
        """
        The function of not an endless stream of the cars in the game.
        """
        for car in self.garage:
            car.move()

    def speed_up(self) -> None:
        """
        The function is to speed up cars in the flow.
        """
        for car in self.garage:
            car.move_accelerator += 1


