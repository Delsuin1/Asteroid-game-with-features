import pygame
from constants import *
from logger import log_state, log_event
from images import *
from player import Player
from hud import Hud
from asteroid import Asteroid
from asteroidfield import AsteroidField
from sys import exit as leave
import random
from sounds import background_music



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # move to menu module
    def draw_text(text, font, text_color, x, y):
        style = font.render(text, False, text_color)
        style_rect = style.get_rect(center = (x,y))
        screen.blit(style, style_rect)
    
    
    pygame.init()
    pygame.display.set_caption("Asteroids", "A game about Asteroids!")
    game_active = False
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    gui = pygame.sprite.Group()
    
    bgm = pygame.mixer.music.load(background_music)
    pygame.mixer.music.set_volume(0.14)
    pygame.mixer.music.play(-1)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Hud.containers = (gui, updatable, drawable)

    player = Player(X, Y, PLAYER_STAMINA, PLAYER_LIVES)
    asteroid_field = AsteroidField()
    hud = Hud(player)
    
    def restart():
        player = Player(X,Y, PLAYER_STAMINA, PLAYER_LIVES)
        asteroid_field = AsteroidField()
        hud = Hud(player)
        return player, asteroid_field, hud
    explosions_path = ["explosions/explode.wav", "explosions/explodemini.wav"]
    current_frame = 0
    frame_counter = 0
    
    clock = pygame.time.Clock()
    dt = 0.0
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                leave()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or not game_active:
                    updatable.empty() 
                    drawable.empty()
                    asteroids.empty()
                    player, asteroid_field, hud = restart()
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
                    destruction_sound.play(fade_ms = random.randint(1000,1100))
                    player.lives -= 1
                    
                    # play explosion animation 
                    
                    player.position.x = X
                    player.position.y = Y

                    if player.lives <= 0:
                        print("Game Over!")
                        game_active = False


            # Background images
            screen.fill("black")
            backgrounds = pygame.transform.rotozoom(background, int(player.useable_stamina) * dt, 1)
            screen.blit(backgrounds, background_rect)
            frame_speed = 15
            
            frame_counter += 1
            if frame_counter >= frame_speed:
                current_frame += 1

            for drawables in drawable:
                drawables.draw(screen)
                       
            pygame.display.flip()
            dt = clock.tick(60) / 1000
            print(dt)
        else:
            screen.blit(background, background_rect)
            
            draw_text("Press SPACE to start", MENU_TEXT_FONT, TEXT_COLOR, X,300)
            draw_text("Press Q to stop", MENU_TEXT_FONT, TEXT_COLOR, X,350)
            draw_text("YOUR SCORE", MENU_TEXT_FONT, TEXT_COLOR, 1024,150)
            player.lives = PLAYER_LIVES
          
            
            pygame.display.flip()
            
            
        
            
            

if __name__ == "__main__":
    main()
