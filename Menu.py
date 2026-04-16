import pygame
from Button import Button
import sys
from Option import Option


class Menu:
    def __init__(self, w, h, game):
        self.state = "MENU"
        self.btn_jouer = Button(370, 250, 80, 40, "jouer")
        self.btn_option = Button(370, 330, 80, 40, "option")
        self.btn_quitter = Button(370, 410, 80, 40, "quitter")
        self.list_btns = [self.btn_jouer, self.btn_option, self.btn_quitter]
        self.font_title = pygame.font.SysFont('leelawadee', 72, bold=True)
        self.width = w
        self.height = h
        self.game = game


    def display_MENU(self, screen):
        screen.fill((25, 25, 35))

        surf_texte = self.font_title.render('PONG', True, (255, 255, 255))
        rect_texte = surf_texte.get_rect(center=(self.width // 2, 150))
        screen.blit(surf_texte, rect_texte)
        for btn in self.list_btns:
            btn.draw(screen)
        
    def handle_event(self, events):
        for event in events:
            if self.btn_jouer.handle_event(event):
                print("")
            elif self.btn_option.handle_event(event):
                self.game.current_state = "OPTION"
            elif self.btn_quitter.handle_event(event):
                sys.exit()