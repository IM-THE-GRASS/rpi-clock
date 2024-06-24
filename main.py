import pygame
import datetime
import os
import json
import requests
pygame.init()
   
f = open("settings.json", "r")
settings = f.read()
f.close()
settings = json.loads(settings)
print(type(settings["font"][1]))

font = settings["font"][0]
quotes = settings["quotes"][0]

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("clock")
screen_size = pygame.display.get_window_size()
screen_width = screen_size[0]
screen_height = screen_size[1]




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
        self.buttons = {}
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
    def open(self):
        self.enabled = True
    def close(self):
        self.enabled = False
    def draw(self):
        if self.enabled == False:
            return
        pygame.draw.rect(screen,(255,255,255), self.outline) # menu outline
        pygame.draw.rect(screen,self.color,self.bg) # menu
        
        self.draw_setting(0, self.name) # settings text
        
        self.draw_setting(1, "font", font)
        self.draw_setting(2, "quotes", quotes)
        self.draw_setting(6, "save")
    def draw_setting(self, number, text, value = None):
        if value != None:
            menu_text = text + " = " + str(value).lower()
        else:
            menu_text = text
        text_size = int(screen_height / 10.5)
        menu_font = pygame.font.SysFont("sans", text_size, True)
        text_surface = menu_font.render(menu_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.bg.x + self.bg.width / 100, self.bg.y + self.bg.width/100 + number * text_rect.height * 1.2)
        pygame.draw.rect(screen,(255,255,255), text_rect)
        screen.blit(text_surface, text_rect) 
        self.buttons[text] = text_rect
        
        return text_rect
    def on_click(self, button):
        if not self.enabled:
            return
        def update_value(key):
            current_value = settings[key][1].index(settings[key][0])
            print(current_value)
            try:
                new_value = settings[key][1][current_value + 1]
            except:
                new_value = settings[key][1][0]
            print(new_value)
            settings[key][0] = new_value
            print(settings[key][0])
        if button == "font":
            update_value(button)
        elif button == "quotes":
            update_value(button)
            print("g")
        elif button == "save":
            
            f = open("settings.json", "w")
            f.write(json.dumps(settings, indent=4))
            f.close()
            self.close()
quote_count = 19999999
def get_quote():
    global quote_count
    txt = open("quote.txt", "r").read().split("\n")
    if quote_count < 9999999:
        print(quote_count)
        quote_count +=1
        return txt[0], txt[1]
    quote_count = 0
    data = requests.get("https://zenquotes.io/api/random").json()[0]
    quoted = data["q"]
    author = data["a"]
    if quoted != "Too many requests. Obtain an auth key for unlimited access.":
        open("quote.txt", "w").write(quoted + "\n--" + author)
        return quoted,author
    else:
        return txt[0], txt[1]

def write_text(text, text_font, location, color = (255,255,255)):
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = location
    screen.blit(text_surface, text_rect)
    return text_rect
            
            
            
            

        
        
settings_menu = menu("settings", (0,0,0))

settings_button = button(
    screen_width / 1.15,
    screen_height / 15,
    screen_width/10,
    screen_width/10,
    "settings.png"
)

running = True
while running:
    quotes = settings["quotes"][0]
    font = settings["font"][0]
    #time stuff
    now = datetime.datetime.now()
    times = now.strftime("%I:%M %p")
    time_font = pygame.font.SysFont(font, int(screen_width / 5), bold=True)
    
    
    
        

    
    screen.fill((0, 0, 0))
    write_text(times,time_font,(screen_width / 2, screen_height / 2))
    
    
    
    if quotes:
        quote_font = pygame.font.SysFont(font, int(screen_width / 40), bold=True)
        quote, author = get_quote()
        quote1 = quote[:80]
        quote2 = quote[80:160]
        quote3 = quote[160:240]
        quote_rect1 = write_text(quote1,quote_font,(screen_width / 2, screen_height / 1.4))
        quote_rect2 = write_text(quote2,quote_font,(screen_width / 2, screen_height / 1.3))
        quote_rect3 = write_text(quote3,quote_font,(screen_width / 2, screen_height / 1.2))
        author_rect = write_text(author,quote_font,(quote_rect3.centerx, quote_rect3.centery + 50))
        
    settings_button.draw()
    settings_menu.draw()
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_ESCAPE]:
        settings_menu.close()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if settings_button.get_rect().collidepoint(event.pos):
                if settings_menu.enabled == False:
                    settings_menu.open()
            for key in settings_menu.buttons.keys():
                rect = settings_menu.buttons[key]
                if rect.collidepoint(event.pos):
                    settings_menu.on_click(key)
            

pygame.quit()