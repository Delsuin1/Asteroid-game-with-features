import pygame
from constants import *
from logger import log_state, log_event
from images import background, background_rect
from player import Player
from hud import Hud
from asteroid import Asteroid
from asteroidfield import AsteroidField
from sys import exit as leave



def main():
    game_active = False
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    def draw_text(text, font, text_color, x, y):
        style = font.render(text, False, text_color)

    
    draw_text("Press SPACE to start", TEXT_FONT, TEXT_COLOR, 100,400)
    
    pygame.init()
    pygame.display.set_caption("Asteroids", "A game about Asteroids!")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    
    drawable = pygame.sprite.Group()
    
    asteroids = pygame.sprite.Group() 
    
    gui = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Hud.containers = (gui, updatable, drawable)
    
    

    player = Player(x, y, PLAYER_STAMINA, PLAYER_LIVES)
    asteroid_field = AsteroidField()
    hud = Hud(player)
  
   
    
    clock = pygame.time.Clock()
    dt = 0.0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                leave()
            if not game_active:
                if event.type == pygame.KEYDOWN:
                    game_active = True
        log_state()
                
        if game_active:
                
            # Visual elements must go after otherwise it will be overridden
            updatable.update(dt)
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    player.lives -= 1
                    # add immunity frames
                    player.last_collide_time = pygame.time.get_ticks() 
                    
                    # play an animation
                    player.position.x = x
                    player.position.y = y
                    
                    
    
                    if player.lives <= 0:
                        print("Game Over!")
                        game_active = False
            
            # print("invulurnable if 1500ms ",pygame.time.get_ticks() - player.last_collide_time, player.is_immune())
            # print(f"player lives: {player.lives}")
                
            # Background images
            screen.fill("black")
            screen.blit(background, background_rect)
            
            for drawables in drawable:
                drawables.draw(screen)
                
            pygame.display.flip()
            dt = clock.tick(60) / 1000
        else:
            player.lives = PLAYER_LIVES
            screen.blit(background, background_rect)
          
            
          
            pygame.display.flip()
            
            
        
            
            

if __name__ == "__main__":
    main()
