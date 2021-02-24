import random
from turtle import Turtle, Screen


is_race_on=False

screen= Screen()
screen.setup(width=500,height=400)
colors=["red", "orange", "blue", "black", "yellow", "green"]
y_positions= [0, 50, -50, 100, -100, 150]

all_turtles=[]

for turtle_index in range(0,6):
    new_turtle= Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)

bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a color: ")

if bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

        if turtle.xcor()>223:
            is_race_on=False
            winning_color= turtle.pencolor()
            if winning_color==bet:
                print(f"You won! {winning_color} turtle won the race!")
                
            else:
                print(f"You lose. {winning_color} turtle won the race.")
               



    

screen.exitonclick()