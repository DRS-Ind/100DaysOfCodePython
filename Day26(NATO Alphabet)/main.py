import pandas


def main() -> None:
    """
    The main function.
    """
    # transform .csv file into pandas`s DataFrame
    alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

    # using list comprehension transform pandas`s DataFrame into a dictionary with a letter as key and the code as value
    nato_alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

    common_word = input().upper()  # get word from user

    # print a list of the NATO code words from a user`s word
    print([nato_alphabet_dict.get(letter) for letter in common_word])


if __name__ == '__main__':
    main()
