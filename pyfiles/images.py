import pygame
from pyfiles.constants import X, Y, SCREEN_WIDTH, SCREEN_HEIGHT
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def convert(image):
    image.convert_alpha()
    return image
background = pygame.image.load("images/space.png").convert()
background_rect = background.get_rect(center = (X, Y))
shield = pygame.image.load("images/shield.png").convert_alpha()
shield_image = pygame.transform.rotozoom(shield, 0, 0.4)
asteroid_sprite_sheet = pygame.image.load("images/AsteroidAnimation.png").convert_alpha()
explosion_sprite_sheet = pygame.image.load("fx/particlefx_07.png")

