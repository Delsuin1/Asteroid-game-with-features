import pygame
from rectshape import RectShape
from text import stamina_text, stamina_text_rect
from constants import BAR_COLOR, BOARDER_WIDTH


class Hud(RectShape):
    def __init__(self, player):
        super().__init__()
        self.player = player
        
    def draw(self, screen):
        screen.blit(stamina_text, stamina_text_rect)
        current_stamina = self.player.useable_stamina

        # stamina_bar 
        pygame.draw.rect(screen, "grey", (50,30,current_stamina,30))
        # stamina_boarder
        pygame.draw.rect(screen, "Blue", (50,30,100,30), BOARDER_WIDTH)
        
        
    
    def update(self, dt):
        pass
        

