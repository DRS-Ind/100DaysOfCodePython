def band_name_generator(city_name: str, pet_name: str) -> str:
    """
    Function for generating band name, for the 1 day of codding.
    :param city_name: take city name
    :param pet_name: take pet name
    :return: string with proposition for band name
    """
    return f"Your band name could be {city_name} {pet_name}"


if __name__ == '__main__':
    # Claim information from user about his city and pet names
    city, pet = input("What's the name of the city you grew up in?\n"), input("What's your pet's name?\n")

    # Print string with proposition for user`s band name
    print(band_name_generator(city_name=city, pet_name=pet))