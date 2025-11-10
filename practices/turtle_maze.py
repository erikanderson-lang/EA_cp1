#EACP1
import turtle as t
import random
import time

print("""When the maze generates you might need to scroll up in order to see
part of the maze I am waiting to print the maze until you have read this.(There is a scoll bar on the side. Use that.)
Wait.""")
time.sleep(1)
# Setup backgrownd
e = t.Screen()
e.setup(1300, 900)
t.screensize(1000,2000)
t.bgcolor("black")


def generate_random_maze():
    """Generate completely random maze grids"""
    gridrow = [[random.randint(0,1) for _ in range(6)] for _ in range(5)]
    gridcol = [[random.randint(0,1) for _ in range(6)] for _ in range(6)]
    return gridrow, gridcol

def is_maze_solvable(gridrow, gridcol):
    """Check if maze has a path from top-left (0,0) to bottom-right (5,5)"""
    #find if path exists
    from collections import deque
    
    visited = set()
    queue = deque([(0, 0)])  # Start at top-left
    visited.add((0, 0))
    
    while queue:
        row, col = queue.popleft()
        
        # Check if reached the goal (bottom-right)
        if row == 5 and col == 5:
            return True
        
        # Try moving right (check if no wall blocks)
        if col < 5 and (row, col + 1) not in visited:
            # Check if there's a vertical wall between col and col+1
            if gridcol[col + 1][row] == 0:  # 0 means no wall
                visited.add((row, col + 1))
                queue.append((row, col + 1))
        
        
        if row < 5 and (row + 1, col) not in visited:
            # Check if there's a horizontal wall between row and row+1
            if gridrow[row][col] == 0:  # 0 means no wall
                visited.add((row + 1, col))
                queue.append((row + 1, col))
        
        
        if col > 0 and (row, col - 1) not in visited:
            if gridcol[col][row] == 0:
                visited.add((row, col - 1))
                queue.append((row, col - 1))
        
        
        if row > 0 and (row - 1, col) not in visited:
            if gridrow[row - 1][col] == 0:
                visited.add((row - 1, col))
                queue.append((row - 1, col))
    
    return False

# Generate mazes until a solvable one
attempts = 0
while True:
    attempts += 1
    gridrow, gridcol = generate_random_maze()
    if is_maze_solvable(gridrow, gridcol):
        print("")
        break

m = t.Turtle()
m.shape("square")
m.pencolor("red")
# Makes maze outline
m.forward(550)
m.penup()
m.forward(50)
m.left(90)
m.pendown()
m.forward(600)
m.left(90)
m.forward(550)
m.penup()
m.forward(50)
m.pendown()
m.left(90)
m.forward(600)
m.hideturtle()

# Draws rows
el = t.Turtle()
el.shape("circle")
el.speed("fastest")
el.pencolor("blue")

for row_idx in range(5):
    el.penup()
    el.goto(0, 600 - (row_idx + 1) * 100)
    for col_idx in range(6):
        if gridrow[row_idx][col_idx] == 1:
            el.pendown()
        else:
            el.penup()
        el.forward(100)

# Draw vertical walls (columns)
for col_idx in range(1, 6):
    el.penup()
    el.goto(col_idx * 100, 600)
    el.setheading(270)
    for row_idx in range(6):
        if gridcol[col_idx][row_idx] == 1:
            el.pendown()
        else:
            el.penup()
        el.forward(100)

el.hideturtle()



t.update()
t.done()