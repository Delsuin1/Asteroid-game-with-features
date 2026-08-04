import pygame
from pyfiles.images import *
from pyfiles.constants import *
from pyfiles.logger import log_state, log_event
from pyfiles.player import Player as Player
from pyfiles.hud import Hud
from pyfiles.asteroid import Asteroid
from pyfiles.asteroidfield import AsteroidField
from pyfiles.sounds import background_music
from pyfiles.shot import Shot, Bomb
from sys import exit as leave
import random



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
    shots = pygame.sprite.Group()
    gui = pygame.sprite.Group()
    
    bgm = pygame.mixer.music.load(background_music)
    pygame.mixer.music.set_volume(0.14)
    pygame.mixer.music.play(-1)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    Bomb.containers = (shots, drawable, updatable)
    Hud.containers = (gui)


    player = Player(X, Y, PLAYER_STAMINA, PLAYER_LIVES)
    asteroid_field = AsteroidField()
    hud = Hud(player)

                
            
    
    def restart():
        player = Player(X,Y, PLAYER_STAMINA, PLAYER_LIVES)
        asteroid_field = AsteroidField()
        hud = Hud(player)
        return player, asteroid_field, hud
    

    collide_position = [X,Y]
    
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
                        updatable.empty() 
                        drawable.empty()
                        asteroids.empty()
                        player, asteroid_field, hud = restart()
                        game_active = True
                    
        log_state()
        if game_active:
            # Visual elements must go after otherwise it will be overridden


            # Background images
            updatable.update(dt)
            screen.fill("black")
            screen.blit(background, background_rect)


            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    collide_position = player.position.x, player.position.y
                    game_active = player.destroyed(game_active)


            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collides_with(shot):
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()
                        if hasattr(shot, "bomb"):
                            shot.split()
            player.teleport_animation(screen, dt, collide_position)
            for drawables in drawable:
                drawables.draw(screen)
            hud.draw(screen)


                       
            pygame.display.flip()
            dt = clock.tick(60) / 1000
            
        else:
            screen.blit(background, background_rect)
            for asteroid in asteroids:
                asteroid.draw(screen)
            draw_text("Press SPACE to start", MENU_TEXT_FONT, TEXT_COLOR, X,300)
            draw_text("Press Q to stop", MENU_TEXT_FONT, TEXT_COLOR, X,350)
            draw_text("YOUR SCORE", MENU_TEXT_FONT, TEXT_COLOR, 1024,150)
            player.lives = PLAYER_LIVES
          
            
            pygame.display.flip()
            
            
        
            
            

if __name__ == "__main__":
    main()
