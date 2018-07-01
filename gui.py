from random import randint
import time
from Snake import Snake
import tkinter as tk

# Command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-vh", "--height", type=int, default=20,
                    help="sets field height")
parser.add_argument("-vw", "--width", type=int, default=20,
                    help="sets field width")
parser.add_argument("-s", "--scale", type=int, default=30,
                    help="sets display scale")
parser.add_argument("-u", "--user", type=bool, default=False,
                    help="toggles user input or random input")
args = parser.parse_args()
HEIGHT = args.height
WIDTH = args.width
SCL = args.scale
USER = args.user

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

OPPOSITE_DIRECTION = {LEFT: RIGHT, UP: DOWN,
                      RIGHT: LEFT, DOWN: UP}

# Initializing tkinter window
window = tk.Tk()
window.title("Snake Game")

class Display:

    def __init__(self, window):
        self.window = window
        self.w = tk.Canvas(window, width=WIDTH*SCL, height=HEIGHT*SCL)
        self.w.pack()
        self.s = Snake(HEIGHT, WIDTH)
        self.s.new_game()

        if USER:
            self.direction = None
            self.old_direction = RIGHT
            self.window.bind('<KeyPress>', self.keydown)

        self.render()

    def render(self):
        # Draw the background
        self.w.create_rectangle(0, 0,
                                WIDTH*SCL, HEIGHT*SCL,
                                fill="gray", outline="")
        # Draw the food
        fx = self.s.food['x']
        fy = self.s.food['y']
        self.w.create_rectangle(fx*SCL, fy*SCL,
                                (fx + 1)*SCL, (fy + 1)*SCL,
                                fill="green2", outline="")

        # Draw the body
        for segment in self.s.snake[1:]:
            x = segment['x']
            y = segment['y']
            self.w.create_rectangle(x*SCL, y*SCL,
                                    (x + 1)*SCL, (y + 1)*SCL,
                                    fill="white", outline="")
        # Draw the head in a different color
        x = self.s.snake[0]['x']
        y = self.s.snake[0]['y']
        self.w.create_rectangle(x*SCL, y*SCL,
                                (x + 1)*SCL, (y + 1)*SCL,
                                fill="indian red", outline="")

        # Move, reset if gameover, then render next frame
        if USER:
            if self.direction != None:
                self.s.move(self.direction)
                self.old_direction = self.direction
        else:
            self.s.move(randint(0, 3))
            
        if self.s.gameover:
            self.s.new_game()
            self.direction = None
            
        self.w.after(100, self.render)

    def keydown(self, key):
        k = key.keycode
        
        KEY_LEFT = 37
        KEY_UP = 38
        KEY_RIGHT = 39
        KEY_DOWN = 40

        # Flipping up and down because display works top to bottom
        directions = {KEY_LEFT: LEFT, KEY_UP: DOWN,
                      KEY_RIGHT: RIGHT, KEY_DOWN: UP}

        if k in directions.keys():
            new_direction = directions[k]
            if new_direction != OPPOSITE_DIRECTION[self.old_direction]:
                self.direction = directions[k]
        
game = Display(window)
window.mainloop()
