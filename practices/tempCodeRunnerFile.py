el.right(90)
el.forward(100)
el.right(90)


rock = 0
while True:
        if rock == 6:
                break
        if gridcol[5][rock] == 1:
                el.pendown()
                el.forward(100)
                

        if gridcol[5][rock] == 0:
               el.penup()
               el.forward(100)
               
        rock +=1
el.hideturtle()