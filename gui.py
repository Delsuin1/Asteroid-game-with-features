import pygame
from constants import BOARDER_WIDTH
class Gui(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
    
    def draw_ui(self, screen):
        used_stamina = pygame.draw.rect(screen, "grey", (50,30,100,30) )
        stamina_boarder = pygame.draw.rect(screen, "blue", (50,30,100,30), BOARDER_WIDTH)
        