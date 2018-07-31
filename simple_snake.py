import numpy as np
from random import randint
from collections import deque

import tkinter as tk

EMPTY = 0
BODY = 5
FOOD = 1

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

class Display:

    def __init__(self, height=20, width=20, scale=30):
        self.height = height
        self.width = width
        self.scale = scale

        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.w = tk.Canvas(self.window, width=self.width * self.scale, height=self.height * self.scale)
        self.w.pack()

        self.snake = Snake(self.height, self.width)

        self.sboard = self.snake.board.reshape((self.height, self.width))
        self.gboard = self.sboard.copy()

        for row in range(self.height):
            for col in range(self.width):
                color = 'gray'
                if self.sboard[row, col] == BODY:
                    color = 'white'
                elif self.sboard[row, col] == FOOD:
                    color = 'green'

                self.gboard[row, col] = self.w.create_rectangle(
                        col * self.scale, row * self.scale,
                        (col + 1) * self.scale, (row + 1) * self.scale,
                        fill=color, outline='')
        
        self.window.bind('<KeyPress>', self.keydown)

    def draw(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.sboard[row, col] == EMPTY:
                    self.w.itemconfig(self.gboard[row, col], fill='gray')
                elif self.sboard[row, col] == BODY:
                    self.w.itemconfig(self.gboard[row, col], fill='white')
                elif self.sboard[row, col] == FOOD:
                    self.w.itemconfig(self.gboard[row, col], fill='green')

    def keydown(self, key):
        k = key.keycode
        
        key_left = 37
        key_up = 38
        key_right = 39
        key_down = 40

        directions = {key_left: LEFT, key_up: UP, key_right: RIGHT, key_down: DOWN}

        self.snake.move(directions[k])
        self.draw()
    

class Snake:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.snake = deque()
        self.score = 0

        self.init_board()
        self.init_snake()
        self.add_food()


    def init_board(self):
        self.board = np.zeros(self.height * self.width, dtype=int)

    def init_snake(self):
        # Middlemost index
        start_loc = (self.height // 2) * self.width + (self.width // 2)
        
        start_length = 3
        for i in range(start_length):
            segment = start_loc - start_length + 1 + i
            self.board[segment] = BODY
            self.snake.append(segment)

    def add_food(self):
        placed = False
        while not placed:
            food_loc = randint(0, self.height * self.width - 1)
            if self.board[food_loc] == EMPTY:
                self.board[food_loc] = FOOD
                placed = True

    def move(self, direction):
        curr_head = self.snake[-1]
        new_head = 0

        if direction == LEFT:
            new_head = curr_head - 1

        elif direction == UP:
            new_head = curr_head - self.width

        elif direction == RIGHT:
            new_head = curr_head + 1

        elif direction == DOWN:
            new_head = curr_head + self.width

        # Check for food
        try:
            eaten = self.check_food(new_head)
            if eaten:
                self.score += 1
                self.add_food()
            else:
                # Remove tail if not eaten
                self.board[self.snake.popleft()] = EMPTY

                # Then check for collision
                if self.check_collision(direction, new_head):
                    self.gameover()

        except IndexError:
            self.gameover()

        # Add new head to snake
        self.board[new_head] = BODY
        self.snake.append(new_head)

    def check_food(self, loc):
        return self.board[loc] == FOOD

    def check_collision(self, direction, loc):

        if self.board[loc] == BODY:
            return True

        if direction == LEFT:
            if (loc + 1) % self.width == 0:
                return True
        elif direction == UP:
            if loc < 0:
                return True
        elif direction == RIGHT:
            if loc % self.width == 0:
                return True
        elif direction == DOWN:
            if loc >= self.height * self.width:
                return True

        return False

    def gameover(self):
        raise Exception('Gameover. Your score was: {}'.format(self.score))