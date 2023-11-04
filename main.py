from app import *
pygame.display.set_caption("Printing App")

def draw_window():
    App.WINDOW.fill((255, 255, 255))
    draw_text("Printing App", 30, (0, 0, 0), (App.WIDTH / 2, App.HEIGHT / 20))

def draw_text(text, size, colour, location):  # Draws text centered on a location
    text_surface = Font.render(text, colour, size=int(size * App.HEIGHT / 720))[0]
    App.WINDOW.blit(text_surface, (location[0] - text_surface.get_width() / 2, location[1]))

if __name__ == '__main__':
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.VIDEORESIZE:
                App.WINDOW = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                App.WIDTH = event.size[0]
                App.HEIGHT = event.size[1]
        draw_window()
        pygame.display.update()
