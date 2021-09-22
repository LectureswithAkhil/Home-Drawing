def star(x,y):
    t.goto(x,y)
    t.begin_fill()
    for i in range(5):
        t.forward(15)
        t.rt(144)      
    t.fillcolor("white")
    t.end_fill()
def tree(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.pensize(3)
    t.pencolor("orange")
    t.setheading(90)
    t.forward(100)
    for i in range(5):
        t.setheading(180)
        t.lt(-144)
        t.forward(10)
        t.rt(144)
    t.up()
    t.goto(x,y)
    t.setheading(90)
    t.forward(100)
    t.down()
    for i in range(5):
        t.setheading(180)
        t.rt(-144)
        t.forward(10)
        t.lt(144)
    t.up()
    t.goto(x,y)
    t.setheading(90)
    t.forward(100)
    t.down()
    for i in range(5):
        t.setheading(180)
        t.rt(-144)
        t.backward(10)
        t.lt(144)
    t.up()
    t.goto(x,y)
    t.setheading(90)
    t.forward(100)
    t.down()
    for i in range(5):
        t.setheading(180)
        t.lt(-144)
        t.backward(10)
        t.rt(144)
def door():
    t.up()
    t.begin_fill()
    t.goto(0,-100)
    t.down()
    t.setheading(90)
    t.forward(100)
    t.lt(-210)
    t.forward(30)
    t.setheading(270)
    t.forward(50)
    t.lt(30)
    t.forward(30)
    t.fillcolor("grey")
    t.end_fill()
import turtle
t=turtle.Turtle()
t.speed(1000)
w=turtle.Screen()
w.bgcolor("black")
w.title("My Sweet Home")
t.begin_fill()
t.goto(-50,0)
for i in range(3):
    t.forward(100)
    t.lt(120)
t.fillcolor("blue")
t.end_fill()
t.begin_fill()
t.setheading(270)
for i in range(4):
    t.forward(100)
    t.lt(90)
t.fillcolor("red")
t.end_fill()
t.up()
t.goto(250,250)
t.begin_fill()
t.circle(50)
t.down()
t.fillcolor("white")
t.end_fill()
t.goto(0,250)
t.up()
door()
t.up()
x=0
y=200
for i in range(5):
    star(x,y)
    star(-x+100,y-10)
    star(-x,y)
    x=x+10
    y=y+120

x=0
y=0
for i in range(10):
    star(x-500,y+200)
    x=x+10
    y=y+120

for i in range(5):
    t.forward(100)
    t.left(150)
    t.forward(100)
t.up()
t.goto(-50,-170)
t.down()
t.pensize(8)
t.pencolor("white")
for i in range(5):
    t.forward(100)
    t.lt(144)
t.ht()
x=200
y=-80
for i in range(4):
    tree(x,y)
    tree(-x,y)
    x=x+100













    



    










    



    


