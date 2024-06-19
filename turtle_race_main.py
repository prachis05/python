from turtle import Turtle,Screen
import random

is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle win the race? Enter the color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_turtle = turtle.pencolor()
                if winning_turtle == user_bet:
                    print(f"You've  won! The {winning_turtle} turtle is the winner ")
                else:
                    print(f"You've lost ! The {winning_turtle} turtle is the winner")

            random_no = random.randint(0, 10)
            turtle.forward(random_no)


screen.exitonclick()
