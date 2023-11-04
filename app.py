import os
import pygame.freetype
pygame.freetype.init()
FPS = 60

Font = pygame.freetype.Font(os.path.join("Fonts", "beastboss_font.ttf"))

class App:
    WIDTH, HEIGHT = 1280, 720
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
