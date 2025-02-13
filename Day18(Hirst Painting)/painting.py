from turtle import Turtle
from colorgram import extract


colors = extract('hirst_spots.jpg', 20)
rgb_colors = [(color.rgb.r, color.rgb.b, color.rgb.b) for color in colors]

print(rgb_colors)
