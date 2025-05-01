import tkinter as tk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


class PomodoroTimer:
    def __init__(self) -> None:
        """
        Well-known Pomodoro timer.
        """
        # initialize main variables
        self.reps = 0
        self.count_down_canvas = str()

        # initialize window
        self.window = tk.Tk()

        # initialize tomato on screen
        self.tomato_canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_img = tk.PhotoImage(file="tomato.png")
        self.text_on_tomato = str()

        # initialize labels, mode name and check mark
        self.mode_label = tk.Label()
        self.check_label = tk.Label()

        # initialize buttons
        self.button_start = tk.Button(text="Start", command=self.start_timer)
        self.button_reset = tk.Button(text="Reset", command=self.reset_timer)

    def window_setup(self) -> None:
        """
        Setup window for pomodoro timer.
        """
        self.window.title(string="Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)

    def update_timer(self) -> None:
        """
        Update time, mode name and count of check marks for Pomodoro timer.
        """
        self.tomato_canvas.itemconfig(self.text_on_tomato, text="00:00")
        self.mode_label.config(text="Timer", bg=YELLOW, font=(FONT_NAME, 42, "bold"), fg=GREEN)
        self.check_label.config(text="", bg=YELLOW, fg=GREEN)

    def start_timer(self) -> None:
        """
        The function of the button. Used for starting the countdown timer.
        """
        self.reps += 1
        if self.reps % 8 == 0:
            self.count_down(count=LONG_BREAK_MIN * 60)
            self.mode_label.config(text="Break", fg=RED)
        elif self.reps % 2 == 0:
            self.count_down(count=SHORT_BREAK_MIN * 60)
            self.mode_label.config(text="Break", fg=PINK)
        else:
            self.count_down(count=WORK_MIN * 60)
            self.mode_label.config(text="Work", fg=GREEN)

    def reset_timer(self) -> None:
        """
        The function of the button. Used for resetting the timer.
        """
        self.window.after_cancel(self.count_down_canvas)
        self.reps = 0
        self.update_timer()

    def count_down(self, count: int) -> None:
        """
        The timer function. Used to show time and check marks.
        :param count: seconds to count
        """
        seconds = count % 60
        if seconds < 10:
            seconds = "".join(("0", str(seconds)))
        self.tomato_canvas.itemconfig(self.text_on_tomato, text=f"{count // 60}:{seconds}")
        if count > 0:
            self.count_down_canvas = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            self.check_label.config(text="✔"*(self.reps // 2))

    def start(self) -> None:
        """
        Start Pomodoro timer.
        """
        # setup window
        self.window_setup()

        # setup and place the tomato on the screen
        self.tomato_canvas.create_image(100, 112, image=self.tomato_img)
        self.text_on_tomato = self.tomato_canvas.create_text(
            100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
        )
        self.tomato_canvas.grid(row=1, column=1)

        # place the mode name and check marks on the screen
        self.mode_label.grid(row=0, column=1)
        self.check_label.grid(row=3, column=1)

        # setup information on screen
        self.update_timer()

        # setup buttons
        self.button_start.grid(row=2, column=0)
        self.button_reset.grid(row=2, column=2)

        # don`t close until the user closes the program
        self.window.mainloop()


if __name__ == '__main__':
    timer = PomodoroTimer()
    timer.start()
