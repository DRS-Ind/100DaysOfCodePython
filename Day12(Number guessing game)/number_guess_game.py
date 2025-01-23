import random

class GuessGame:
    def __init__(self, min_number: int = 1, max_number: int = 100) -> None:
        """
        Try to beat a computer, find the guessed number.
        :param min_number: set the lower limit of the guessing range
        :param max_number: set the upper limit of the guessing range
        """
        self._difficult = None
        self._min_number = min_number
        self._max_number = max_number
        self._attempts = {"easy": 10, "hard": 5}
        self.__secret_number = random.randint(min_number, max_number)

    def __str__(self) -> str:
        """
        Representation of class in string form.
        :return: welcome message and show between which numbers the computer thinks about guessed number
        """
        return f"""  _  _            _                ___                _              ___                
 | \\| |_  _ _ __ | |__  ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
 | .` | || | '  \\| '_ \\/ -_) '_| | (_ | || / -_|_-<_-< | ' \\/ _` | | (_ / _` | '  \\/ -_)
 |_|\\_|\\_,_|_|_|_|_.__/\\___|_|    \\___|\\_,_\\___/__/__/_|_||_\\__, |  \\___\\__,_|_|_|_\\___|
                                                            |___/                       
                Welcome to the Number Guessing Game!
I`m thinking of a number between {self._min_number} and {self._max_number}"""

    @property
    def secret_number(self) -> int:
        """
        Get secret number for work.
        """
        return self.__secret_number

    def set_difficult(self, difficult_value: str = None) -> None:
        """
        Function for setting difficult.
        :param difficult_value: take 'easy' or 'hard' for setting the game mode
        """
        if not isinstance(difficult_value, str) or difficult_value not in ("easy", "hard"):  # catch wrong input
            self._difficult = "easy"
            print("Wrong value for difficult or difficult not selected. Set 'easy' by default")
        else:
            self._difficult = difficult_value

    def game_start(self) -> None:
        """
        Main function start The Number Guess Game.
        """
        self.set_difficult(self._difficult)  # check difficult
        while self._attempts[self._difficult] > 0:  # play until you have attempts
            try:
                print(f"You have {str(self._attempts[self._difficult])} attempts remaining to guess the number.")
                user_number = int(input("Make a guess: "))
                if user_number == self.secret_number:
                    print("You win.")
                    break
                elif user_number != self.secret_number and self._attempts[self._difficult] == 1:
                    print("You lose")
                    print(f"The guessed number is {self.__secret_number}")
                    break
                elif user_number > self.secret_number:
                    print("Your number is bigger than mine.")
                else:
                    print("Your number is less than mine.")
                self._attempts[self._difficult] -= 1
                print("Guess again.")
            except ValueError:  # inform player about wrong input
                print("Wrong type of input. You lose a try.")
                if self._attempts[self._difficult] > 1:
                    self._attempts[self._difficult] -= 1
                # fixed an issue where the player does not have a game over message when entering data incorrectly
                else:
                    self._attempts[self._difficult] -= 1
                    print("You lose")
                    print(f"The guessed number is {self.__secret_number}")


if __name__ == '__main__':
    game = GuessGame()  # initialize the game class

    print(game)  # print welcome message and information about guessing range

    game.set_difficult(difficult_value=input("Choose a difficulty. Type 'easy' or 'hard': "))  # set game difficult

    game.game_start()  # start the game
