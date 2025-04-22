import pandas


def count_every_color(info: pandas.DataFrame, colors: list[str]) -> dict:
    """
    The function for making a dict from pandas`s DataFrame. It count every color appearance in the dataset.
    :param info: get pandas`s DataFrame for work
    :param colors: get list of colors
    :return: dict with color as key and count as value
    """
    return {color: len(info[info["Primary Fur Color"] == color]) for color in colors}


def main() -> None:
    """
    The main function.
    """
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    colors = data["Primary Fur Color"].drop_duplicates().to_list()[1:]
    colors_with_counts = count_every_color(info=data, colors=colors)
    result_in_dict = {
        "Fur color": colors,
        "Counts": colors_with_counts.values()
    }
    result = (pandas.DataFrame(result_in_dict))
    result.to_csv("squirrel_count.csv")


if __name__ == '__main__':
    main()
