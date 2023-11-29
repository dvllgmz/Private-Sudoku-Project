import pygame

background_color, primary_color, secondary_color, tertiary_color = (18,18,18), (65,76,80), (7,132,181), (45,56,60)

pygame.init()
screen = pygame.display.set_mode((500, 650))


def game_screen():
    # grid lines
    for i in range(10): # draws both horizontal and vertical lines, 10 lines in each
        pygame.draw.line(screen, tertiary_color, (25, 25 + (i*50)), (500-25, 25 + (i * 50)), width=2)
        pygame.draw.line(screen, tertiary_color, (25 + (i*50), 25), (25 + (i * 50), 500-25), width=2)
    for i in range(4):  # draws wider lines every 3, to separate the 9 subsections
        pygame.draw.line(screen, secondary_color, (25, 25 + (i*150)), (500-25, 25 + (i*150)), width=5)
        pygame.draw.line(screen, secondary_color, (25 + (i*150), 25), (25 + (i*150), 500-25), width=5)



while True:
    pygame.event.get()
    screen.fill(background_color)
    game_screen()
    pygame.display.update()
