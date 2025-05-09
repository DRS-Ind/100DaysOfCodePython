import random
import tkinter as tk
import pandas

BACKGROUND_COLOR = "#B1DDC6"


class FlashGame:
    def __init__(self) -> None:
        """
        The well-know Flash cards game.
        """
        # initialize variables for project
        self.word = None
        self.language = None
        self.card_image = None
        self.flip_timer = None

        try:  # if the file words_to_learn.csv is missing use flash_cards.csv instead
            self.cards = pandas.read_csv("words_to_learn.csv").to_dict(orient="records")
        except FileNotFoundError:
            self.cards = pandas.read_csv("flash_cards.csv").to_dict(orient="records")
        self.random_pair = random.choice(self.cards)  # generate a random word pair

        self.window = tk.Tk()

        self.card_canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

        self.wrong_image = tk.PhotoImage(file="images/wrong.png")
        self.right_image = tk.PhotoImage(file="images/right.png")
        self.card_back_image = tk.PhotoImage(file="images/card_back.png")
        self.card_front_image = tk.PhotoImage(file="images/card_front.png")

        self.wrong_button = tk.Button(image=self.wrong_image, command=self.random_word, highlightthickness=0)
        self.right_button = tk.Button(image=self.right_image, command=self.remove_cards_from_pull, highlightthickness=0)

        # setup user interface
        self.gui_setup()

    def gui_setup(self) -> None:
        """
        The function is to customize the user interface.
        """
        self.window.title(string="Flash")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.card_image = self.card_canvas.create_image(400, 263, image=self.card_front_image)
        self.language = self.card_canvas.create_text(400, 150, text="Italian", fill="black",
                                                     font=("Ariel", 40, "italic"))
        self.word = self.card_canvas.create_text(400, 263, text=self.random_pair["Italian"], fill="black",
                                                 font=("Ariel", 60, "bold"))
        self.card_canvas.grid(row=0, column=0, columnspan=2)  # columnspan used because word cards require more space

        self.wrong_button.grid(row=1, column=0)
        self.right_button.grid(row=1, column=1)

    def end_of_the_list(self) -> None:
        """
        The function to display congratulation message.
        """
        self.card_canvas.itemconfig(self.language, text="Congratulations")
        self.card_canvas.itemconfig(self.word, text="You`re learn them all!")

    def remove_cards_from_pull(self) -> None:
        """
        The right button`s function, used to remove a word card from learning.
        """
        # call the end_of_the_list function when it`s not possible to remove a pair of words otherwise call random_word
        try:
            self.cards.remove(self.random_pair)
            pandas.DataFrame(self.cards).to_csv("words_to_learn.csv", index=False)
        except ValueError:
            self.end_of_the_list()
        else:
            self.random_word()

    def random_word(self) -> None:
        """
        The button function, used to flip to another word card.
        """
        self.window.after_cancel(self.flip_timer)  # prevent flipping from last time
        try:
            self.random_pair = random.choice(self.cards)
        except IndexError:  # call the end_of_the_list function when all cards have been learned
            self.end_of_the_list()
        else:
            self.card_canvas.itemconfig(self.language, text="Italian", fill="black")
            self.card_canvas.itemconfig(self.word, text=self.random_pair["Italian"], fill="black")
            self.card_canvas.itemconfig(self.card_image, image=self.card_front_image)
            self.flip_timer = self.window.after(3000, self.flip_the_card)

    def flip_the_card(self) -> None:
        """
        The function for flipping a word card.
        """
        self.card_canvas.itemconfig(self.card_image, image=self.card_back_image)
        self.card_canvas.itemconfig(self.language, text="English", fill="white")
        self.card_canvas.itemconfig(self.word, text=self.random_pair["English"], fill="white")

    def start(self) -> None:
        """
        The function for start learning words.
        """
        self.flip_timer = self.window.after(3000, self.flip_the_card)

        self.window.mainloop()


if __name__ == "__main__":
    game = FlashGame()
    game.start()
