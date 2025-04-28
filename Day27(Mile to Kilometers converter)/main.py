import tkinter as tk


def miles_to_km_converter(miles: int | float) -> float:
    """
    The function converts miles to kilometers.
    :param miles: miles to convert
    :return: kilometers
    """
    return miles * 1.60934


def button_clicked() -> None:
    """
    The function that is triggered when a user clicks the button.
    """
    miles = entry.get()
    calc_kilom_label.config(text=str(miles_to_km_converter(miles=float(miles))))


if __name__ == "__main__":
    # window initialization and configuration
    window = tk.Tk()
    window.title("Mile to kilometers converter")
    window.minsize(width=200, height=50)
    window.config(padx=20, pady=30)

    # pack of labels initialization and configuration
    equal_label = tk.Label(text="is equal to")
    equal_label.grid(row=1, column=0)

    miles_label = tk.Label(text="Miles")
    miles_label.grid(row=0, column=2)

    km_label = tk.Label(text="Km")
    km_label.grid(row=1, column=2)

    calc_kilom_label = tk.Label(text="0")
    calc_kilom_label.grid(row=1, column=1)

    # entry initialization and configuration
    entry = tk.Entry(width=8)
    entry.grid(row=0, column=1)

    # button initialization and configuration
    button = tk.Button(text="Calculate", command=button_clicked)
    button.grid(row=2, column=1)

    # Make the window open until the user closes it
    window.mainloop()
