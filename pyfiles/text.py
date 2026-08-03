import pygame
pygame.init()
from pyfiles.constants import TEXT_FONT as text_font, TEXT_COLOR, MENU_TEXT_FONT


fuel_text = MENU_TEXT_FONT.render("BOOST", False, TEXT_COLOR)
fuel_text_rect = fuel_text.get_rect(center = (310,690))


score_text = MENU_TEXT_FONT.render(f"WARPS", False, TEXT_COLOR)
score_text_rect = score_text.get_rect(center = (105, 635))



