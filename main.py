import pygame
import datetime

pygame.init()


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Current Time Clock (12-hour)")
screen_size = pygame.display.get_window_size()
screen_width = screen_size[0]
screen_height = screen_size[1]
print(screen_size)

font = pygame.font.SysFont("sans", int(screen_width / 5), bold=True)
# Font setup
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #time stuff
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")


    text_surface = font.render(time, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height / 2))


    screen.fill((0, 0, 0))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


    pygame.time.delay(1000)

pygame.quit()