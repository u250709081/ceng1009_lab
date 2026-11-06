# def getGrade(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
# marks=[90,80,70,60,50]
# for mark in marks:
#     print("your grade is ", getGrade(mark))
# mark= float(input("enter your mark: "))
# print(getGrade(mark))
# import turtle
# def choosecolor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(gap+height)
#     t.write(" "+str(height))
#     t.backward(gap+height)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(choosecolor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     max_height= max(data)
#     num_bars= len(data)
#     border=10
#     gap=(max_height-border)/25
#     wn=turtle.Screen()
#     wn.bgcolor("black")
#     right=40*num_bars+border
#     top=max_height+4*border
#     wn.setworldcoordinates(-border,-border,right,top)
#     t.pensize(2)
#     for height in data:
#          drawBar(t,height,gap)
#     wn.exitonclick()
# data=[48,64,100,150,978,399,234]
# t=turtle.Turtle()
# t.color("white")
# t.pensize(2)
# for height in data:
#     drawBar(t,height,gap)
# wn.exitonclick()
#
# data=[48,64,100,150,978,399,234]
# print(barChart(data))
# import turtle
# def choosecolor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(gap+height)
#     t.write(" "+str(height))
#     t.backward(gap+height)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(choosecolor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     max_height= max(data)
#     num_bars= len(data)
#     border=10
#     gap=(max_height-border)/25
#     wn=turtle.Screen()
#     wn.bgcolor("black")
#     right=40*num_bars+border
#     top=max_height+4*border
#     wn.setworldcoordinates(-border,-border,right,top)
#     t.pensize(2)
#     for height in data:
#          drawBar(t,height,gap)
#     wn.exitonclick()
# data=[48,64,100,150,978,399,234]
# t=turtle.Turtle()
# t.color("white")
# t.pensize(2)
# print(barChart(data))
# import math
# def findHypot(a,b):
#     hypot= (a**2+b**2)**0.5
#     return hypot
# def calcWithMath(a,b):
#     hypot= math.sqrt(a**2+b**2)
#     return hypot
# print(calcWithMath(3,4))
# print(findHypot(3,4))