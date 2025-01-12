def tip_calculator(total_bill: float, tip_to_add: float, people_count: int) -> float:
    """
    The function of splitting the bill along with the tip between several people, for the 2 day of codding.
    :param total_bill: claim total sum of bill
    :param tip_to_add: claim tip you want to add
    :param people_count: claim count people
    :return: divided bill for each person
    """
    return round(total_bill * (tip_to_add / 100 + 1) / people_count, 2)


if __name__ == '__main__':
    # Hello message
    print("Welcome to the tip calculator!")

    # Claim information from user about bill, tip and people count
    bill, tip, people = (float(input("What was the total bill? $")),
                         float(input("How much tip would you like to give? 10, 12, or 15? ")),
                         int(input("How many people to split the bill? ")))

    # Print result string with divided bill
    print("Each person should pay: ${}".format(tip_calculator(total_bill=bill,
                                                              tip_to_add=tip,
                                                              people_count=people)))
