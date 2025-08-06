import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizGUI:
    def __init__(self, brain: QuizBrain) -> None:
        """
        Front-end for quiz.

        :param brain: connect to the back-end
        """
        self.quiz_brain = brain

        self.window = tk.Tk()

        self.score_label = tk.Label(background=THEME_COLOR, fg="white", text="Score: 0")

        self.canvas = tk.Canvas(height=250, width=300)
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        self.true_img = tk.PhotoImage(file="images/true.png")
        self.false_img = tk.PhotoImage(file="./images/false.png")
        self.true_button = tk.Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.false_button = tk.Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)

        # set up gui component
        self.window_set_up()

        # generate first question
        self.get_new_question()

        self.window.mainloop()

    def window_set_up(self) -> None:
        """
        Function for setup all gui component.
        """
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.score_label.grid(row=0, column=1)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

    def get_new_question(self) -> None:
        """
        Main function. Update quiz score, text. Disable buttons when the quiz bank is empty.
        """
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You're reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self) -> None:
        """
        The function for pressing the true button.
        """
        self.give_feedback_color(self.quiz_brain.check_answer(user_answer="True"))

    def false_pressed(self) -> None:
        """
        The function for pressing the false button.
        """
        self.give_feedback_color(self.quiz_brain.check_answer(user_answer="False"))

    def give_feedback_color(self, answer: bool) -> None:
        """
        Change the color of the text canvas when the user answers.

        :param answer: result from checking answer
        """
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_new_question)
