from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        """
        The scoreboard for the game Pong.
        """
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = {"left": 0, "right": 0}
        self.penup()
        self.sety(y=250)
        self.update_score()

    def update_score(self) -> None:
        """
        The function for updating the scoreboard.
        """
        self.clear()
        self.write(f"{self.score['left']} \t : \t {self.score['right']}",
                   align="center",
                   font=("Courier", 32, "normal"))

    def point_to_left(self) -> None:
        """
        The function is to raise the left's score.
        """
        self.score["left"] += 1
        self.update_score()

    def point_to_right(self) -> None:
        """
        The function is to raise the right's score.
        """
        self.score["right"] += 1
        self.update_score()
