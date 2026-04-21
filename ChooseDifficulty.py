import pygame
from Button import Button   

class ChooseDifficulty:
    def __init__(self,w, h, game):
        self.w = w
        self.h = h
        self.game = game
        self.btn_easy = Button(370, 250, 80, 40, "easy")
        self.btn_normal = Button(370, 330, 80, 40, "normal")
        self.btn_hard = Button(370, 410, 80, 40, "hard")
        self.font = pygame.font.SysFont("arial", 72, True)
        self.btn = [self.btn_easy, self.btn_normal, self.btn_hard]

    def display_screen(self, screen):
        screen.fill((25, 25, 35))
        for btn in self.btn:
            btn.draw(screen)
        surf_texte = self.font.render('Choose Difficulty', True, (255, 255, 255))
        rect_texte = surf_texte.get_rect(center=(self.w // 2, 150))
        screen.blit(surf_texte, rect_texte)
    
    def handle_event(self, events):
        for event in events:
            if self.btn_easy.handle_event(event):
                self.game.current_state = "EASY"

            elif self.btn_normal.handle_event(event):
                self.game.current_state = "NORMAL"

            elif self.btn_hard.handle_event(event):
                self.game.current_state = "HARD"

    