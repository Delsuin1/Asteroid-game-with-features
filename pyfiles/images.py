import pygame
from pyfiles.constants import X, Y, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from pyfiles.animate import animate
from random import choice
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("images/space.png").convert()
background_rect = background.get_rect(center = (X, Y))
shield = pygame.image.load("images/shield.png").convert_alpha()
shield_image = pygame.transform.rotozoom(shield, 0, 0.4)
asteroid_sprite_sheet = pygame.image.load("images/AsteroidAnimation.png").convert_alpha()
explosion_sprite_sheet = pygame.image.load("fx/particlefx_07.png").convert_alpha()

teleport_sprite1, teleport_rect1 = animate(explosion_sprite_sheet, 8,8, 20*0.05, 4 , 5)
teleport_sprite2, teleport_rect2  = animate(explosion_sprite_sheet, 8,8, 20*0.05, 3 , 7)

