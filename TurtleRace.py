from turtle import Turtle, Screen
import random

race_is_on = False

screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet", prompt='Which turtle will win?' 'Enter a color: ')
colors = ['red', 'blue', 'green', 'pink', 'orange']
y_positions = [-100, -70, -40, -10, 10]
every_turtle = []

for turtle_index in range(0, 5):
    o = Turtle(shape='turtle')
    o.color(colors[turtle_index])
    o.penup()
    o.goto(x=-230, y=y_positions[turtle_index])
    every_turtle.append(o)

if user_bet:
    race_is_on = True

while race_is_on:

    for turtle in every_turtle:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f" You lost The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 11)
        turtle.forward(rand_distance)


screen.exitonclick()