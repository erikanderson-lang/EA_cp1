#EACP1
import turtle as t
import random
e = t.Screen()
e.setup(3000,1300)
t.bgcolor("black")
m = t.Turtle()
m.speed("fastest")
m.shape("square")
m.pencolor("red")
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
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]]

gridcol = [
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],
        [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]]

#new toitle
el = t.Turtle()
el.shape("circle")
el.speed("fastest")
el.pencolor("blue")
el.teleport(0,500)
# checks if there is a wall and prints if there is


rock = 0
while True:
        if rock == 6:
                break
        if gridrow[0][rock] == 1:
                el.pendown()
                el.forward(100)
                

        if gridrow[0][rock] == 0:
               el.penup()
               el.forward(100)
               
        rock +=1
el.right(90)
el.forward(100)
el.right(90)


rock = 0
while True:
        if rock == 6:
                break
        if gridrow[1][rock] == 1:
                el.pendown()
                el.forward(100)
                

        if gridrow[1][rock] == 0:
               el.penup()
               el.forward(100)
               
        rock +=1
el.left(90)
el.forward(100)
el.left(90)

rock = 0
while True:
        if rock == 6:
                break
        if gridrow[2][rock] == 1:
                el.pendown()
                el.forward(100)
                

        if gridrow[2][rock] == 0:
               el.penup()
               el.forward(100)
               
        rock +=1
el.right(90)
el.forward(100)
el.right(90)


rock = 0
while True:
        if rock == 6:
                break
        if gridrow[3][rock] == 1:
                el.pendown()
                el.forward(100)
                

        if gridrow[3][rock] == 0:
               el.penup()
               el.forward(100)
               
        rock +=1
el.left(90)
el.forward(100)
el.left(90)

rock = 0
while True:
        if rock == 6:
                break
        if gridrow[4][rock] == 1:
                el.pendown()
                el.forward(100)
                

        if gridrow[4][rock] == 0:
               el.penup()
               el.forward(100)
               
        rock +=1
el.right(90)
el.forward(100)
el.right(90)

el.teleport(100,600)
el.right(260)
rock = 0
while True:
        if rock == 6:
                break
        if gridcol[4][rock] == 1:
                el.pendown()
                el.forward(100)
                

        if gridcol[4][rock] == 0:
               el.penup()
               el.forward(100)
               
        rock +=1
el.right(90)
el.forward(100)
el.right(90)







#checks to see if it is solvable

t.done()





















