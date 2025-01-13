def treasure_island_game():
    # Print logo and welcome message
    print("""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \\'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
            Welcome to Treasure Island.
        Your mission is to find the treasure.""")
    # first question
    first_decision = input('You\'re at a cross road. Where do you want to go?\n\tType "left" or "right"\n')
    # it is desirable to translate all answers in small letters, for check
    if first_decision.lower() != 'left':
        return "You fell into a hole. Game Over."  # first possible Game Over

    # second question
    second_decision = input('You\'ve come to a lake. There is an island in the middle of the lake.\n\tType "wait" to '
                            'wait for a boat. Type "swim" to swim across.\n')
    if second_decision.lower() != "wait":
        return "You get attacked by an angry trout. Game Over."  # second possible Game Over

    # third question
    third_decision = input('You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, '
                           'one yellow and one blue. Which colour do you choose?\n')
    if third_decision.lower() == "red":
        return "It`s a room full of fire. Game Over."  # third possible Game Over
    elif third_decision.lower() == "yellow":
        return "You found the treasure! You win!"  # desired treasure
    elif third_decision.lower() == "blue":
        return "You enter a room of beasts. Game Over."  # forth possible Game Over
    else:
        return "You stepped out of 3 dimension. Game Over."  # last possible Game Over


if __name__ == '__main__':
    # start the game here and print the result
    print(treasure_island_game())
