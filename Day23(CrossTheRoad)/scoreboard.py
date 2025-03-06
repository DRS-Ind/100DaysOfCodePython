from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        """
        Class for the in-game scoreboard.
        """
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.update_display()

    def update_display(self) -> None:
        """
        The function for updating the scoreboard.
        """
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 22, "normal"))

    def level_up(self) -> None:
        """
        The function for level up.
        """
        self.level += 1
        self.update_display()

    def game_over(self) -> None:
        """
        The function for showing ''GAME OVER''
        """
        self.home()
        self.write("GAME OVER", align="center", font=("Courier", 32, "normal"))
