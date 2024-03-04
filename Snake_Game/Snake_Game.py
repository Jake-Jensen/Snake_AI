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

# We can use the snake size as a cell size too, so build the play grid array
PlayGrid = [(Width / SNAKE_SIZE), (Height / SNAKE_SIZE)]



# --- Game Logic Functions ---
def move_snake():
   # (Implementation to move the snake based on its direction)
   global direction  # Assuming direction is a global variable

   if window.event_generate(MOVE_LEFT):
       direction = "left"
   elif window.event_generate(MOVE_RIGHT):
       direction = "right"
   elif window.event_generate(MOVE_UP):
       direction = "up"
   elif window.event_generate(MOVE_DOWN):
       direction = "down"

def create_food():
   # (Implementation to place food at a random position)

def check_collisions():
   # (Implementation to detect collisions with food, walls, or itself)

# --- Create the Window --- 
window = tk.Tk()
window.title("Snake Game")

# --- Create the Canvas ---
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# --- Initialize Snake (example: starting as a simple line) ---
snake = [
    canvas.create_rectangle(SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE*2, SNAKE_SIZE*2, fill="green")
]

# --- Main Game Loop ---
def game_loop():
    window.bind(MOVE_LEFT, move_snake)  # Call move_snake on MoveLeft event
    window.bind(MOVE_RIGHT, move_snake)  # ... and so on for other directions
    move_snake()
    check_collisions()
    window.after(DELAY, game_loop)  # Schedule the next game update

# --- Start the Game ---
create_food()
game_loop()
window.mainloop()
