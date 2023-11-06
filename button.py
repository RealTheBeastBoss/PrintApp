from app import *

class Button:
    def __init__(self, text, x_pos, y_pos, height, size, width = 0):
        self.text = text
        self.xPos = x_pos
        self.yPos = y_pos
        self.height = height
        self.size = size
        self.colourOne = App.BACKGROUND
        self.colourTwo = App.FOREGROUND
        self.width = width
        self.draw()

    def draw(self):
        if self.width == 0:
            button_text = Font.render(self.text, self.colourTwo, size=int(self.size * App.HEIGHT / 720))[0]
            self.width = button_text.get_width() + 20
        button_rect = pygame.rect.Rect((self.xPos - (self.width/2), self.yPos - (self.height/2)), (self.width, self.height))
        if not self.check_hover():
            button_text = Font.render(self.text, self.colourTwo, size=int(self.size * App.HEIGHT / 720))[0]
            pygame.draw.rect(App.WINDOW, self.colourOne, button_rect, 0, 5)
            pygame.draw.rect(App.WINDOW, self.colourTwo, button_rect, 3, 5)
        else:
            button_text = Font.render(self.text, self.colourOne, size=int(self.size * App.HEIGHT / 720))[0]
            pygame.draw.rect(App.WINDOW, self.colourTwo, button_rect, 0, 5)
            pygame.draw.rect(App.WINDOW, self.colourOne, button_rect, 3, 5)
        text_width_offset = button_text.get_width() / 2
        text_height_offset = button_text.get_height() / 2
        App.WINDOW.blit(button_text, ((self.xPos - text_width_offset), self.yPos - text_height_offset))

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect((self.xPos - (self.width/2), self.yPos - (self.height/2)), (self.width, self.height))
        if button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def check_click(self):
        button_rect = pygame.rect.Rect((self.xPos - (self.width/2), self.yPos - (self.height/2)), (self.width, self.height))
        mouse_pos = pygame.mouse.get_pos()
        if App.LEFT_MOUSE_RELEASED and button_rect.collidepoint(mouse_pos) and App.BUTTONS_ENABLED:
            pygame.time.set_timer(BUTTON_COOLDOWN_EVENT, 100, 1)
            App.BUTTONS_ENABLED = False
            return True
        return False