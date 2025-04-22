# from tool import get_mouse_clic_coordinates
from turtle import Screen, shape
import pandas
from checker import Checker


def main() -> None:
    """
    The main function.
    """
    # initializing values
    screen, image, data = Screen(), 'blank_states_img.gif', pandas.read_csv("50_states.csv")
    game_checker = Checker(data=data)

    # screen setup
    screen.setup(width=780, height=550)
    screen.title("U.S States Guesser")
    screen.addshape(image)
    shape(image)

    # for using tool get_mouse_clic_coordinates() you need to comment screen.exitonclick() row
    # turtle.onscreenclick(get_mouse_clic_coordinates)
    # turtle.mainloop()

    # main loop
    while game_checker.right_guesses() < 50:
        user_answer = screen.textinput(
            title=f"{game_checker.right_guesses()}/50 States correct",
            prompt="What`s another state`s name?"
        ).title()

        # stop the game while type "exit"
        if user_answer == "Exit":
            game_checker.not_guessed()
            break

        game_checker.check_answer(guess=user_answer)

    screen.exitonclick()


if __name__ == "__main__":
    main()
