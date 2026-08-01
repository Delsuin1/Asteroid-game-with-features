import pygame
from pyfiles.constants import SCREEN_WIDTH, SCREEN_HEIGHT
class RectShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    
    def __init__(self, x=0, y=0):
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.image = pygame.Surface((SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3))
        self.image.fill("red")
        self.rect = self.image.get_rect(center = (0,0))
            
    def draw(self, screen):
        pass

    
    def update(self, dt):
        pass
        

