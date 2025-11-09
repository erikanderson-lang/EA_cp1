import turtle as t
import random

e = t.Screen()
e.setup(1200, 700)
t.bgcolor("black")
m = t.Turtle()
m.speed("fastest")
m.shape("square")
m.pencolor("red")
m.hideturtle()

el = t.Turtle()
el.shape("circle")
el.speed("fastest")
el.pencolor("blue")
el.hideturtle()

CELL_SIZE = 100
ROWS = 5
COLS = 6
MAZE_START_X = -300
MAZE_START_Y = 300

def generate_maze_data():
    """Generates random wall data."""
    gridrow = [[random.randint(0, 1) for _ in range(COLS)] for _ in range(ROWS)]
    gridcol = [[random.randint(0, 1) for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
    return gridrow, gridcol

def solve_maze(gridrow, gridcol):
    """Checks if the maze is solvable using Breadth-First Search (BFS) with a list as a queue."""
    start_pos = (0, 0) # Top-left cell
    end_pos = (ROWS - 1, COLS - 1) # Bottom-right cell
    
    # Use a standard list as a queue (append for enqueue, pop(0) for dequeue)
    queue = [start_pos] 
    visited = set([start_pos])

    while queue:
        r, c = queue.pop(0) # Dequeue the first element

        if (r, c) == end_pos:
            return True # Solvable

        # Define potential movements: Right, Left, Down, Up
        # Check adjacent cell bounds and walls
        
        # Move Right (check gridcol[r][c+1])
        if c + 1 < COLS and gridcol[r][c+1] == 0 and (r, c + 1) not in visited:
            visited.add((r, c + 1))
            queue.append((r, c + 1))
            
        # Move Left (check gridcol[r][c])
        if c - 1 >= 0 and gridcol[r][c] == 0 and (r, c - 1) not in visited:
            visited.add((r, c - 1))
            queue.append((r, c - 1))

        # Move Down (check gridrow[r][c])
        if r + 1 < ROWS and gridrow[r][c] == 0 and (r + 1, c) not in visited:
            visited.add((r + 1, c))
            queue.append((r + 1, c))

        # Move Up (check gridrow[r-1][c])
        if r - 1 >= 0 and gridrow[r-1][c] == 0 and (r - 1, c) not in visited:
            visited.add((r - 1, c))
            queue.append((r - 1, c))

    return False # Not solvable

def draw_maze(gridrow, gridcol):
    """Draws the solvable maze using turtle graphics."""
    # Clear previous drawings if any
    m.clear()
    el.clear()

    # Draw outline
    m.penup()
    m.goto(MAZE_START_X, MAZE_START_Y)
    m.pendown()
    for _ in range(2):
        m.forward(COLS * CELL_SIZE)
        m.left(90)
        m.forward(ROWS * CELL_SIZE)
        m.left(90)
    m.penup()

    # Draw horizontal walls (gridrow)
    for r in range(ROWS):
        el.penup()
        el.goto(MAZE_START_X, MAZE_START_Y - (r + 1) * CELL_SIZE)
        el.pendown()
        for c in range(COLS):
            if gridrow[r][c] == 1:
                el.pendown()
            else:
                el.penup()
            el.forward(CELL_SIZE)
        
    # Draw vertical walls (gridcol)
    for c in range(COLS + 1):
        el.penup()
        el.goto(MAZE_START_X + c * CELL_SIZE, MAZE_START_Y)
        el.pendown()
        el.right(90) # Face down
        for r in range(ROWS):
            if gridcol[r][c] == 1:
                el.pendown()
            else:
                el.penup()
            el.forward(CELL_SIZE)
        el.left(90) # Face right again


# --- Main Logic ---

while True:
    print("Generating new maze data...")
    # Generate data
    gridrow_data, gridcol_data = generate_maze_data()
    
    # Check if solvable
    if solve_maze(gridrow_data, gridcol_data):
        print("Maze is solvable! Drawing now.")
        draw_maze(gridrow_data, gridcol_data)
        break # Exit the loop once a solvable maze is drawn
    else:
        print("Maze not solvable, regenerating...")
        # Loop continues to generate a new one

t.done()
