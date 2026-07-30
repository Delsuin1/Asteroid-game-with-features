import pygame
from rectshape import RectShape
from text import stamina_text, stamina_text_rect, score_text, score_text_rect
from constants import BAR_COLOR, BOARDER_WIDTH, LINE_WIDTH


class Hud(RectShape):
                
    def __init__(self, player):
        super().__init__()
        self.player = player
    

    def stamina_hud(self, screen):
        screen.blit(stamina_text, stamina_text_rect)
        current_stamina = self.player.useable_stamina
        
        pygame.draw.rect(screen, "grey", (50,30,current_stamina,30))
        # stamina_boarder
        pygame.draw.rect(screen, "Blue", (50,30,100,30), BOARDER_WIDTH)
    def lives_hud(self,screen):
        gap = 50
        # (width,height)
        left = (165, 130)  
        middle = (180,90) 
        right = (195,130)
   
        for i in range(self.player.lives):
            triangle = [(left[0] + gap * i, left[1]), (middle[0] + gap * i, middle[1]), (right[0] + gap * i, right[1])]
            player_lives = pygame.draw.polygon(screen, self.player.color, triangle, LINE_WIDTH)
        
        
    def draw(self, screen):
        self.stamina_hud(screen)
        self.lives_hud(screen)
        screen.blit(score_text, score_text_rect)
        
        
    
    def update(self, dt):
        pass
        
