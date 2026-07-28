import pygame

pygame.init()

text_font = pygame.font.Font("fonts/Pixeltype.ttf", 30)

stamina_text_1= text_font.render("Stamina", False, "white")
stamina_text_2 = text_font.render("Stamina", False, "red")
stamina_text_rect = stamina_text_1.get_rect(center = (100,20))

stamina_text = [stamina_text_1, stamina_text_2]

def alternate_text_color(dt, text_list):
    index = 0
    
    if index >= len(text_list):
        index = 0
    else:
        index += 0.4 * dt
        
    return index


