from random import randint
import time
from Snake import Snake
import tkinter as tk

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-vh", "--height", type=int, default=20,
                    help="sets field height")
parser.add_argument("-vw", "--width", type=int, default=20,
                    help="sets field width")
parser.add_argument("-s", "--scale", type=int, default=30,
                    help="sets display scale")
args = parser.parse_args()
HEIGHT = args.height
WIDTH = args.width
SCL = args.scale

window = tk.Tk()
window.title("Snake Game")
w = tk.Canvas(window, width=WIDTH*SCL, height=HEIGHT*SCL)
w.pack()

class Display:

    def __init__(self, canvas):
        self.w = canvas
        self.s = Snake(HEIGHT, WIDTH)
        self.s.new_game()
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
        self.s.move(randint(0, 3))
        if self.s.gameover:
##            time.sleep(1)
            self.s.new_game()
        self.w.after(100, self.render)
        
        
game = Display(w)
window.mainloop()
