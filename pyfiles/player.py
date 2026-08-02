import pygame
from pyfiles.circleshape import CircleShape
from pyfiles.images import *
from pyfiles.animate import animate
import random
from pyfiles.constants import (
    PLAYER_RADIUS, 
    LINE_WIDTH, 
    BOARDER_WIDTH,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_IMMUNITY_DURATION,
    BAR_COLOR,
    LEFT,
    RIGHT,
    TOP,
    BOTTOM,
)


class Player(CircleShape):
    def __init__(self, x: int, y: int, stamina, lives) -> None:
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 180
        self.max_speed = PLAYER_SPEED
        self.accel = 0
        self.friction = 0.96
        self.useable_stamina = stamina
        self.color = BAR_COLOR
        self.__stamina = stamina
        self.lives = lives
        self.last_collide_time = 0
        self.immunity_duration = PLAYER_IMMUNITY_DURATION
        # results of animate file stuff
        self.explosion_sprite1, self.explosion_sprite1_rect = animate(explosion_sprite_sheet, 8,8, self.radius*0.05, self.position, 4 , 5)
        self.explosion_sprite2, self.explosion_sprite2_rect  = animate(explosion_sprite_sheet, 8,8, self.radius*0.05, self.position, 3 , 7)
        self.teleport_sound = pygame.mixer.Sound(random.choice(["audio/teleport.wav", "audio/teleport.wav"]))
        self.destruction_sound = pygame.mixer.Sound(random.choice(["audio/explode.wav", "audio/explodemini.wav"]))
        self.frame2 = 0
        # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def in_boundary(self, left, right, top, bottom):
        # Example: If player x coor is more than the screens width(1280),
        # reduce the player's x coordinate by the screens width returning the player to the opposite side of the screen(left side).
        
        # If the player goes in the opposite direction, check if the player is at x coor 0 if it is add the screen's width.
        # This places the player on the opposite side(right side).
        
        # Add padding so the player model completely leaves frame
        if self.position.x > right:
            self.position.x -= right
        elif self.position.x < left:
            self.position.x += right
        elif self.position.y > bottom:
            self.position.y -= bottom
        elif self.position.y < top:
            self.position.y += bottom

    def get_frame1(self, images, dt):
        if self.frame <= len(images):
            self.frame -= 14 * dt
          
          
        if self.frame <= -len(images) or self.frame >= len(images):
            self.frame = 0.1
            self.teleport_sound.play(fade_ms = random.randint(1100,1200))
            return True
        return False

    def get_frame2(self, images, dt):
        if self.frame2 <= len(images):
            self.frame2 -= 15 * dt
            
        if self.frame2 <= -len(images):
            self.frame2 = 0 
            self.frame = 0

    
    def destroyed(self, game_active):
        if game_active:
            
            # for imunnity frames
            self.last_collide_time = pygame.time.get_ticks() 
            # create destruction sound
            # find out how to reduce volume and change timing of sound
            self.alive = False
            # could use teleport_sound.set_volume(0.2)
            self.lives -= 1
            
            # play explosion animation 
                
            # Returns player to center
            self.position.x = X
            # Don't know why but I need to separate the x,y values otherwise the boundaries will bring up an error
            self.position.y = Y
            # player rotation resets to original
            self.rotation = 180
            
            self.accel = 0
            
            if self.lives <= 0:
                print("Game Over!")
                self.destruction_sound.play(fade_ms = random.randint(1100,1200))
                return False
            else:
                self.teleport_sound.play(fade_ms = random.randint(1100,1200))
            # return True or False for game_active: bool variable
        return True

    
    def shot_animation(self, screen, dt, position):
    
        if not self.alive:
            self.alive = self.get_frame1(self.explosion_sprite1, dt)
            screen.blit(self.explosion_sprite1[int(self.frame)], self.explosion_sprite1_rect.get_rect(center = position))
        if self.frame == 0.1:
            alive = self.get_frame2(self.explosion_sprite2, dt)
            screen.blit(self.explosion_sprite2[int(-self.frame2)], self.explosion_sprite2_rect.get_rect(center = (X,Y)))
            
            
        
    
    def draw(self, screen: pygame.Surface) -> None:
        if self.alive and self.frame2 == 0:
            shield_rect = shield_image.get_rect(center = self.position)
            player_shape = pygame.draw.polygon(screen, self.color, self.triangle(), LINE_WIDTH)
            if self.is_immune():
                self.color = "grey"
                screen.blit(shield_image.convert_alpha(), shield_rect)
            else:
                self.color = BAR_COLOR
            
    def is_immune(self):
        delay = 3000
        seconds = pygame.time.get_ticks()
        if seconds - self.last_collide_time - delay < self.immunity_duration and not seconds < 5000:
            return True
        return False
    
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
    
    
    def update(self, dt: float) -> None:
        self.in_boundary(LEFT, RIGHT, TOP, BOTTOM)
        if self.alive and self.frame == 0:
            boost = False
            self.accel *= self.friction
            
            keys = pygame.key.get_pressed()
            
            # friction will multiply by percent e.g. 0.95 which decreases velocity(gradual speed)
            if keys:
                if self.useable_stamina >= 0 :
                    if keys[pygame.K_LSHIFT] and keys[pygame.K_w]:
                        boost = True
                        self.useable_stamina -= 25 * dt
                    if boost:
                        self.accel += 10 
                    if keys[pygame.K_w]:
                        self.accel += 10
                        self.useable_stamina -= 5 * dt
                    if keys[pygame.K_a]:
                        self.rotate(-dt)
                    if keys[pygame.K_s]:
                        self.accel -= 20
                        self.useable_stamina -= 5 * dt
                    if keys[pygame.K_d]:
                        self.rotate(dt)
                    # create a faster acceleration sprint feature
                    # create an animation that players behind the ship to make a bigger blast

                    # when boost equals False increase the stamina bar
            if not boost:
                self.useable_stamina += 20 * dt
                    
                # limits stamina by player stat
                if self.useable_stamina >= self.__stamina:
                    self.useable_stamina = self.__stamina
            if boost:
                self.max_speed = PLAYER_SPEED + 100
            else:
                self.max_speed = PLAYER_SPEED
            
            
            # this limits the speed
            if self.accel >= self.max_speed:
                self.accel = self.max_speed
            elif self.accel <= -self.max_speed:
                self.accel = -self.max_speed

            # to prevent negative scientific notation 
            if abs(self.accel) <= 0.1:
                self.accel = 0
            if self.accel != 0:
                self.move(dt)

                
    def move(self, dt) -> None:
        unit_vector = pygame.Vector2(0,self.accel)
        rotated_vector = unit_vector.rotate(self.rotation) 
        self.position += rotated_vector * dt 
        