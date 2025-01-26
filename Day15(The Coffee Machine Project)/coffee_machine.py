class Coffee:
    def __init__(self, water: int, coffee: int, milk: int, price: float, name: str) -> None:
        """
        A class for a cup of coffee.
        """
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.price = price
        self.name = name

    def __str__(self) -> str:
        return (f"Coffee {self.name} that contains {self.water} ml of water, {self.coffee} g of coffee and {self.milk} "
                f"ml of milk. Price: ${self.price}.")

class Espresso(Coffee):
    def __init__(self) -> None:
        """
        A cup of Coffee Espresso.
        """
        super().__init__(water=50, coffee=18, milk=0, price=1.5, name="Espresso")

class Latte(Coffee):
    def __init__(self) -> None:
        """
        A cup of Coffee Latte.
        """
        super().__init__(water=200, coffee=24, milk=150, price=2.5, name="Latte")

class Cappuccino(Coffee):
    def __init__(self) -> None:
        """
        A cup of Coffee Cappuccino.
        """
        super().__init__(water=250, coffee=24, milk=100, price=3.0, name="Cappuccino")

class CoffeeMachine:
    def __init__(self) -> None:
        """
        Coffee machine with already filled tanks.
        """
        self._water_tank = 300
        self._milk_tank = 0
        self._coffee_tank = 100
        self._money_bank = 0
        self._stand_by = True
        self._coffee_set = {"espresso": Espresso(), "latte": Latte(), "cappuccino": Cappuccino()}
        self._possible_prompt = ["off"] + [coffee for coffee in self._coffee_set]

    def report(self) -> str:
        """
        Report about machine filling.
        """
        return f"""Water: {self._water_tank}ml
Milk: {self._milk_tank}ml
Coffee: {self._coffee_tank}g
Money: ${self._money_bank}"""

    def is_enough_resources(self, coffee: Coffee) -> bool:
        """
        The function checks whether there are enough resources to prepare a certain type of coffee.

        :param coffee: takes Coffee type
        """
        if coffee.water > self._water_tank:
            print("Sorry there is not enough water.")
            return False
        elif coffee.coffee > self._coffee_tank:
            print("Sorry there is not enough coffee.")
            return False
        elif coffee.milk > self._milk_tank:
            print("Sorry there is not enough milk.")
            return False
        return True

    def start_machine(self) -> None:
        """
        The main function for starting the coffee machine
        """
        if self._stand_by:
            self.check_user_prompt()
        else: print("Machine under maintenance.")

    def check_user_prompt(self) -> None:
        """
        The function checks users` prompts.
        """
        user_prompt = input(f"What would you like? ({'/'.join(self._possible_prompt[1:])})").lower()
        if user_prompt == "off":
            print("Off")
            self._stand_by = False
        else:
            if user_prompt in self._possible_prompt[1:]:
                if self.is_enough_resources(coffee=self._coffee_set[user_prompt]):
                    print("Coffee")
            else: print(f"Wrong coffee name. Possible coffee: {", ".join(self._possible_prompt[1:])}")
            self.check_user_prompt()


if __name__ == '__main__':
    machine = CoffeeMachine()

    machine.start_machine()
