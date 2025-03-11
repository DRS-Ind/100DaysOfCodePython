from turtle import Turtle


class Snake:
    def __init__(self) -> None:
        """
        Snake class for Snake the game.
        """
        self.body = [Turtle(shape="square") for _ in range(3)]
        self.create_snake()
        self.head = self.body[0]

    def blast_away(self) -> None:
        for seg in self.body:
            seg.setpos(x=1000, y=1000)

    def create_snake(self) -> None:
        """
        The setup function for the snake`s body is used to set up each snake segment.
        """
        x_pos, y_pos = 0, 0
        for segment in self.body:
            segment.color("white")
            segment.penup()
            segment.setpos(x=x_pos, y=y_pos)
            x_pos -= 20

    def add_segment(self) -> None:
        """
        Adding new segment for snake and teleport it in the end of the snake`s body.
        :return:
        """
        self.body.append(Turtle(shape="square"))
        self.body[-1].color("white")
        self.body[-1].penup()
        self.body[-1].setpos(self.body[-2].position())

    def move(self) -> None:
        """
        The function for the correct snake`s moving.
        """
        for i_segment in range(len(self.body) - 1, 0, -1):
            new_x_pos = self.body[i_segment - 1].xcor()
            new_y_pos = self.body[i_segment - 1].ycor()
            self.body[i_segment].setpos(x=new_x_pos, y=new_y_pos)
        self.head.forward(20)

    def up(self) -> None:
        """
        Function to rotate the snake's head upwards relative to the screen.
        """
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self) -> None:
        """
        Function to rotate the snake's head downwards relative to the screen.
        """
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self) -> None:
        """
        Function to rotate the snake's head right relative to the screen.
        """
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self) -> None:
        """
        Function to rotate the snake's head left relative to the screen.
        """
        if self.head.heading() != 0:
            self.head.setheading(180)
