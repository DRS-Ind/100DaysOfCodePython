import pandas
from state import PinState


class Checker:
    def __init__(self, data: pandas.DataFrame) -> None:
        """
        The class checks answers from the user and data from the dataset.
        :param data: pandas`s DataFrame
        """
        self.data = data
        self.users_guesses = list()

    def right_guesses(self) -> int:
        """
        The function gives a count of how many states were guessed
        :return: int number of guessed states
        """
        return len(self.users_guesses)

    def not_guessed(self) -> None:
        """
        The function writes to the .csv file all the not-guessed states
        """
        not_guessed = self.data.state.to_list()
        for state in self.users_guesses:
            not_guessed.remove(state)
        result = {"state": not_guessed}
        pandas.DataFrame(result).to_csv("Not Guessed states")

    def check_answer(self, guess: str) -> None:
        """
        The function checks the answer and pins the state's name to the map if it`s correct.
        :param guess: user`s guess in str type
        """
        if guess in self.data.state.to_list() and guess not in self.users_guesses:
            self.users_guesses.append(guess)
            x_cor = self.data[self.data.state == guess]["x"].item()
            y_cor = self.data[self.data.state == guess]["y"].item()
            PinState(name=guess, x_cor=x_cor, y_cor=y_cor)

