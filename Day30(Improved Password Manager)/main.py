import json
import pyperclip
import tkinter as tk
from tkinter import messagebox
from tools import PasswordGenerator


class PasswordManager:
    def __init__(self) -> None:
        """
        GUI password manager generates and saves passwords for websites into a file.
        """
        # initialize window
        self.window = tk.Tk()

        # initialize canvas and implement image
        self.image_canvas = tk.Canvas(width=200, height=200)
        self.lock_image = tk.PhotoImage(file="logo.png")

        # initialize labels like website, email and password
        self.website_label = tk.Label(text="Website")
        self.email_label = tk.Label(text="Email/Username")
        self.password_label = tk.Label(text="Password")

        # initialize entries for website, email and password
        self.website_text = tk.Entry(width=35)
        self.email_text = tk.Entry(width=35)
        self.password_text = tk.Entry(width=21)

        # initialize buttons for generating a password and save data to the file
        self.generator_button = tk.Button(text="Generate Password", command=self.generate_password_at_entry)
        self.add_button = tk.Button(text="Add", width=36, command=self.save_to_file)
        self.search_button = tk.Button(text="Search", command=self.search_data_from_file)

    def save_to_file(self) -> None:
        """
        The function to save data about the website, email and password to a file.
        """
        website, email, password = self.website_text, self.email_text, self.password_text

        # pop-up window if one or more of the entries are empty
        if len(website.get()) == 0 or len(email.get()) == 0 or len(password.get()) == 0:
            messagebox.showinfo(
                title="Some of the fields empty",
                message="Check entries, maybe one or more of them are empty."
            )
        else:  # pop-up window if all fields are filled in to agree with the specified information
            to_save = messagebox.askokcancel(
                title="Check before",
                message=f"Check info before save:\n"
                        f"Website: {website.get()}\n"
                        f"Email/Password: {email.get()}\n"
                        f"Password: {password.get()}\n\n"
                        f"Save or no?")

            if to_save:  # if user agree save data to the file
                new_data = {
                    website.get(): {
                        "email": email.get(),
                        "password": password.get()
                    }
                }

                try:
                    # reading data from file
                    with open(file="password_data.json", mode="r") as file:
                        file_data = json.load(file)
                        file_data.update(new_data)  # update data with new information

                # catching a null file or non-existent file error
                except (FileNotFoundError, json.JSONDecodeError):
                    file_data = new_data

                else:
                    # saving data to the file
                    with open(file="password_data.json", mode="w") as file:
                        json.dump(file_data, file, indent=4)

                finally:
                    website.delete(0, tk.END)
                    password.delete(0, tk.END)

    def generate_password_at_entry(self) -> None:
        """
        The button`s function to generate password.
        """
        self.password_text.delete(first=0, last=tk.END)
        password = PasswordGenerator().generate()
        pyperclip.copy(password)  # copy password to the clipboard
        self.password_text.insert(index=0, string=password)

    def search_data_from_file(self) -> None:
        """
        The button`s function to search data from file.
        """
        try:
            with open(file="password_data.json", mode="r") as file:
                password_data = json.load(file)
                website_details = password_data[self.website_text.get()]
        except KeyError as error_ms:  # show a message when the website is absent from the file
            messagebox.showinfo(message=f"The website named {error_ms} has not found.")
        except FileNotFoundError:  # show a message when a file with data is not found
            messagebox.showwarning(title="Warning", message="File not found.")
        else:  # show a message with email and password information from the site
            messagebox.showinfo(title=f"{self.website_text.get()}",
                                message=f"Email: {website_details['email']}\n"
                                        f"Password: {website_details['password']}")

    def start(self) -> None:
        """
        The main function to start the manager.
        """
        self.window.title(string="Password Manager")
        self.window.config(pady=40, padx=40)

        self.image_canvas.create_image(100, 100, image=self.lock_image)
        self.image_canvas.grid(row=0, column=1)

        self.website_label.grid(row=1, column=0)
        self.email_label.grid(row=2, column=0)
        self.password_label.grid(row=3, column=0)

        self.website_text.grid(row=1, column=1, sticky="EW")
        self.website_text.focus()  # for cursor, to start from this point
        self.email_text.grid(row=2, column=1, columnspan=2, sticky="EW")
        self.email_text.insert(index=0, string="random@mail.com")  # already filled email
        self.password_text.grid(row=3, column=1, sticky="EW")

        self.generator_button.grid(row=3, column=2, sticky="EW")
        self.add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
        self.search_button.grid(row=1, column=2, sticky="EW")

        self.window.mainloop()


if __name__ == '__main__':
    app = PasswordManager()
    app.start()