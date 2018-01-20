# P1JPG.py
import turtle
t = turtle.Pen()
turtle.bgcolor('gray')
t.speed(0)

#Ask user for # circles

nCirc = int(turtle.numinput("Number of circles", "Please enter the nmber of circles wanted in the rosette", 6))
wCirc = str(turtle.textinput("Width", "Do you want the rosette to have Strong or Thin lines?"))

if wCirc.title() == ("Strong"):
    t.width(3)
else:
    t.width(0)

for x in range(nCirc):
    t.pencolor('blue')
    t.circle(30)
    t.pencolor('green')
    t.circle(60)
    t.pencolor('red')
    t.circle(120)
    t.left(360/nCirc)

