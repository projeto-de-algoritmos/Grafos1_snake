import pygame
import time
import random
from snake import Snake

class Level:
    def __init__(self, name, snake_speed):
        self.name = name
        self.snake_speed = snake_speed

class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.game_display = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.block_size = 20
        
        self.levels = [
            Level("Fácil", 10),
            Level("Médio", 15),
            Level("Difícil", 20)
        ]
        self.current_level = 0

        self.snake_speed = 5
        self.snake = Snake(self.screen_width, self.screen_height, self.block_size)
        self.food = self.generate_food()

    def select_level(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.current_level = 0  
                        return
                    elif event.key == pygame.K_2:
                        self.current_level = 1  
                        return
                    elif event.key == pygame.K_3:
                        self.current_level = 2  
                        return
    
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
            self.clock.tick(self.levels[self.current_level].snake_speed)
        
        pygame.quit()