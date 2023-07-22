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