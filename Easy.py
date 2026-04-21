import pygame
from Paddle import Paddle
from Pong import Pong

class Easy:
    
    def __init__(self, w, h, game):
        self.scoreIA = 0
        self.scoreJ = 0
        self.w = w
        self.h = h
        self.state = "EASY"
        self.game = game
        self.paddle = Paddle(0, 0)
        self.ball = Pong((self.w // 2), (self.h //2))
        self.paddle_ia = Paddle(w-(2*self.paddle.rect.centerx), h-(self.paddle.rect.centery*2))
        self.font = pygame.font.SysFont("arial", 16, bold= True)
        
    
    def display_screen(self, screen):
        screen.fill((25, 25, 35))
        self.paddle.draw(screen)
        self.paddle_ia.draw(screen)
        self.ball.draw(screen)
        text_surf = self.font.render(f"score : {self.scoreJ}", True, (255, 255, 255))
        text_surf2 = self.font.render(f"score : {self.scoreIA}", True, (255, 255, 255))
        text_rect = text_surf.get_rect()
        text_rect2 = text_surf2.get_rect(center=(self.w -36, 8))
        screen.blit(text_surf, text_rect)
        screen.blit(text_surf2, text_rect2)
        
        
    
    
    def run(self, events):
        my = pygame.mouse.get_pos()[1]
        self.paddle.move_to_y(my, self.h)
        self.ball.update(self.h)

        self.paddle_ia.follow_ball(self.ball.rect.centery, speed=4, screen_height=self.h)


        #collision balle paddleJ
        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.bounce_off_paddle(1)
            self.ball.rect.left = self.paddle.rect.right

        #collision balle paddleiIA
        if self.ball.rect.colliderect(self.paddle_ia.rect):
            self.ball.bounce_off_paddle(1)
            self.ball.rect.right = self.paddle_ia.rect.left

        #point sort à gauche point IA
        if self.ball.rect.right < 0:
            self.scoreIA +=1
            print(self.scoreIA)
            self.ball.reset(self.w//2, self.h//2, go_left=False)
        
        if self.ball.rect.left > self.w:
            self.scoreJ += 1
            print(self.scoreJ)
            self.ball.reset(self.w//2, self.h//2, go_left=True)

        if self.scoreJ >= 5 or self.scoreIA >=5:
            self.game.current_state = "GAMEOVER"
