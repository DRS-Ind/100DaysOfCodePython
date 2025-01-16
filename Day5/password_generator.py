import string
import random


# generate lists for further work
alphabet, digits, punctuation = string.ascii_letters, string.digits, string.punctuation


def password_generator_easy_mode(letters_count: int, numbers_count: int, symbols_count: int) -> str:
    """
    The function for generating password in easy mode, for 5 day of codding.
    :param letters_count: claim letter`s count
    :param numbers_count: claim number`s count
    :param symbols_count: claim symbol`s count
    :return: randomly generated password in sequence
    """
    return ("".join(random.choices(alphabet, k=letters_count)) + "".join(random.choices(digits, k=numbers_count))
            + "".join(random.choices(punctuation, k=symbols_count)))


def password_generator_hard_mode(letters_count: int, numbers_count: int, symbols_count: int) -> str:
    """
    The function for generating password in hard mode, for 5 day of codding.
    :param letters_count: claim letter`s count
    :param numbers_count: claim number`s count
    :param symbols_count: claim symbol`s count
    :return: randomly generated password
    """
    # generating password in sequence
    password_in_sequence = password_generator_easy_mode(letters_count, numbers_count, symbols_count)

    # transform password into list and shuffle all elements
    split_password = list(password_in_sequence)
    random.shuffle(split_password)

    return ''.join(split_password)


if __name__ == '__main__':
    # Welcome message
    print("Welcome to PyPassword Generator!")

    # get the count for letters, numbers and symbols
    letters = int(input("How many letters would you like in your password?\n"))
    numbers = int(input("How many numbers would you like?\n"))
    symbols = int(input("How many symbols would you like?\n"))

    # generate password in easy mode
    print(f"Your password in easy mode is: {password_generator_easy_mode(letters_count=letters,
                                                                         numbers_count=numbers,
                                                                         symbols_count=symbols,)}")

    # generate password in hard mode
    print(f"Your password in hard mode is: {password_generator_hard_mode(letters_count=letters,
                                                                         numbers_count=numbers,
                                                                         symbols_count=symbols,)}")
