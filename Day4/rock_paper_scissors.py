from random import randint


# Rock Paper Scissors
gestures = [""""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]


def game_rps() -> str:
    """
    The function for playing Rock Paper Scissors, for 4 day of codding.
    :return:
    """
    # Welcome message
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor")
    try:
        # receive player move
        player_choice = int(input(""))

        # catch non-positive numbers
        if player_choice < 0:
            raise IndexError

        # try print player`s gesture
        print(gestures[player_choice])

    # if gesture not exist, disqualified player
    except (ValueError, IndexError):
        return "Unacceptable gestures. Disqualification."

    # comp turn
    comp_choice = randint(0, 2)
    print(f"Computer chose:\n{gestures[comp_choice]}")

    # compare gestures and display the result
    if comp_choice == player_choice:
        return "Draw. Try again"
    elif comp_choice == 2 and player_choice == 0:
        return "You win"
    elif comp_choice == 0 and player_choice == 2:
        return "You lose"
    elif comp_choice < player_choice:
        return "You win"
    else:
        return "You lose"


if __name__ == '__main__':
    # start the game
    print(game_rps())
