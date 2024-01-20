import turtle
from turtle import Turtle, Screen
import random
s = Screen()
s.setup(500,400)
user_bet = s.textinput("Make your bet","Which turtle will win the race? Enter a color: ")
print(user_bet)
colors=["red","orange","yellow","green","blue","purple"]
y=[-70,-40,-10,20,50,80]
all_tur=[]
for i in range(0,6):

    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(-230, y[i])
    tim.color(colors[i])
    all_tur.append(tim)

is_race_on=False
if user_bet:
    is_race_on=True

while is_race_on:

    for i in all_tur:
        if i.xcor()>230:
            is_race_on = False

            win=i.pencolor()
            if win==user_bet:
                print(f"You've won!The {win} turtle is the winner!")
            else:
                print(f"You've lost!The {win} turtle is the winner!")

        dist = random.randint(0,10)
        i.forward(dist)

s.exitonclick()