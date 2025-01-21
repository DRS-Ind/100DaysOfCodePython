import os


def secret_auction() -> tuple[str | None, int | None]:
    """
    Function for secret auction, for day 9 of codding. (for better performance, it`s recommended to start a program
    from CLI)
    :return: winner name and his bid
    """
    # start function variables condition for continue and dictionary for clients and their bids
    another_bidder, auction  = 'yes', dict()

    # start loop before we run off bidders
    while another_bidder == 'yes':
        try:
            # start loop variables for name, bid
            game_name, game_bid = input("What is your name?: "), int(input("What`s your bid?: "))
            auction[game_name] = game_bid  # write name and bid to the auction dictionary
            another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")  # ask about continue
            if another_bidder not in ("yes", "no"):  # catch wrong frase for continue
                raise ValueError
            else:
                os.system('cls' if os.name == 'nt' else 'clear')  # if all ok clear the terminal, works for Win and Unix
        except ValueError:
            # end auction by accident
            print("The auction is compromised and ends now.")
            return None, None

    # find key of max value in auction dictionary
    winner_name = max(auction, key=lambda key: auction[key])
    return winner_name, auction[winner_name]


if __name__ == '__main__':
    # Welcome message
    print("""                     ___________
                     \\         /
                      )_______(
                      |\"\"\"\"\"\"\"|_.-._,.---------.,_.-._
                      |       | | |               | | ''-.
                      |       |_| |_             _| |_..-'
                      |_______| '-' `'---------'` '-'
                      )\"\"\"\"\"\"\"(
                     /_________\\
                     `'-------'`
                   .-------------.
                  /_______________\\
Welcome to the secret auction program.""")

    # print winner frase
    name, bid = secret_auction()
    if name and bid is not None:
        print(f"The winner {name} is with a bid of ${bid}.")
    else:
        pass
