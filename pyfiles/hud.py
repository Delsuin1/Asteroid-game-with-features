import pygame
from pyfiles.rectshape import RectShape
from pyfiles.text import fuel_text, fuel_text_rect, score_text, score_text_rect
from pyfiles.constants import BAR_COLOR, BOARDER_WIDTH, LINE_WIDTH, TEXT_COLOR
from pyfiles.images import teleport_sprite1, teleport_rect1


class Hud(RectShape):
                
    def __init__(self, player):
        super().__init__()
        self.player = player
    

    def fuel_hud(self, screen):
        screen.blit(fuel_text, fuel_text_rect)
        current_stamina = self.player.useable_stamina
        
        pygame.draw.rect(screen, "#596565", (50,670, current_stamina*2, 30))
        # stamina_boarder
        pygame.draw.rect(screen, TEXT_COLOR, (50,670,200, 30), 2)
        
        
    def lives_hud(self,screen):
        gap = 70
        # (width,height)
        # left = (165, 130 * 5)  
        # middle = (180,90 * 6.7) 
        # right = ((195,130 * 5))
   
        # for i in range(self.player.lives):
        #     triangle = [(left[0] + gap * i, left[1]), (middle[0] + gap * i, middle[1]), (right[0] + gap * i, right[1])]
        #     pygame.draw.polygon(screen, self.player.color, triangle, LINE_WIDTH)
        for i in range(self.player.lives):
            screen.blit(teleport_sprite1[10], teleport_sprite1[10].get_rect(center = (190+gap*i,630)))
        
        
    def draw(self, screen):
        self.fuel_hud(screen)
        self.lives_hud(screen)
        screen.blit(score_text, score_text_rect)
        
        
    
    def update(self, dt):
        pass
        
