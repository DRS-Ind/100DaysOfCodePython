import os
import random
from art import logo, vs
from game_data import data


class HigherLowerGame:
    def __init__(self) -> None:
        """
        Have fun and test your knowledge who has more followers on Instagram.
        """
        self.__score = 0  # variable for storing user`s score
        self._compare_a = None
        self._compare_b = None
        self._continue_game = True

    @property
    def score(self) -> int:
        """
        User`s score.
        """
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        """
        Setter for user`s score.
        """
        self.__score = value

    def _adjust_data_after_parse(self) -> None:
        """
        Function to fill class variables with data.
        """
        # generate data "A"
        if self._compare_a is None:  # check if first guess is the first in the game
            self._compare_a = parse_data_to_compare(random.randint(0, 49))
        else:  self._compare_a = self._compare_b  # else data "A" become data "B"

        # generate data "B"
        actual_data = parse_data_to_compare(random.randint(0, 49))
        while self._compare_a == actual_data:  # regenerate data "B" if it's the same as data "A"
            actual_data = parse_data_to_compare(random.randint(0, 49))
        self._compare_b = actual_data

    def compare_data(self) -> None:
        """
        Main function to compare data "A" and data "B".
        :return: itself if user was right
        """
        self._adjust_data_after_parse()  # assign the data their places

        # store values in variables
        value_a = [value for value in self._compare_a.values()][0]
        value_b = [value for value in self._compare_b.values()][0]
        os.system('cls' if os.name == 'nt' else 'clear')  # clear CLI, before showtime

        # visual showtime
        print(f"""{logo}
Compare A: {[key_data for key_data in self._compare_a][0]}
{vs}
Compare B: {[key_data for key_data in self._compare_b][0]}""")

        # user`s answer, make it lower case for easier user interaction
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        # check if user is right
        if (value_a > value_b and user_answer == "a") or (value_b > value_a and user_answer == "b"):
            self.score += 1
            return self.compare_data()  # start over
        else: self._continue_game = False  # you lose, if press wrong answer or anything but "A" or "B"

    def game_start(self) -> None:
        """
        Start the fun game if you can.
        """
        if self._continue_game:
            self.compare_data()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{logo}\nSorry that`s wrong. Final score: {self.score}")

def parse_data_to_compare(index: int) -> dict[str, int]:
    """
    Function for parsing data from game_data.py, especially for 14 day of codding.
    :return: dictionary with text in string format as key and followers in integer format as value
    """
    # the article is "an" for vowels and "a" for other
    article = ("an" if data[index]["description"].lower().startswith(("a", "e", "i", "o", "u")) else "a")
    return {
        f"{data[index]['name']}, {article} {data[index]['description']}, from {data[index]['country']}"
        :data[index]['follower_count']
    }


if __name__ == '__main__':
    game = HigherLowerGame()

    game.game_start()
