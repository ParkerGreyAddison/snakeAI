HEIGHT = 20
WIDTH = 20
SCL = 30
DISPLAY = True

def setup():
    size(WIDTH * SCL, HEIGHT * SCL)
    colorMode(RGB)
    noStroke()
    
    global s
    s = Snake()
    s.new_game()
    
    
from random import randint
import time

class Snake:

    START_LENGTH = 5

    def __init__(self):
        self.h = HEIGHT
        self.w = WIDTH
        self.score = 0
        self.gameover = False

    def init_snake(self):
        """
        Initializes our snake to the center of the field
        """
        self.snake = []
        start_x = self.w // 2
        start_y = self.h // 2
        
        for i in range(self.START_LENGTH):
            self.snake.append({'x':start_x - i, 'y':start_y})

    def new_game(self):
        self.__init__()
        self.init_snake()
        self.add_food()
        if DISPLAY:
            self.render()
        return self.observe()

    def move(self, direction):
        self.add_snake(direction)

        if self.check_food():
            self.score += 1
            self.add_food()

        else:
            self.remove_snake()

        self.gameover = self.check_gameover()
        
        if DISPLAY:
            self.render()

        return self.observe()

    def add_food(self):
        """
        Adds a new piece of food to the field
        """
        food = {}

        while food == {}:
            food['x'] = randint(0, self.w - 1)
            food['y'] = randint(0, self.h - 1)

            if food in self.snake:
                food = {}

        self.food = food

    def add_snake(self, direction):
        """
        Adds a new head to the snake in a given direction
        """
        # keys = {
        #     0: 'left',
        #     1: 'up',
        #     2: 'right',
        #     3: 'down'
        # }

        new_x = self.snake[0]['x']
        new_y = self.snake[0]['y']

        if direction == 0:
            new_x += 1
        elif direction == 1:
            new_y += 1
        elif direction == 2:
            new_x -= 1
        elif direction == 3:
            new_y -= 1

        self.snake.insert(0, {'x': new_x, 'y': new_y})

    def remove_snake(self):
        """
        Removes the tail of the snake
        """
        self.snake.pop()

    def check_gameover(self):
        """
        Checks if the head of the snake has run into a wall or itself
        """
        head = self.snake[0]

        if (head['x'] < 0 \
        or head['x'] >= self.w \
        or head['y'] < 0 \
        or head['y'] >= self.h \
        or head in self.snake[1:]):
            return True
        else:
            return False
    
    def check_food(self):
        """
        Checks if the head of the snake is in the same position as the food
        """
        if self.snake[0] == self.food:
            return True
        else:
            return False

    def observe(self):
        """
        Return where the snake is, where the food is, what the score is, and if gameover

        The h and w should be constants, so no need to observe these
        """
        return self.snake, self.food, self.score, self.gameover

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
        
        time.sleep(0.01)
        
def draw():
    s.move(randint(0, 3))
    if s.gameover:
        s.new_game()
