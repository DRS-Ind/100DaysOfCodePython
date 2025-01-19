from faker import Faker
from hangman_status_and_art import hangman_status, welcome_art


def hangman_the_game(guessed_word: str) -> None:
    """
    Function for playing hangman, for 7 day of codding.
    :param guessed_word: get word for guessing
    """
    # ciphered word with underscore
    ciphered_word = list(len(guessed_word) * "_")

    print(guessed_word)

    lives, used_letters = 6, list()  # make variable for lives and used letters

    # start game
    while lives > 0 and ''.join(ciphered_word) != guessed_word:  # play until you win or lose

        # current situation
        print(f"""{hangman_status[lives]}
{'*' * 10}Lives: {lives}/6 {'*' * 10}
Word to guess: {"".join(ciphered_word)}""")
        guessed_letter = input("Guess a letter: ").lower()  # get a guess

        if guessed_letter in used_letters:  # warning about already used letter
            print("Letter already used")
        elif guessed_letter in guessed_word:  # work with right guess
            used_letters.append(guessed_letter)  # update the used letter list

            # open all right guessed letter
            indexes = [index for index, letter in enumerate(guessed_word) if letter == guessed_letter]
            for letter_index in indexes:
                ciphered_word[letter_index] = guessed_letter
        else:  # work with wrong guess
            lives -= 1
            used_letters.append(guessed_letter)  # update the used letter list
            print(f"You guessed {guessed_letter}, that`s not in the word. You lose a life.")

    # Result of the game
    if lives > 0:
        print(f"""{hangman_status[-1]}
Guessed word: {guessed_word}
{'!' * 10} You win {'!' * 10}""")
    else:
        print(f"""{hangman_status[lives]}
        Game Over""")


if __name__ == '__main__':
    # Welcome message
    print(welcome_art)

    # generate random word in lowercase
    random_word = Faker().word().lower()

    # start the game
    hangman_the_game(guessed_word=random_word)
