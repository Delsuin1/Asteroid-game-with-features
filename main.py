import pygame
from constants import *
from logger import log_state, log_event
from images import background, background_rect
from player import Player
from hud import Hud
from asteroid import Asteroid
from asteroidfield import AsteroidField
from sys import exit as leave
import random



def main():
    game_active = False
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    def draw_text(text, font, text_color, x, y):
        style = font.render(text, False, text_color)
        screen.blit(style, (x,y))
    
    
    
    
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
  
   
    explosions_path = ["explosions/explode.wav", "explosions/explodemini.wav"]
    
    
    clock = pygame.time.Clock()
    dt = 0.0
    
    
    
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                leave()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_active = False
                    
                    
                    
                if not game_active:
                    if event.key == pygame.K_SPACE:
                        game_active = True
                    
        log_state()
                
        if game_active:
                
            # Visual elements must go after otherwise it will be overridden
            updatable.update(dt)
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    # add immunity frames
                    player.last_collide_time = pygame.time.get_ticks() 
                    # create destruction sound
                    destruction_sound = pygame.mixer.Sound(random.choice(explosions_path))
                    # reduce volume and timing of sound
                    # could use destruction_sound.set_volume(0.2)
                    destruction_sound.play(fade_ms = random.randint(800,1100))
                    player.lives -= 1
                    
                    # play explosion animation 
                    
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
            
            screen.blit(background, background_rect)
            
            draw_text("Press SPACE to start", MENU_TEXT_FONT, TEXT_COLOR, 400,300)
            draw_text("Press Q to stop", MENU_TEXT_FONT, TEXT_COLOR, 450,350)
            player.lives = PLAYER_LIVES
          
            
          
            pygame.display.flip()
            
            
        
            
            

if __name__ == "__main__":
    main()
