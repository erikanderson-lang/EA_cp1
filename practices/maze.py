#EACP1
import turtle as t
import random

m = t.Turtle()
m.speed(1234567890)
m.shape("square")
#makes maze outline
m.penup()
m.forward(50)
m.pendown()
m.forward(550)
m.left(90)
m.forward(600)
m.left(90)
m.penup()
m.forward(50)
m.pendown()
m.forward(550)
m.pendown()
m.left(90)
m.forward(600)
m.hideturtle()
#makes the inside walls yes or no colloms and rows
#hail
gridrow = [
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]]

gridcol = [
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]]

#new toitle
el = t.Turtle()
el.shape("circle")
el.speed(1234567890)

def isgood():
        pass
# checks if there is a wall and prints if there is
rock = 1
while rock < 6:
        if gridrow == 1:
                el.pendown()
                el.forward(100)
                rock += 1

        elif gridrow == 0:
               el.penup()
               el.forward(100)
               rock += 1








#checks to see if it is solvable

t.done()





















