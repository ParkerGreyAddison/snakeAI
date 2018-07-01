from random import randint
import time

class Snake:

    START_LENGTH = 3

    def __init__(self, HEIGHT=20, WIDTH=20):
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
        self.__init__(self.h, self.w)
        self.init_snake()
        self.add_food()
        return self.observe()

    def move(self, direction):
        self.add_snake(direction)

        if self.check_food():
            self.score += 1
            self.add_food()

        else:
            self.remove_snake()

        self.gameover = self.check_gameover()

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

        # TODO: Possibly change so that new direction can be
        # - forwards, - left, - right,
        # to prevent turning back into itself
        if direction == 0:
            new_x -= 1
        elif direction == 1:
            new_y += 1
        elif direction == 2:
            new_x += 1
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
