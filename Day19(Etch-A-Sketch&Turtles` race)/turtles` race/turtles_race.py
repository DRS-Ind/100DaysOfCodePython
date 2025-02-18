import random
from turtle import Turtle, Screen


def race(racers_list: list[Turtle], bet_color: str) -> None:
    """
    Good-organized turtle race, all legal.
    :param racers_list: list of the turtles
    :param bet_color: user`s bet
    :return:
    """
    winner_color = None
    while winner_color is None:  # go until someone win
        for racer in racers_list:
            racer.forward(random.randint(0, 10))  # each turn each turtle moves forward a distance from 0 to 10
            if racer.xcor() >= 220:  # write down the color of the turtle that crosses the finish line first.
                winner_color = racer.color()[0]
    if bet_color != winner_color:
        print(f"You lost! The {winner_color} turtle is the winner!")
    else:
        print(f"You win! The {winner_color} turtle is the winner!")


if __name__ == '__main__':
    # race setup
    screen, colors, x_pos, y_pos = Screen(), ("red", "orange", "yellow", "green", "blue", "purple"), -230, -125
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    turtles = list()

    # color the turtles and place them at the start
    for i_turtle in range(6):
        lil_turtle = Turtle(shape="turtle")
        lil_turtle.penup()  # we don`t need a traces
        lil_turtle.color(colors[i_turtle])
        lil_turtle.setpos(x=x_pos, y=y_pos)
        turtles.append(lil_turtle)
        y_pos += 50

    # let the race begin
    if user_bet is not None:  # if we have a bet
        race(racers_list=turtles, bet_color=user_bet)
    else:
        print("Wrong turtle`s color")

    screen.exitonclick()
