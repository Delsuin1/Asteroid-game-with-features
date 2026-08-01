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
explosion_sprite_sheet = pygame.image.load("fx/particlefx_14.png")

def get_sprite_sheet(sprite_sheet, num_col, num_rows, radius, position, rotation=0):
        sheet_width, sheet_height = sprite_sheet.get_size()
        asteroid_frame_width = sheet_width // num_col
        asteroid_frame_height = sheet_height // num_rows
        
        asteroid_frame = []


        for row in range(num_col):
            for col in range(num_col):
                rect = pygame.Rect(
                    col * asteroid_frame_width,
                    row * asteroid_frame_height, 
                    asteroid_frame_width, 
                    asteroid_frame_height
                )
                frame = sprite_sheet.subsurface(rect)
                resized_frame = pygame.transform.rotozoom(frame,rotation,radius)
                
                asteroid_frame.append(resized_frame)
        return asteroid_frame, resized_frame