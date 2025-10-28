import time
import turtle as t
import random
#EACP1


#What is a library?
#a built in thing 

#What libraries have we used?
#time , random

#What are some common python libraries?
#nunmpy pygame matplotlib beautiful soup

#How do you call built-in functions?
#doing it

#What are some common functions that we have used
#rand.randint time.sleep


t.shape("turtle")
t.shapesize(0.0000001)

colors = ["blue", "red", "black"]
side = random.randint(10,10000)
t.color(random.choice(colors))

t.fillcolor(random.choice(colors))
t.begin_fill()
for x in range(1,4):
    t.forward(side)
    t.right(90)
t.end_fill()

t.penup()
t.goto(0,300)
t.pendown()

t.color("blue")
t.fillcolor("red")
t.begin_fill()
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.end_fill()

t.done()


t.shape("turtle")