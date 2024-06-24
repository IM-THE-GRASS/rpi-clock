import pygame
import datetime
import os
import json


pygame.init()

f = open("settings.json", "r")
settings = f.read()
f.close



screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("clock")
screen_size = pygame.display.get_window_size()
screen_width = screen_size[0]
screen_height = screen_size[1]
font = "sans"


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
        menu_x = screen_width/20
        menu_y = screen_height/20
        menu_width = screen_width - screen_width/10
        menu_height = screen_height - screen_height/10
        
        self.bg = pygame.Rect(
            menu_x,
            menu_y,
            menu_width,
            menu_height
        )
        self.outline = pygame.Rect(
            menu_x - screen_width/60,
            menu_y - screen_width/60,
            menu_width + screen_width/30,
            menu_height + screen_width/30
        )
    def draw_text(self, text, number, text_size):
        menu_font = pygame.font.SysFont(font, text_size, True)
        text_surface = menu_font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.bg.x + self.bg.width / 100, self.bg.y + self.bg.width/100 + number * text_rect.height * 1.2)
        pygame.draw.rect(screen,(255,255,255), text_rect)
        screen.blit(text_surface, text_rect) 
        
        return text_rect
    def open(self):
        self.enabled = True
    def close(self):
        self.enabled = False
    def draw(self):
        if self.enabled == True:
            text_size = int(screen_width / 20)
            pygame.draw.rect(screen,(255,255,255), self.outline)
            pygame.draw.rect(screen,self.color,self.bg)
            self.draw_text(self.name, 0, text_size)
            
            self.draw_text("font = " + font, 1, text_size)
            
            self.draw_text("save", 6, text_size)
            
            
            
            
            
            
            
            
            
    
        
        
settings_menu = menu("settings", (0,0,0))

settings = button(
    screen_width / 1.15,
    screen_height / 15,
    screen_width/10,
    screen_width/10,
    "settings.png"
)

running = True
while running:
    

    #time stuff
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")

    time_font = pygame.font.SysFont("sans", int(screen_width / 5), bold=True)
    text_surface = time_font.render(time, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height / 2))
    

    
    screen.fill((0, 0, 0))
    screen.blit(text_surface, text_rect)
    
    
    settings.draw()
    settings_menu.draw()
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_ESCAPE]:
        settings_menu.close()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if settings.get_rect().collidepoint(event.pos):
                
                if settings_menu.enabled == False:
                    settings_menu.open()

    pygame.time.delay(1)

pygame.quit()