import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, STARTING_POS, PLAYER_STAMINA
from logger import log_state
from images import background, background_rect
from player import Player
from hud import Hud

def main():

    pygame.init()
    pygame.display.set_caption("Asteroids", "A game about Asteroids!")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Hud.containers = (updatable, drawable)
    
    
    player = Player(STARTING_POS["x"], STARTING_POS["y"], PLAYER_STAMINA)
    hud = Hud(player)
    
    clock = pygame.time.Clock()
    dt = 0.0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Visual elements must go after otherwise it will be overridden
        updatable.update(dt)
    
        # Background images
        screen.fill("black")
        screen.blit(background, background_rect)
        
        for drawables in drawable:
            drawables.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
        
     
        
        

if __name__ == "__main__":
    main()
