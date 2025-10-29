#EACP1
import random
import turtle as t

t.shape("turtle")
t.shapesize(1000)

colors = ["blue", "red", "black"]
side = random.randint(10,10000)
t.color(random.choice(colors))

t.speed(random.randint(3,5))

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