import os


class Calculator:
    """
    Class for calculator of the four basic operations of arithmetic (addition, subtraction, multiplication and
    division).
    """

    def __init__(self, start_number: float) -> None:
        """
        Initialize class.
        """
        self._memory_number = start_number
        self._last_operation = None
        self.acceptable_operations = ["+", "-", "*", "/"]

    def __str__(self) -> str:
        """
        String representation of the last operation, also you can print it.
        :return: memory number
        """
        return str(self._last_operation)

    @property
    def memory_number(self) -> float:
        """
        Getter for memory number
        :return: result of all operations
        """
        return self._memory_number

    def make_operation(self, operation: str, number: float) -> None:
        """
        Make certain type of the operation with memory number and addition number.
        :param operation: take type of operation
        :param number:
        :return:
        """
        #  make operation
        if operation == "+":
            self.addition(second_addend=number)
        elif operation == '-':
            self.subtraction(subtrahend=number)
        elif operation == '*':
            self.multiplication(multiplicand=number)
        elif operation == '/':
            self.division(divisor=number)
        # Maybe next
        # %	Modulus	x % y
        # **	Exponentiation	x ** y
        # //	Floor division	x // y

    def addition(self, second_addend: float) -> float:
        """
        Represent the sum of the two addends
        :param second_addend: claim second addend
        :return: sum of those values
        """
        result = self._memory_number + second_addend
        # write into variable visual representation of the operation
        self._last_operation = f"{self._memory_number} + {second_addend} == {result}"
        self._memory_number = result
        return self._memory_number

    def subtraction(self, subtrahend: float) -> float:
        """
        Represent removal minuend from the subtrahend
        :param subtrahend: claim subtrahend
        :return: difference of those values
        """
        result = self._memory_number - subtrahend
        # write into variable visual representation of the operation
        self._last_operation = f"{self._memory_number} - {subtrahend} == {result}"
        self._memory_number = result
        return self._memory_number

    def multiplication(self, multiplicand: float) -> float:
        """
        Represent product of multiplier and multiplicand
        :param multiplicand: claim multiplicand
        :return: product of those values
        """
        result = self._memory_number * multiplicand
        # write into variable visual representation of the operation
        self._last_operation = f"{self._memory_number} * {multiplicand} == {result}"
        self._memory_number = result
        return self._memory_number

    def division(self, divisor: float) -> float:
        """
        Represent quotient of the dividend, which is divided by the divisor
        :param divisor: claim divisor
        :return: quotient of those values
        """
        try:
            result = self._memory_number / divisor
            # write into variable visual representation of the operation
            self._last_operation = f"{self._memory_number} / {divisor} == {result}"
            self._memory_number = result
            return self._memory_number
        except ZeroDivisionError:  # catch division by zero
            print("Impossible division on zero. Result haven`t change.")
            # write into variable visual representation of the zero division
            self._last_operation = f"{self._memory_number} / {divisor} == {self._memory_number}"
            # return memory number without change
            return self._memory_number


def main() -> None:
    try:
        # start variable for main loop (start new calculation)
        retry = 'n'
        while retry == 'n':
            # Welcome message
            print("W")

            # start variables such as Calculator class and change retry on 'y' for inner loop (continue calculating)
            calculator, retry = Calculator(start_number=float(input("What`s the first number?: "))), "y"

            while retry == "y":

                # ask about type of operation
                type_of_operation = input(f"Choose one of a operations {str(calculator.acceptable_operations)}: ")

                if type_of_operation not in calculator.acceptable_operations:  # catch wrong input for operation
                    raise ValueError

                second_number = float(input("What`s the next number?: "))

                calculator.make_operation(operation=type_of_operation, number=second_number)

                print(str(calculator))

                retry = input(f"Type 'yes' to continue calculating with {calculator.memory_number}, or type 'no' to "
                              f"start "
                              f"a new calculation: ")

                if retry not in ("y", "n"):
                    raise ValueError
                if retry == "n":
                    os.system('cls' if os.name == 'nt' else 'clear')

    except ValueError:
        print("Wrong input type. Try again.")
    except KeyboardInterrupt:
        print("\nSee you soon.")


if __name__ == '__main__':
    main()
