from app import *
from button import Button
import win32print
pygame.display.set_caption("Printing App")
printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)

def draw_window():
    App.WINDOW.fill((255, 255, 255))
    draw_text("Printing App", 30, (0, 0, 0), (width_relative(50), height_relative(5)))
    if App.SELECTED_FILE != "":
        draw_wrapped_text("Current File: " + App.SELECTED_FILE, 11, (0, 0, 0), (width_relative(50), height_relative(10)), width_relative(50))
    else:
        draw_text("No File Selected", 11, (0, 0, 0), (width_relative(50), height_relative(10)))
    draw_text("Quantity: " + str(App.QUANTITY), 25, (0, 0, 0), (width_relative(50), width_relative(10)))
    if App.PRINTER_HANDLER is None:
        for x in range(len(printers)):
            text_surface = Font.render(printers[x][2], (0, 0, 0), size=int(11 * App.HEIGHT / 720))[0]
            text_rect = text_surface.get_rect()
            App.WINDOW.blit(text_surface, (width_relative(50) - text_rect.width / 2, App.HEIGHT / 4 + (x * App.HEIGHT / 40)))
            text_rect.topleft = (width_relative(50) - text_rect.width / 2, height_relative(25) + (x * App.HEIGHT / 40))
            if App.LEFT_MOUSE_RELEASED and text_rect.collidepoint(pygame.mouse.get_pos()):
                PRINTER_DEFAULTS = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
                App.PRINTER_HANDLER = win32print.OpenPrinter(printers[x][2], PRINTER_DEFAULTS)
    if App.SELECTED_FILE != "" and App.PRINTER_HANDLER is not None and App.QUANTITY != "" and int(App.QUANTITY) > 0:
        print_button = Button("Print", width_relative(50), height_relative(33), App.HEIGHT / 30, 20)
        if print_button.check_click():
            properties = win32print.GetPrinter(App.PRINTER_HANDLER, 2)
            properties["pDevMode"].Copies = int(App.QUANTITY)
            win32print.SetPrinter(App.PRINTER_HANDLER, 2, properties, 0)
            job_info = win32print.StartDocPrinter(App.PRINTER_HANDLER, 1, (App.SELECTED_FILE, None, "RAW"))
            win32print.StartPagePrinter(App.PRINTER_HANDLER)
            win32print.WritePrinter(App.PRINTER_HANDLER, App.FILE_HANDLER.read())
            win32print.EndPagePrinter(App.PRINTER_HANDLER)
            win32print.EndDocPrinter(App.PRINTER_HANDLER)

def height_relative(vh):
    vh /= 100
    return App.HEIGHT * vh

def width_relative(vw):
    vw /= 100
    return App.WIDTH * vw

def draw_wrapped_text(text, size, colour, location, max_width):
    text_lines = []
    text_part = ""
    for letter in text:
        text_part += letter
        width = Font.get_rect(text_part, size=int(size * App.HEIGHT / 720)).width
        if width > max_width:
            text_lines.append(text_part)
            text_part = ""
    if text_part != "":
        text_lines.append(text_part)
    for x in range(len(text_lines)):
        text_surface = Font.render(text_lines[x], colour, size=int(size * App.HEIGHT / 720))[0]
        App.WINDOW.blit(text_surface, (location[0] - text_surface.get_width() / 2, (location[1] + (x * (App.HEIGHT / 40)))))

def draw_text(text, size, colour, location):
    text_surface = Font.render(text, colour, size=int(size * App.HEIGHT / 720))[0]
    App.WINDOW.blit(text_surface, (location[0] - text_surface.get_width() / 2, location[1]))

if __name__ == '__main__':
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        App.LEFT_MOUSE_RELEASED = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                App.WINDOW = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                App.WIDTH = event.size[0]
                App.HEIGHT = event.size[1]
            elif event.type == pygame.DROPFILE:
                for letter in event.file:
                    App.SELECTED_FILE += letter
                    if letter == "\\":
                        App.SELECTED_FILE += "\\"
                App.FILE_HANDLER = open(App.SELECTED_FILE, "rb")
            elif event.type == pygame.KEYDOWN:
                if event.key in ALLOWED_KEYS:
                    if event.key != pygame.K_BACKSPACE:
                        App.QUANTITY += event.unicode
                    else:
                        App.QUANTITY = App.QUANTITY[:-1]
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                App.LEFT_MOUSE_RELEASED = True
            elif event.type == BUTTON_COOLDOWN_EVENT:
                App.BUTTONS_ENABLED = True
        draw_window()
        pygame.display.update()
