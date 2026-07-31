import pygame
pygame.init()

background = pygame.image.load("space.png")
background_rect = background.get_rect(topleft = (0,0))
shield = pygame.image.load("shield.png")
shield_image = pygame.transform.rotozoom(shield, 0, 0.4)