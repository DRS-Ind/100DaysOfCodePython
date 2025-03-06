import time
from car import Car
from turtle import Screen
from hero import HeroTurtle
from scoreboard import ScoreBoard


class TurtleCrossTheRoad:
    def __init__(self) -> None:
        """
        Enjoy the game ''Cross the Road''.
        """
        self.screen = Screen()
        self.screen.tracer(0)
        self.scoreboard = ScoreBoard()
        self.hero = HeroTurtle()
        self.cars = [Car() for _ in range(10)]
        self.game_on = True
        self.screen_setup()

    def screen_setup(self) -> None:
        """
        The function for screen setup.
        :return:
        """
        self.screen.setup(width=600, height=600)
        self.screen.title("Cross the road")

    def start_game(self) -> None:
        """
        Start the game.
        """
        # listen to pressing the keyboard
        self.screen.listen()
        self.screen.onkeypress(fun=self.hero.move_up, key="Up")
        self.screen.onkeypress(fun=self.hero.move_right, key="Right")
        self.screen.onkeypress(fun=self.hero.move_left, key="Left")

        while self.game_on:  # start of the moving
            self.screen.update()  # update screen
            time.sleep(.1)
            [car.move() for car in self.cars]

            # return the turtle to the start and level up
            if self.hero.ycor() > 260:
                self.hero.reset_pos()
                self.scoreboard.level_up()

            # understanding collision turtle with the car
            for car in self.cars:
                if self.hero.distance(car) < 20:
                    self.game_on = False

        self.scoreboard.game_over()
        self.screen.exitonclick()


if __name__ == '__main__':
    game = TurtleCrossTheRoad()
    game.start_game()
