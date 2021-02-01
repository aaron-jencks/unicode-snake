# unicode-snake
A Python Snake implementation on the terminal using unicode characters and ANSI escape sequences

## Gameplay
Use `python main.py` to run the program, then use the WASD keys to control movements, the game ends when you move onto yourself, or outside of the play area (which is the entire console by default). You score for each piece of food that you collect, and the speed of the snake is calculated by `speed=(floor(score / 10) + 1) * 10 fps`.

# Compatibility
This should be compatible for both Windows and Unix systems, but I've only tested it on linux, so if you have any issues, please let me know and I will work them out.
