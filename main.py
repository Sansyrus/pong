import pygame 
import sys
from Button import Button
from Menu import Menu
from Game import Game


pygame.init()

game = Game(800, 600)

game.run()
