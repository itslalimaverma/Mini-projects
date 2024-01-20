from turtle import Turtle,Screen

timmy=Turtle()
s=Screen()

# to control our turtle

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    new=timmy.heading()+10
    timmy.setheading(new)

def turn_right():
    new=timmy.heading()-10
    timmy.setheading(new)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

s.listen()
s.onkey(key="w", fun=move_forwards)
s.onkey(key="s", fun=move_backwards)
s.onkey(key="a", fun=turn_left)
s.onkey(key="d", fun=turn_right)
s.onkey(key="c", fun=clear)


s.exitonclick()