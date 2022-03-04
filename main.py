import turtle
from turtle import Turtle,Screen





tim=Turtle()
screen=Screen()




def right():
    a=tim.heading()-10
    tim.setheading(a)


screen.onkey(right, "d")
screen.listen()


def left():
    a=tim.heading()+10
    tim.setheading(a)


screen.onkey(left, "a")
screen.listen()


def Down():

    tim.backward(50)

screen.onkey(fun=Down, key="s")

def Up():

    tim.fd(50)

screen.onkey(Up, "w")



def clear():
    turtle.resetscreen()

screen.onkey(clear,"c")



screen.listen()







screen.exitonclick()