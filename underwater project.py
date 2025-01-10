##inital
import turtle
jel = turtle.Turtle()
jel.speed(0)
angelo = turtle.Turtle()
char = turtle.Turtle()
angelo.speed(0)
char.speed(0)
##functions

#next 2 coded by jel
def seaweed(size,color,posx,posy):#makes seaweed....
    jel.pensize(1)
    
    jel.color(color)
    jel.pu()
    jel.goto(posx,posy)
    jel.begin_fill()
    jel.pd()
    jel.seth(45)
    jel.circle(size,90)
    for i in range(3):
        jel.right(20)
        jel.circle(size,90)
        jel.left(20)
        jel.circle(size,-90)
    jel.seth(370)
    jel.pu()
    jel.goto(posx,posy)
    jel.pd()
    jel.circle(size*1.5,150)
    jel.end_fill()

    
def sand(size,color,posx,posy): #makes...you guessed it! sand!
    jel.color(color)
    jel.pu()
    jel.goto(posx,posy)
    jel.seth(180)
    jel.pd()
    jel.pensize(size)
    jel.forward(10000)


    
#next 2 coded by angelo
def draw_star(size,color,x,y):
    angelo.color(color)
    angelo.penup()
    angelo.goto(x,y)
    angelo.pendown()
    angelo.begin_fill()
    for i in range(5):
        angelo.forward(size)
        angelo.left(160)
        angelo.forward(size)
        angelo.right(88)
    angelo.end_fill()
def draw_all_star():
    draw_star(45,"red",0,-100)
    draw_star(75,"blue",-200,200)
    draw_star(50,"green",250,100)
    draw_star(25,"orange",-250,-250)
    draw_star(40,"purple",100,-250)



##next 2 coded by charlotte
def drawfish(size,color,x,y):
    char.color(color)
    char.penup()
    char.goto(x,y)
    char.pendown()
    char.dot(size)
    char.begin_fill()
    for i in range(3):
        char.forward(size)
        char.left(120)
    char.end_fill()


def draw_all_fish():
    drawfish(100,"red", 10, 200)
    drawfish(50,"turquoise", 50, 300)
    drawfish(70,"pink", 4, 20)
    drawfish(20,"purple", -50,-100)
    drawfish(29,"orange", 100,-150)
    drawfish(35,"yellow", 200,150)
    
#main
jel.dot(10000,"blue")
sand(500,"tan",1000,-500)
seaweed(50,"green",0,-300)
seaweed(20,"green", 300, -250)
seaweed(20,"green", -350, -300)
seaweed(20,"green", 200, -350)
seaweed(20,"green", -100, -250)
draw_all_star()
draw_all_fish()
