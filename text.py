import pygame
pygame.init()
from constants import TEXT_FONT as text_font, TEXT_COLOR


stamina_text = text_font.render("Stamina", False, TEXT_COLOR)
stamina_text_rect = stamina_text.get_rect(center = (100,20))

score_text = text_font.render(f"Score: ", False, TEXT_COLOR)
score_text_rect = score_text.get_rect(center = (100, 80))



