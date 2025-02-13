import random
import turtle
from turtle import Turtle, Screen
from color_parse import prepared_colors


def draw_the_line() -> None:
    """
    Draw line with 10 dots.
    """
    for _ in range(10):
        turtle.dot(20, random.choice(prepared_colors))
        turtle.forward(50)


def main() -> None:
    """
    Function for draw 100 dots.
    """
    # preparation
    # initialize Turtle and screen, also set start position for turtle
    lil_turtle, screen, x_pos, y_pos = Turtle(), Screen(), -225, -225
    turtle.ht()  # hide turtle from user
    screen.clear()  # clean screen from first appearance of turtle
    turtle.penup()  # turtle`s pen up, don`t do the mess, don`t draw the line
    turtle.colormode(255)  # change colormode for accepting RGB code
    turtle.speed(0)  # up speed to fastest

    # draw a ten lines
    for _ in range(10):
        turtle.setpos(x_pos, y_pos)  # change position for turtle
        draw_the_line()
        y_pos += 50  # up turtle line start position on 50

    screen.exitonclick()


if __name__ == '__main__':
    main()
