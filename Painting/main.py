# import colorgram
import turtle
import turtle as t
import random

turtle.colormode(255)
russ = t.Turtle()
russ.speed("fastest")
russ.penup()
russ.hideturtle()


color_list = [(225, 237, 230), (239, 213, 106), (22, 108, 190), (117, 92, 56), (237, 137, 68), (222, 54, 81), (112, 99, 196), (247, 117, 150), (68, 126, 108), (143, 171, 186), (216, 8, 28), (146, 178, 4), (193, 47, 92), (30, 191, 104), (240, 41, 32), (30, 54, 122), (107, 169, 133)]

russ.setheading(225)
russ.forward(300)
russ.setheading(0)
no_dots = 100

for dot_count in range(1, no_dots + 1):
    russ.dot(20,random.choice(color_list))

    russ.forward(50)

    if dot_count % 10 == 0:
        russ.left(90)
        russ.forward(50)
        russ.setheading(180)
        russ.forward(500)
        russ.setheading(0)


screen = t.Screen()
screen.exitonclick()