import pygame
from pyfiles.images import *
from pyfiles.constants import *
from pyfiles.logger import log_state, log_event
from pyfiles.player import Player as Player
from pyfiles.hud import Hud
from pyfiles.asteroid import Asteroid
from pyfiles.asteroidfield import AsteroidField
from pyfiles.sounds import background_music
from pyfiles.shot import *
from pyfiles.skillorb import SkillOrb
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
    orbs = pygame.sprite.Group()
    
    bgm = pygame.mixer.music.load(background_music)
    pygame.mixer.music.set_volume(0.14)
    pygame.mixer.music.play(-1)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    Hud.containers = (gui)
    SkillOrb.containers = (updatable, drawable, orbs)

    weapon_types = [Shot, Bomb, BarrierShot, WaveShot]
    
    player = Player(X, Y, PLAYER_STAMINA, PLAYER_LIVES)
    asteroid_field = AsteroidField()
    orb = SkillOrb(random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), 40, random.choice(weapon_types)) 
    hud = Hud(player)
    
    score_dict = {
        "max" : 0,
        "med" : 0,
        "min" : 0,
                  }
            
    collide_position = [X,Y]
    
    def restart():
        player = Player(X,Y, PLAYER_STAMINA, PLAYER_LIVES)
        asteroid_field = AsteroidField()
        hud = Hud(player)
        orb = SkillOrb(random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), 40, random.choice(weapon_types))

        return player, asteroid_field, hud, orb
    
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
            # Keys to be removed if ever released as a public build or something
                if event.key == pygame.K_j:    
                    player.skill = BarrierShot
                if event.key == pygame.K_k:
                    player.skill = WaveShot   
                if event.key == pygame.K_l:  
                    player.skill = Bomb                 
            if not game_active:
                if event.type == pygame.KEYDOWN:               
                    if event.key == pygame.K_SPACE:
                        # add a way to save the information after next round
                        
                        # emptys the groups so it clears the screen
                        score_dict = dict.fromkeys(score_dict, 0)
                        updatable.empty() 
                        drawable.empty()
                        asteroids.empty()
                        orbs.empty()
                        player, asteroid_field, hud, orb = restart()
                        
                        game_active = True
                    
        log_state()
        if game_active:
            # Visual elements must go after otherwise it will be overridden


            # Background images
            updatable.update(dt)
            screen.fill("black")
            screen.blit(background, background_rect)
            
            
            
            for orb in orbs:
       
                if orb.collides_with(player):
                    orb.timer = True
                    
                    player.skill = orb.skill
                    
                    
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    collide_position = player.position.x, player.position.y
                    game_active = player.destroyed(game_active)


            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collides_with(shot):
                        asteroid.immunity = True
                        log_event("asteroid_shot")
                        if asteroid.radius >= ASTEROID_MAX_RADIUS:
                            score_dict["max"] += ASTEROID_MAX_POINTS
                        elif asteroid.radius >= ASTEROID_MIN_RADIUS * 2:
                            score_dict["med"] += ASTEROID_MED_POINTS
                        else:
                            score_dict["min"] += ASTEROID_MIN_POINTS    
                        
                        asteroid.split()
                        if hasattr(shot, "bomb"):
                            shot.split()
                        else:
                            shot.kill()
                            
                            
            player.teleport_animation(screen, dt, collide_position)
            for drawables in drawable:
                drawables.draw(screen)
            hud.draw(screen)
            # draw to hud screen

            draw_text(f"{score_dict["max"] + score_dict["med"] + score_dict["min"]}", MENU_TEXT_FONT, TEXT_COLOR, 1200,40)

                       
            
            
            
        else:
            screen.blit(background, background_rect)
            draw_text("Press SPACE to start", MENU_TEXT_FONT, TEXT_COLOR, X,300)
            draw_text("Press Q to stop", MENU_TEXT_FONT, TEXT_COLOR, X,350)
            max, medium, min = score_dict.values()
            draw_text(f"YOUR SCORE", MENU_TEXT_FONT, TEXT_COLOR, 1024,150)
            # print(f"{max}\n{medium}\n{min}")
            draw_text(f"{score_dict["max"], score_dict["med"], score_dict["min"]}", MENU_TEXT_FONT, TEXT_COLOR, 1024,250)
            draw_text(f"{score_dict["max"] + score_dict["med"] + score_dict["min"]}", MENU_TEXT_FONT, TEXT_COLOR, 1024,200)
            
                
          
        dt = clock.tick(60) / 1000  
        pygame.display.flip()
        
            
            

if __name__ == "__main__":
    main()
