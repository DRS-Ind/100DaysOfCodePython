import random


class GameBlackjack:
    """
    Class for playing BlackJack, for day 11 of codding.
    """
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10,
              "A": 11}
    "dictionary with each card and their value"
    cpu_hand, player_hand = {"hand": list(), "sum": int()}, {"hand": list(), "sum": int()}

    def __init__(self, decks: int = 1) -> None:
        """
        Take a pleasure while playing in Blackjack.
        :param decks: claim counts of decks used for game, but no more than 6
        """
        try:
            if decks > 6:
                raise ValueError
            elif not isinstance(decks, int):
                raise TypeError
        except TypeError:
            print("Wrong type for decks. Decks changed into 1, by default")
            decks = 1
        except ValueError:
            print("Decks for game must be 6 at max. Decks changed into 1, by default")
            decks = 1
        finally:
            self._decks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * decks

    def is_game_over(self) -> bool:
        """
        Function check is game over.
        :return: True or False
        """
        if self.player_hand["sum"] > 21 or self.cpu_hand["sum"] > 21:
            return True
        return False

    def is_game_win(self) -> bool:
        """
        Function check is game won.
        :return: True or False
        """
        if self.player_hand["sum"] == 21 or self.cpu_hand["sum"] == 21:
            return True
        return False

    def take_from_deck(self) -> tuple[str, int]:
        """
        Function for taking random card from the deck.
        :return: name of the card and that value
        """
        take = random.choice(self._decks)
        value = self.values.get(take)
        self._decks.remove(take)
        return take, value

    def player_draw(self) -> None:
        """
        Function which help player to take a card from deck.
        """
        card, value = self.take_from_deck()
        self.player_hand["hand"].append(card)
        self.player_hand["sum"] += value

    def cpu_draw(self) -> None:
        """
        Function which help player to take a card from deck.
        """
        card, value = self.take_from_deck()
        self.cpu_hand["hand"].append(card)
        self.cpu_hand["sum"] += value

    def __current_hand_situation(self) -> str:
        """
        Function only for show player his and cpu`s hands in the end.
        :return: cards in player`s hand and cpu`s hand
        """
        return f"Your final hand: {self.player_hand["hand"]}\nComputer`s final hand: {self.cpu_hand["hand"]}"

    @property
    def current_hand_situation(self) -> str:
        return self.__current_hand_situation()

    def game_set(self) -> None:
        """
        Main function. Use this for start the game.
        """
        # Welcome message
        print(f"""Welcome.
{'!' * 10} All Aces cost 11. {'!' * 10}""")
        # first move
        for _ in range(2):
            self.player_draw()
            self.cpu_draw()

        # for exception if from first move both player and cpu have 21
        if self.player_hand["sum"] == 21 == self.cpu_hand["sum"]:
            print(self.current_hand_situation)
            print("Push (non of you win)")

        # play until player lose or don`t want to draw
        hit = 'y'
        while hit == 'y':
            print(f"Your hand: {self.player_hand["hand"]}")
            print(f"Computer`s first card: {self.cpu_hand["hand"][0]}")
            if self.is_game_win() and self.player_hand["sum"] == 21:  # player win with 21 score
                print(self.current_hand_situation)
                print("You win (your hand is 21 score)")
                break
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == "y":  # player accept to draw
                self.player_draw()
                if self.is_game_over():  # player breaks his hand
                    print(self.current_hand_situation)
                    print("You lose (your hand is break)")
                    break
            else:  # player don`t want to draw
                break

        # cpu move, if player haven`t already win or lose and cpu`s hand less than 18
        while self.cpu_hand["sum"] <= 18 and not self.is_game_over() and not self.is_game_win():
            self.cpu_draw()
            if self.is_game_over():  # cpu breaks his hand
                print(self.current_hand_situation)
                print("You win (computer`s hand in break)")
                break
            elif self.is_game_win():  # cpu win with 21 score
                print(self.current_hand_situation)
                print("You lose (cpu`s hand is 21 score)")
                break

        # analyze result or not if game is over
        if not self.is_game_over() and not self.is_game_win():
            print(self.current_hand_situation)
            if self.cpu_hand["sum"] < self.player_hand["sum"]:
                print("You win")
            elif self.player_hand["sum"] < self.cpu_hand["sum"]:
                print("You lose")
            elif self.cpu_hand["sum"] == self.player_hand["sum"]:
                print("Push (non of you win)")


if __name__ == '__main__':
    game = GameBlackjack(decks=4)
    game.game_set()
