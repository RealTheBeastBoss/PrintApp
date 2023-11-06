import os
import pygame.freetype
pygame.freetype.init()
FPS = 60

BUTTON_COOLDOWN_EVENT = pygame.USEREVENT + 1
Font = pygame.freetype.Font(os.path.join("Fonts", "beastboss_font.ttf"))

ALLOWED_KEYS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_BACKSPACE]

class App:
    WIDTH, HEIGHT = 1280, 720
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    DARK_MODE = False
    BACKGROUND = (255, 255, 255)
    FOREGROUND = (0, 0, 0)
    SELECTED_FILE = ""
    QUANTITY = "1"
    BUTTONS_ENABLED = True
    LEFT_MOUSE_RELEASED = False
    SELECTED_PRINTER = None
    FILE_HANDLER = None
    PRINTER_HANDLER = None
