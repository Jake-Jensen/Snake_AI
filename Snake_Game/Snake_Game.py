import tkinter as tk
import random

# --- Game Constants ---
WIDTH = 400
HEIGHT = 300
SNAKE_SIZE = 20  # Size of each snake segment
DELAY = 100      # Game update speed (milliseconds)
MOVE_LEFT = "<MoveLeft>"
MOVE_RIGHT = "<MoveRight>"
MOVE_UP = "<MoveUp>"
MOVE_DOWN = "<MoveDown>"
SnakeHeadLocation = [0,0]
FoodCoordinate = [0,0]
SnakeBodyLocationArray = []

# We can use the snake size as a cell size too, so build the play grid array
PlayGrid = [(WIDTH / SNAKE_SIZE), (HEIGHT / SNAKE_SIZE)]
direction = "up"

def handle_key_press(event):
    if event.char == 'q':
        root.quit()  # Quit on 'q' press

# --- Game Logic Functions ---
def move_snake():
    # As the playgrid is a static object, populate and check all at once

    # TODO
    # HANDLE SNAKE HEAD DIRECTION CHANGE

    # The snake moves before colliding, to make it easier to test if the head is out of bounds
    if (SnakeHeadLocation[0] < 0 or
    SnakeHeadLocation[0] > PlayGrid[0] or
    SnakeHeadLocation[1] < PlayGrid[1] or
    SnakeHeadLocation[1] > PlayGrid[1]):
        # Snake head is out of bounds, go to game over.
        print("End of snake head reached")

def create_food():
   # (Implementation to place food at a random position)
   print("Create food called")

def check_collisions():
   # (Implementation to detect collisions with food, walls, or itself)
   print("Check collisions called")

# --- Main Game Loop ---
def game_loop():
    #window.bind(MOVE_LEFT, move_snake)  # Call move_snake on MoveLeft event
    #window.bind(MOVE_RIGHT, move_snake)  # ... and so on for other directions
    move_snake()
    check_collisions()
    window.after(DELAY, game_loop)  # Schedule the next game update

# --- Start the Game ---
# --- Create the Window --- 
window = tk.Tk()
window.title("Snake Game")
window.bind("<Key>", handle_key_press)

# --- Create the Canvas ---
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# --- Initialize Snake (example: starting as a simple line) ---
snake = [
    canvas.create_rectangle(SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE*2, SNAKE_SIZE*2, fill="green")
]

create_food()
game_loop()
window.mainloop()
