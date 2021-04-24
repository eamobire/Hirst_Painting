import colorgram
import turtle
import random

# colors = colorgram.extract('hirst_image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

extracted_colors = [(246, 245, 243), (232, 238, 246),
                    (247, 238, 242), (239, 246, 243),
                    (131, 166, 205), (222, 148, 106),
                    (31, 42, 61), (199, 134, 147),
                    (165, 59, 48), (140, 184, 162),
                    (39, 105, 157), (238, 212, 89),
                    (152, 58, 66), (217, 81, 70),
                    (169, 29, 33), (236, 165, 156),
                    (50, 112, 90), (35, 61, 55), (17, 97, 71),
                    (156, 33, 30), (231, 160, 165), (53, 44, 49),
                    (170, 188, 221), (57, 51, 48), (189, 100, 110),
                    (31, 60, 109), (103, 127, 161), (34, 151, 209),
                    (174, 200, 188), (65, 66, 56)]

tim = turtle.Turtle()
colors = turtle.colormode(255)

tim.speed("fast")
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(extracted_colors))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.setheading(180)
        tim.penup()
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()
tim.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
