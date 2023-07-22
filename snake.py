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

    def move(self):
        self.lead_x += self.lead_x_change
        self.lead_y += self.lead_y_change

    def check_collision(self, screen_width, screen_height):
        if self.lead_x >= screen_width or self.lead_x < 0 or self.lead_y >= screen_height or self.lead_y < 0:
            return True
        return False

    def check_eat(self, food):
        if self.lead_x == food[0] and self.lead_y == food[1]:
            return True
        return False

    def grow(self):
        self.snake_length += 1

    def draw(self, game_display):
        self.snake_head = []
        self.snake_head.append(self.lead_x)
        self.snake_head.append(self.lead_y)
        self.snake_list.append(self.snake_head)

        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

        for segment in self.snake_list[:-1]:
            if segment == self.snake_head:
                return True

        for x in self.snake_list:
            pygame.draw.rect(game_display, (0, 255, 0), [x[0], x[1], self.block_size, self.block_size])

        return False