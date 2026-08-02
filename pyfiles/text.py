import pygame
pygame.init()
from pyfiles.constants import TEXT_FONT as text_font, TEXT_COLOR, MENU_TEXT_FONT


fuel_text = MENU_TEXT_FONT.render("FUEL", False, TEXT_COLOR)
fuel_text = pygame.transform.rotate(fuel_text, 90)
fuel_text_rect = fuel_text.get_rect(center = (100,600))


score_text = MENU_TEXT_FONT.render(f"Lives", False, TEXT_COLOR)
score_text_rect = score_text.get_rect(center = (235, 680))



