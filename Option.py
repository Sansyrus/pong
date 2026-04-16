import pygame
from Button import Button

class Option:
    def __init__(self, w, h, game):
        self.state = "OPTION"
        self.w = w
        self.h = h
        self.btn_menu = Button(400, 200, 80, 50, "Menu")
        self.game = game
    
    def handle_event(self, events):
        for event in events:
            if self.btn_menu.handle_event(event):
                self.game.current_state = "MENU"
    def display_OPTION(self, screen):
        screen.fill((0, 255, 255))
        self.btn_menu.draw(screen)
