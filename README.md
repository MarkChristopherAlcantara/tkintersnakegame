# Tkinter Snake Game

This code is a classic Snake Game implementation using Python's Tkinter library for the graphical interface. The game window is **600x400 pixels**, and the snake moves in a grid where each cell is **20x20 pixels**. The game's main features include:

## Features

### Initialization
- The game starts with a single-segment snake positioned in the middle of the screen, moving to the right.
- The score is set to **zero**, and the game is in a running state.

### Movement
- The snake moves in the direction specified by the `direction` variable.
- The snake's head moves **one cell at a time**.
- If the snake eats the food, it grows longer.
- If the snake collides with itself, the game is over.

### Food Placement
- Food appears at random locations on the grid that do **not** overlap with the snake's body.
- When the snake eats the food, the **score increases**, and new food is placed.

### Drawing
- The game continuously **redraws** the snake, food, and score on the canvas.
- The snake is drawn as **green rectangles**.
- The food is drawn as **red rectangles**.
- The score is displayed in **white text**.

### Direction Change
- The direction of the snake can be changed using the **arrow keys**.
- The game prevents the snake from moving in the **opposite direction immediately** (to avoid self-collision).

### Game Over and Restart
- When the game is over, a **"Game Over"** text is displayed.
- A **Restart** option appears, allowing the player to reset the game.
- Clicking "Restart" resets the game to its **initial state**.

### Blinking Text
- The restart text **blinks** to draw attention.
- This blinking behavior is controlled by the `blink_restart_text` function.

## Screenshots
![Snake Game Screenshot](https://github.com/user-attachments/assets/6b3fcb72-c762-4d6f-9644-39d5b1dcf619)

The code uses the `tk.Canvas` widget to handle all drawing operations, and the `root.after()` method to create a **game loop** that updates the snake's movement and game state at regular intervals. The game logic is contained within several functions that handle:
- Movement
- Drawing
- Food placement
- Direction changes
- Restarting the game

![Game Over Screen](https://github.com/user-attachments/assets/add5a161-261b-4260-8178-2668240adf50)
