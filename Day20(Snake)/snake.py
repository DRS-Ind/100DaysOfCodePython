from turtle import Turtle


class Snake:
    def __init__(self) -> None:
        self.body = [Turtle(shape="square") for _ in range(3)]
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self) -> None:
        x_pos, y_pos = 0, 0
        for segment in self.body:
            segment.color("white")
            segment.penup()
            segment.setpos(x=x_pos, y=y_pos)
            x_pos -= 20

    def move(self) -> None:
        for i_segment in range(len(self.body) - 1, 0, -1):
            new_x_pos = self.body[i_segment - 1].xcor()
            new_y_pos = self.body[i_segment - 1].ycor()
            self.body[i_segment].setpos(x=new_x_pos, y=new_y_pos)
        self.head.forward(20)

    def up(self) -> None:
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self) -> None:
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self) -> None:
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self) -> None:
        if self.head.heading() != 0:
            self.head.setheading(180)

