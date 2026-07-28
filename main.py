import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, STARTING_POS, PLAYER_STAMINA
from logger import log_state
from images import background, background_rect
from player import Player
from text import stamina_text, stamina_text_rect, alternate_text_color
from gui import Gui

def main():

    pygame.init()
    pygame.display.set_caption("Asteroids", "A game about Asteroids!")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(STARTING_POS["x"], STARTING_POS["y"], PLAYER_STAMINA)
    clock = pygame.time.Clock()
    dt = 0.0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    hud = Gui()
    
    while True:
        log_state()
        index = alternate_text_color(dt, stamina_text)
    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Visual elements must go after otherwise it will be overridden
        
        player.update(dt)
   
        screen.fill("black")
        # Background images
        screen.blit(background, background_rect)
        screen.blit(stamina_text[int(index)], stamina_text_rect)
        hud.draw_ui(screen)
        
        
        player.draw(screen)
        print(player.useable_stamina)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
     
        
        

if __name__ == "__main__":
    main()
