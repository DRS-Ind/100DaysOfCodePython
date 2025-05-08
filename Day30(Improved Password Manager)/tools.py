import string
import random


class PasswordGenerator:
    def __init__(self) -> None:
        """
        Password generator, what a surprise.
        """
        # generate lists for further work
        self.alphabet = string.ascii_letters
        self.digits = string.digits
        self.punctuation = string.punctuation

        # generate counts of the letters, numbers and symbols in a password
        self.letters_count = random.randint(8, 10)
        self.numbers_count = random.randint(2, 4)
        self.symbols_count = random.randint(2, 4)

    def generate(self) -> str:
        """
        The function for generating password.
        :return: randomly generated password
        """
        # generating password in sequence
        password_in_sequence = ("".join(random.choices(self.alphabet, k=self.letters_count)) +
                                "".join(random.choices(self.digits, k=self.numbers_count)) +
                                "".join(random.choices(self.punctuation, k=self.symbols_count)))

        # transform password into list and shuffle all elements
        split_password = list(password_in_sequence)
        random.shuffle(split_password)

        return ''.join(split_password)