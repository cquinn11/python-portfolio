#init
import turtle
import random
char=turtle.Turtle()

#allows us to represent colors as RGB triplets
turtle.colormode(255)

#functions

def randomdots():
    for i in range(1000):
        char.dot(random.randint(10,500),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        char.pu()
        char.goto(random.randint(-400,400),random.randint(-400,400))
        char.pd()





        char.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        char.begin_fill()
        char.forward(random.randint(10,500))
        char.left(90)
        char.forward(random.randint(10,500))
        char.left(90)
        char.forward(random.randint(10,500))
        char.left(90)
        char.forward(random.randint(10,500))
        char.left(90)
        char.end_fill()
#main
randomdots()
         

    
