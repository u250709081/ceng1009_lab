import turtle
for a in range(100):
    print("We like Python's turtles!")
import turtle
months=["january","february","march","april","may","june","july","august","september","october","november","december"]
for month in months:

    print("One of the months of the year is", month)
numbers=[12, 10, 32, 3, 66, 17, 42, 99, 20]
for n in numbers:
    nsquare=n**2
    print(n,"squared is", nsquare)
import turtle
t=turtle.Turtle()
screen= turtle.Screen()
t.penup()
t.goto(-200,0)
t.pendown()
for i in range(3):
    turtle.fd(100)
    turtle.left(120)
    t.penup()
    t.goto(-100,0)
    t.pendown()
for i in range(4):
        t.fd(100)
        t.left(90)
t.penup()
t.goto(150,0)
t.pendown()
for i in range(6):
    t.fd(100)
    t.left(60)
t.penup()
t.goto(450,0)
t.pendown()
for i in range(8):
    t.fd(100)
    t.left(360/8)
import turtle
screen = turtle.Screen()
screen.bgcolor("light green")
t=turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(3)
t.stamp()

t.penup()
for i in range(12):
    t.fd(125)
    t.pendown()
    t.fd(15)
    t.penup()
    t.fd(25)
    t.stamp()
    t.backward(165)
    t.left(360/12)


screen.exitonclick()







