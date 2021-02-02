# unicode-snake
A Python Snake implementation using pygame, you can also play a terminal vertion.

## Gameplay
Use `python main.py` to run the pygame program, then use the WASD keys to control movements, the game ends when you move onto yourself, or outside of the play area (which is the entire console by default). You score for each piece of food that you collect, and the speed of the snake is calculated by `speed=(floor(score / 10) + 1) * 10 fps`.

To run the terminal version, use `python game.py` all other interaction remains the same.

# Compatibility
This should be compatible for both Windows and Unix systems, but I've only tested it on linux, so if you have any issues, please let me know and I will work them out.
