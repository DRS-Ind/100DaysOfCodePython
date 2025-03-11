from turtle import Turtle
from tools import find_personal_score


class ScoreBoard(Turtle):
    def __init__(self, name: str) -> None:
        """
        Scoreboard class for Snake the game. Also used for onscreen text.
        """
        super().__init__()
        self.score = 0
        self.personal_score = find_personal_score(name=name)
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """
        Update score on scoreboard.
        """
        self.clear()
        self.sety(270)
        self.write(f"Score: {self.score}", align="center", font=("TimesNewRoman", 20, "normal"))

    def reset_scoreboard(self) -> None:
        self.score = 0
        self.update_scoreboard()

    def game_over(self) -> None:
        """
        Print ''GAME OVER'' in center of the screen.
        :return:
        """
        self.setpos(0, 0)
        self.write("GAME OVER\nPress 'r' to play again", align="center", font=("TimesNewRoman", 20, "normal"))

    def increase_score(self) -> None:
        """
        Increase score.
        """
        self.score += 1
        self.update_scoreboard()
