import pygame

class GameOver:
    def __init__(self, w, h, game):
        self.w = w
        self.h = h
        self.game = game

    def display_screen(self, screen):
        screen.fill((25, 25, 35))