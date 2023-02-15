from turtle import Turtle, Screen
from turtles_data import turtle_data as data
import random

#Initial settings for the screen
screen = Screen()
screen.setup(width=500, height=400)

#Ask to the user to bet on the race
user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")

all_turtles = []
for turtles_settings in data:
    #Creating turtles instances
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(turtles_settings["color"])
    new_turtle.goto(x=-230, y=turtles_settings["cordinates_y"])
    all_turtles.append(new_turtle)

race_is_on = False

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        #Creating a random distance
        random_distance = random.randint(0, 10)
        turtle.pendown()
        turtle.pensize(3)
        turtle.forward(random_distance)
        
        # Proclaim the winner when he reaches these coordinates
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            #Checking the user bet
            if user_bet == winning_color:
                print(f"The {winning_color} turtle arrived first. You win!")
            else:
                print(f"You picked the wrong turtle, you lose. The winning turtle is the {winning_color} one.")

screen.exitonclick()