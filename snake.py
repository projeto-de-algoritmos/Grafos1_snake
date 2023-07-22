import pygame

class Snake:
    def __init__(self, screen_width, screen_height, block_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.snake_speed = 20

        self.lead_x = screen_width // 2
        self.lead_y = screen_height // 2
        self.lead_x_change = 0
        self.lead_y_change = 0

        self.snake_list = []
        self.snake_length = 1

    def handle_event(self, key):
        if key == pygame.K_LEFT:
            self.lead_x_change = -self.block_size
            self.lead_y_change = 0
        elif key == pygame.K_RIGHT:
            self.lead_x_change = self.block_size
            self.lead_y_change = 0
        elif key == pygame.K_UP:
            self.lead_y_change = -self.block_size
            self.lead_x_change = 0
        elif key == pygame.K_DOWN:
            self.lead_y_change = self.block_size
            self.lead_x_change = 0