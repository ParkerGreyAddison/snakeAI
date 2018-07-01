from random import randint
import time
from Snake import Snake

import tkinter as tk

window = tk.Tk()
window.title("Snake Game")

HEIGHT = 20
WIDTH = 20
SCL = 30

s = Snake(HEIGHT, WIDTH)
s.new_game()
s.render()

def render(self):
    fill(150, 150, 150)
    rect(0, 0, width, height)
    
    fill(255, 255, 255)
    for segment in self.snake[1:]:
        rect(segment['x'] * SCL, segment['y'] * SCL, SCL, SCL)
        
    fill(0, 255, 0)
    rect(self.food['x'] * SCL, self.food['y'] * SCL, SCL, SCL)
    
    fill(255, 50, 50)
    rect(self.snake[0]['x'] * SCL, self.snake[0]['y'] * SCL, SCL, SCL)
    
    time.sleep(0.1)
