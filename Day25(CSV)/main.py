import pandas


def count_every_color(info: pandas.DataFrame, colors: list[str]) -> dict:
    return {color: len(info[info["Primary Fur Color"] == color]) for color in colors}


def main() -> None:
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
