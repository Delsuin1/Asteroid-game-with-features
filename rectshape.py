import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
class RectShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

