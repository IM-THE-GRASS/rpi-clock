import pygame
import datetime
import os
pygame.init()


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("clock")
screen_size = pygame.display.get_window_size()
screen_width = screen_size[0]
screen_height = screen_size[1]
print(screen_size)
class button:
    def __init__(self,x,y,width,height,image_path,bg_color = None):
        self.x = x
        self.y = y
        self.bg_color = bg_color
        
        self.rect = pygame.Rect(self.x,self.y,width,height)
        print(image_path)
        self.image = pygame.image.load(os.path.join("data", image_path))
        self.image = pygame.transform.scale(self.image, (width, height))
    def draw(self):
        if self.bg_color != None:
            pygame.draw.rect(screen,pygame.Color(255,255,255),self.rect)
        screen.blit(self.image,(self.x,self.y))
        
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
    settings = button(
        screen_width / 1.15,
        screen_height / 15,
        screen_width/10,
        screen_width/10,
        "settings.png"
        )

    
    screen.fill((0, 0, 0))
    screen.blit(text_surface, text_rect)
    settings.draw()
    pygame.display.flip()


    pygame.time.delay(1000)

pygame.quit()