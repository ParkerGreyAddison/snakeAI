HEIGHT = 20
WIDTH = 20
DISPLAY = True
SCL = 30

from random import randint
import time
import sys
import test

def setup():
    size(WIDTH * SCL, HEIGHT * SCL)
    colorMode(RGB)
    noStroke()
    
    global s
    s = Snake(HEIGHT, WIDTH)
    s.new_game()
    if DISPLAY:
        render(s)


def render(self):
    """ PROCESSING CODE HERE """
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
        
def draw():
    s.move(randint(0, 3))
    if DISPLAY:
        render(s)
    if s.gameover:
        s.new_game()
