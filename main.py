import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from images import background, background_rect

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids", "A game about Asteroids!")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        screen.blit(background, background_rect)
        pygame.display.flip()
        
        
        

if __name__ == "__main__":
    main()
