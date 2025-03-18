def new_letter_data_with_new_name(name: str) -> list[str]:
    """
    The function read letter for name replace.
    :param name: name to be replaced
    :return: letter with replaced name
    """
    with open("Input/Letter/starting_letter.txt", "r") as letter:  # open example txt
        letter_data = letter.readlines()  # transform information from letter to the list
        letter_data[0] = letter_data[0].replace("[name]", name.strip(), 1)  # replace name in first line
        return letter_data


def main() -> None:
    """
    The main function.
    """
    with open("Input/Names/invited_names.txt", "r") as letter:  # open file with names
        names = letter.readlines()  # transform names from letter to the list
        for name in names:
            new_letter_data = new_letter_data_with_new_name(name=name)  # replace name in example with new name
            # rewrite or create new file with updated one
            with open(f"Output/ReadyToSend/letter_to_{name[:-2]}.txt", "a") as new_letter:
                new_letter.writelines(new_letter_data)  #


if __name__ == '__main__':
    main()
