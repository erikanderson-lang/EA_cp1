#EACP1
import turtle as t
import random
#is all the different turtles
tu1 = t.Turtle()
tu2 = t.Turtle()
tu3 = t.Turtle()
tu4 = t.Turtle()
tu5 = t.Turtle()
#gives the turtles colour
tu1.color("blue")
tu1.shape("turtle")
tu2.color("red")
tu2.shape("turtle")
tu3.color("black")
tu3.shape("turtle")
tu4.color("gold")
tu4.shape("turtle")
tu5.color("silver")
tu5.shape("turtle")

tu1.shapesize(3)
tu1.hideturtle()
tu1.penup()
tu1.goto(0,400)
tu1.back(400)
tu1.pendown()
tu1.showturtle()

tu2.shapesize(3)
tu2.hideturtle()
tu2.penup()
tu2.goto(0,200)
tu2.back(400)
tu2.pendown()
tu2.showturtle()

tu3.shapesize(3)
tu3.hideturtle()
tu3.penup()
tu3.goto(0,0)
tu3.back(400)
tu3.pendown()
tu3.showturtle()

tu4.shapesize(3)
tu4.hideturtle()
tu4.penup()
tu4.goto(0,-200)
tu4.back(400)
tu4.pendown()
tu4.showturtle()

tu5.shapesize(3)
tu5.hideturtle()
tu5.penup()
tu5.goto(0,-400)
tu5.back(400)
tu5.pendown()
tu5.showturtle()

end = t.Turtle()

end.hideturtle()
end.penup()
end.goto(500,500)
end.pendown()
end.sety(-500)
end.showturtle()

rock = random.randint(100,200)

for num in range(rock):
    tu1.forward(random.randint(100,200))
    tu2.forward(random.randint(100,200))
    tu3.forward(random.randint(100,200))
    tu4.forward(random.randint(100,200))
    tu5.forward(random.randint(100,200))
    x1 = tu1.xcor()
    if x1 >= 400:
        print("blue Won!")
    elif tu2.pos(500,0):
        print("Red")
    elif tu3.pos(500,0):
        print("Black")
    elif tu4.pos(500,0):
        print("Gold")
    elif tu5.pos(500,0):
        print("Silver")


t.done()