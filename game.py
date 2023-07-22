import pygame
import time
import random
from snake import Snake

class Game:
    def __init__(self):
        # Set up the screen and other game variables
        self.screen_width = 800
        self.screen_height = 600
        self.game_display = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.block_size = 20
        self.snake_speed = 15
        self.snake = Snake(self.screen_width, self.screen_height, self.block_size)
        self.food = self.generate_food()
    
    def generate_food(self):
        food_x = round(random.randrange(0, self.screen_width - self.block_size) / self.block_size) * self.block_size
        food_y = round(random.randrange(0, self.screen_height - self.block_size) / self.block_size) * self.block_size
        return food_x, food_y
    
    def draw_food(self):
        pygame.draw.rect(self.game_display, (213, 50, 80), [self.food[0], self.food[1], self.block_size, self.block_size])


    def run(self):
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    self.snake.handle_event(event.key)

            self.snake.move()
            if self.snake.check_collision(self.screen_width, self.screen_height):
                game_over = True
            if self.snake.check_eat(self.food):
                self.snake.grow()
                self.food = self.generate_food()

            self.game_display.fill((255, 255, 255))
            self.draw_food()
            self.snake.draw(self.game_display)

            pygame.display.update()
            self.clock.tick(self.snake_speed)

        pygame.quit()