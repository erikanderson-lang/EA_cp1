
import turtle as t

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
t.shapesize(1000)

colors = ["blue", "red", "black"]
side = random.randint(10,10000)
t.color(random.choice(colors))

t.speed(random.randint(3,5))

t.fillcolor(random.choice(colors))
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
