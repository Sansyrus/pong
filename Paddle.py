import pygame

class Paddle:

    def __init__(self, x, y, w=14, h=90, color=(40, 56, 234)):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=4)
    
    def move_to_y(self, target_y, screen_height):
        self.rect.centery = target_y
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(screen_height, self.rect.bottom)

    def follow_ball(self, ball_centery, speed, screen_height):
        pass