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
        
        self.bg = pygame.Rect(self.x,self.y,width + screen_width / 25,height + screen_height / 25)
        print(image_path)
        self.image = pygame.image.load(os.path.join("data", image_path))
        self.image = pygame.transform.scale(self.image, (width, height))
    def get_rect(self):
        return self.bg
    def draw(self):
        if self.bg_color != None:
            pygame.draw.rect(screen,self.bg_color,self.bg)
            
        screen.blit(self.image,(self.x,self.y))
class menu:
    def __init__(self, name, color):
        self.enabled = False
        self.name = name
        self.color = color
        self.bg = pygame.Rect(
            screen_width/6,
            screen_height/6,
            screen_width - screen_width/3,
            screen_height - screen_height/3
        )
        self.outline = pygame.Rect(
            screen_width/6 - screen_width/25,
            screen_height/6- screen_width/25,
            screen_width - screen_width/3+ screen_width/25,
            screen_height - screen_height/3+ screen_width/25
        )
        
    def open(self):
        self.enabled = True
    def close(self):
        self.enabled = False
    def draw(self):
        if self.enabled == True:
            pygame.draw.rect(screen,(165,83,34), self.outline)
            pygame.draw.rect(screen,self.color,self.bg)
            
    
        
        
settings_menu = menu("settings", (0,0,0))
font = pygame.font.SysFont("sans", int(screen_width / 5), bold=True)
settings = button(
    screen_width / 1.15,
    screen_height / 15,
    screen_width/10,
    screen_width/10,
    "settings.png"
)
# Font setup
running = True
while running:
    

    #time stuff
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")


    text_surface = font.render(time, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height / 2))
    

    
    screen.fill((0, 0, 0))
    screen.blit(text_surface, text_rect)
    settings.draw()
    settings_menu.draw()
    pygame.display.flip()

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if settings.get_rect().collidepoint(event.pos):
                if settings_menu.enabled:
                    settings_menu.close()
                else:
                    settings_menu.open()

    pygame.time.delay(1)

pygame.quit()