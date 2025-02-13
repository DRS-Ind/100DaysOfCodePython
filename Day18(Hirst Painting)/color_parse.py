from os import PathLike
from colorgram import extract


def rgb_color_extraction(file: PathLike[str] | str, amount_of_colors: int) -> list[tuple[float, float, float]]:
    """
    Parse an image for a certain number of colors and return them to a list with tuples (t, g, b) inside.
    Used colorgram.
    :param file: file for parsing
    :param amount_of_colors: amount of colors we need to parse
    :return: tuples with the values of RGB in a list
    """
    colors = extract(file, amount_of_colors)
    return [(color.rgb.r, color.rgb.b, color.rgb.b) for color in colors
            if color.rgb.r + color.rgb.g + color.rgb.b < 666]


prepared_colors = [(249, 17, 17), (213, 9, 9), (198, 35, 35), (231, 5, 5), (197, 20, 20), (33, 188, 188), (43, 71, 71),
                   (234, 40, 40), (33, 152, 152), (16, 55, 55), (66, 49, 49), (244, 149, 149), (65, 229, 229),
                   (14, 222, 222), (63, 10, 10), (224, 111, 111), (229, 8, 8), (15, 22, 22), (245, 16, 16),
                   (98, 9, 9), (248, 9, 9), (222, 203, 203), (68, 161, 161), (10, 62, 62), (5, 33, 33), (68, 155, 155)]


if __name__ == '__main__':
    print(rgb_color_extraction('hirst_spots.jpg', 30))
