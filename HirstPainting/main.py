# import colorgram

# colors = colorgram.extract('image.jpg', 30)

# print(len(colors)) # 10
# print(colors[0]) # <colorgram.py Color: Rgb(r=236, g=235, b=240), 69.17169292813932%>
# print(colors[0].rgb) # Rgb(r=236, g=235, b=240)
# print(colors[0].rgb[0]) # 236

# rgb_colors = []

# for color in colors:
#     rgb_tup = (color.rgb[0], color.rgb[1], color.rgb[2])
#     rgb_colors.append(rgb_tup)

# print(rgb_colors)
# print(len(rgb_colors))

# Requirements: 10 x 10 dots; dot size = 20; spacing = 50

from turtle import Turtle, Screen

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (126, 40, 61), (21, 86, 61), (59, 48, 37),
        (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134),
        (197, 125, 150), (156, 191, 185), (30, 67, 58), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111),
        (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205), (223, 178, 169)]






screen = Screen()
screen.exitonclick()
