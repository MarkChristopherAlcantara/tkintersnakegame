import tkinter as tk
import random

# Game Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
SPEED = 100
BLINK_SPEED = 500

directions = {'Up': (0, -1), 'Down': (0, 1), 'Left': (-1, 0), 'Right': (1, 0)}

def move():
    global snake, direction, food, score, running
    if not running:
        return
    
    head_x, head_y = snake[0]
    dx, dy = directions[direction]
    new_head = (head_x + dx * CELL_SIZE, head_y + dy * CELL_SIZE)
    
    # Portal behavior (wrap around through opposite wall)
    new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)
    
    if new_head in snake:
        canvas.create_text(WIDTH//2, HEIGHT//2 - 20, text="Game Over", font=("Arial", 24), fill="red")
        running = False
        show_restart_text()
        return
    
    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        place_food()
    else:
        snake.pop()
    
    draw()
    root.after(SPEED, move)

def draw():
    canvas.delete("all")
    for segment in snake:
        canvas.create_rectangle(*segment, segment[0] + CELL_SIZE, segment[1] + CELL_SIZE, fill="green")
    canvas.create_rectangle(*food, food[0] + CELL_SIZE, food[1] + CELL_SIZE, fill="red")
    canvas.create_text(50, 20, text=f"Score: {score}", font=("Arial", 14, "bold"), fill="white", tags="score_text")

def place_food():
    global food
    while True:
        new_food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        if new_food not in snake:
            food = new_food
            break

def change_direction(event):
    global direction
    if event.keysym in directions and (directions[event.keysym][0] * -1, directions[event.keysym][1] * -1) != directions[direction]:
        direction = event.keysym

def restart():
    global snake, direction, food, score, running
    snake = [(WIDTH//2, HEIGHT//2)]
    direction = 'Right'
    score = 0
    running = True
    canvas.delete("restart_text")
    place_food()
    move()

def show_restart_text():
    global restart_text
    restart_text = canvas.create_text(WIDTH//2, HEIGHT//2 + 20, text="Restart", font=("Arial", 20, "bold"), fill="white", tags="restart_text")
    blink_restart_text()
    canvas.tag_bind(restart_text, "<Button-1>", lambda event: restart())

def blink_restart_text():
    if running:
        return
    current_color = canvas.itemcget(restart_text, "fill")
    new_color = "red" if current_color == "white" else "white"
    canvas.itemconfig(restart_text, fill=new_color)
    root.after(BLINK_SPEED, blink_restart_text)

root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = [(WIDTH//2, HEIGHT//2)]
direction = 'Right'
score = 0
running = True
place_food()

root.bind("<Key>", change_direction)
move()
root.mainloop()
