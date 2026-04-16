import pygame
from Menu import Menu
from Option import Option
import sys


class Game():
    def __init__(self, w, h):
        self.menu = Menu(w, h, self)
        self.option = Option(w, h, self)
        self.current_state = "MENU"
        self.running = True
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((w, h), pygame.SCALED)
        self.FPS = 60
        self.clock = pygame.time.Clock()
    

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            if self.current_state == "MENU":
                self.menu.handle_event(events)
                self.menu.display_MENU(self.screen)
            elif self.current_state == "OPTION":
                self.option.handle_event(events)
                self.option.display_OPTION(self.screen)
            pygame.display.flip()
            self.clock.tick(self.FPS)
        pygame.quit()
        sys.exit()

