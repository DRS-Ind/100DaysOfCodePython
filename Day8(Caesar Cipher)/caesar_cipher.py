def caesar_cipher(shift: int, message: str, mode: str = "en") -> str:
    """
    Function for encoding or decoding message by caesar cipher.
    :param shift: how far to move the letters
    :param message: message for encoding/decoding
    :param mode: working mode (encode/decode), encode by default
    :return: encoded/decoded message
    """
    # if shift number bigger than alphabet, reduce it by number of letters in alphabet
    shift %= 26
    # variable for ciphered word and filter for all digits, symbols, etc
    accepted_number, ciphered_word = [index for index in range(65, 91)] + [index for index in range(97, 123)], list()

    if mode == "en" or mode == "encode":  # work in encode mode
        for letter in message:
            if ord(letter) in accepted_number:
                # if uppercase letter out of alphabet go to start
                if 65 <= ord(letter) <= 90 and ord(letter) + shift > 90:
                    ciphered_word.append(ord(letter) + shift - 90 + 64)
                # if lowercase letter out of alphabet go to start
                elif 97 <= ord(letter) <= 122 and ord(letter) + shift > 122:
                    ciphered_word.append(ord(letter) + shift - 122 + 96)
                else:
                    ciphered_word.append(ord(letter) + shift)
            else:  # all symbols, digits, etc.
                ciphered_word.append(ord(letter))
        return ''.join(chr(number) for number in ciphered_word)  # encoded message in string format
    elif mode == "de" or mode == "decode":
        for letter in message:
            if ord(letter) in accepted_number:
                # if uppercase letter out of alphabet go to end
                if 65 <= ord(letter) <= 90 and ord(letter) - shift < 65:
                    ciphered_word.append(ord(letter) - shift + 90 - 64)
                # if lowercase letter out of alphabet go to end
                elif 97 <= ord(letter) <= 122 and ord(letter) - shift < 97:
                    ciphered_word.append(ord(letter) - shift + 122 - 96)
                else:
                    ciphered_word.append(ord(letter) - shift)
            else:  # all symbols, digits, etc.
                ciphered_word.append(ord(letter))
        return ''.join(chr(number) for number in ciphered_word)  # encoded message in string format
    else:
        return f"Wrong mode equipped ({mode})"


def main() -> None:
    """
    The main function for working with Caesar cipher, ask questions and filling variables for 8 days of coding.
    """
    # start questions
    try:
        # transform type of operation in lowercase
        type_of_operation = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

        # catch wrong input
        if type_of_operation != "encode" and type_of_operation != "decode":
            raise ValueError

        user_message = input("Type your message:\n")
        shift_number = int(input("Type the shift number:\n"))

        # work if user decide encode or decode
        if type_of_operation == "decode":
            print(f"Here`s the decoded message: {caesar_cipher(shift=shift_number,
                                                               message=user_message,
                                                               mode=type_of_operation)}")
        elif type_of_operation == "encode":
            print(f"Here`s the result: {caesar_cipher(shift=shift_number,
                                                      message=user_message,
                                                      mode=type_of_operation)}")
    except ValueError:  # catch wrong type of operation or string instead of int in shift number
        print("Wrong input.")
    finally:  # in any case ask user about start again
        loop_question = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if loop_question == "yes":
            main()
        else:  # not need to hesitate
            print("Goodbye")


if __name__ == '__main__':
    # Welcome message
    print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

    # start program
    main()
