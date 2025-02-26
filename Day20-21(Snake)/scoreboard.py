from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        """
        Scoreboard class for Snake the game. Also used for onscreen text.
        """
        super().__init__()
        self.score = 0
        self.penup()
        self.sety(270)
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """
        Update score on scoreboard.
        """
        self.write(f"Score: {self.score}", align="center", font=("TimesNewRoman", 20, "normal"))

    def game_over(self) -> None:
        """
        Print ''GAME OVER'' in center of the screen.
        :return:
        """
        self.setpos(0, 0)
        self.write("GAME OVER", align="center", font=("TimesNewRoman", 20, "normal"))

    def increase_score(self) -> None:
        """
        Increase score.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()
