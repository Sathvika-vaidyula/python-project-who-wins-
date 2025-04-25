import random
from turtle import Turtle, Screen

# Set up screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color:')

# Initialize race data
colors = ['green', 'blue', 'yellow', 'pink', 'black']
y_positions = [-60, 100, 50, -100, -150]
turtles = []

# Create turtles and place them at the starting line
for color, y in zip(colors, y_positions):
    t = Turtle(shape='turtle')
    t.penup()
    t.color(color)
    t.goto(x=-230, y=y)
    turtles.append(t)

# Start the race if user has entered a bet
is_race_on = False
if user_bet:
    is_race_on = True

# Race loop
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            print(f"The winner is {winning_color}!")
            if winning_color == user_bet:
                print("You win! 🎉")
            else:
                print("You lose. 😢")
            is_race_on = False
            break  # Stop checking other turtles

        # Move turtle forward randomly
        distance = random.randint(0, 10)
        turtle.forward(distance)

# Keep window open after race ends
screen.exitonclick()
