import pygame
from pyfiles.circleshape import CircleShape
from pyfiles.images import *
from pyfiles.animate import animate
from pyfiles.sounds import *
import random
from pyfiles.shot import Shot, Bomb, DoubleShot
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
    PLAYER_SHOOT_SPEED,
    SHOT_COOLDOWN_SECONDS,
    BOMB_COOLDOWN_SECONDS
)


class Player(CircleShape):
    def __init__(self, x: int, y: int, stamina, lives) -> None:
        super().__init__(x,y, PLAYER_RADIUS)
        self.__max_speed = PLAYER_SPEED
        self.__stamina = stamina
        self.rotation = 180
        self.accel = 0
        self.useable_stamina = stamina
        self.color = BAR_COLOR
        self.lives = lives
        self.last_collide_time = 0
        # results of animate file stuff
        self.frame2 = 0
        self.cooldown = 0
        self.skill = Shot

        
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def get_frame1(self, images, dt):
        if self.frame <= len(images):
            self.frame -= 14 * dt
          
          
        if self.frame <= -len(images):
            teleport_sound.play(fade_ms = random.randint(1100,1200))
            self.frame = 0.1
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
            self.immunity = True    
            # teleports player to a random area
            self.position.x = self.position.x + random.randint(-1000,1000)
            # Don't know why but I need to separate the x,y values otherwise the boundaries will bring up an error
            self.position.y = self.position.y + random.randint(-1000,1000)
            # for imunnity frames
            self.last_collide_time = pygame.time.get_ticks() 
            self.alive = False
            self.lives -= 1
            # player rotation resets to original
            self.rotation = 180
            
            self.accel = 0
            
            if self.lives <= 0:
                print("Game Over!")
                destruction_sound.play(fade_ms = random.randint(1100,1200))
                return False
            
            # create destruction sound
            teleport_sound.play(fade_ms = random.randint(1100,1200))
            # could use teleport_sound.set_volume(0.2)
        # return True or False for game_active: bool variable
        return True

    
    def teleport_animation(self, screen, dt, position):
        if not self.alive:
            self.alive = self.get_frame1(teleport_sprite1, dt)
            screen.blit(teleport_sprite1[int(self.frame)], teleport_rect1.get_rect(center = position))
        if self.frame == 0.1:
            alive = self.get_frame2(teleport_sprite2, dt)
            screen.blit(teleport_sprite2[int(-self.frame2)], teleport_rect2.get_rect(center = self.position))
            
            
        
    
    def draw(self, screen: pygame.Surface) -> None:
        if self.alive and self.frame2 == 0:
            shield_rect = shield_image.get_rect(center = self.position)
            player_shape = pygame.draw.polygon(screen, self.color, self.triangle(), LINE_WIDTH)
            if self.is_immune():
                self.color = "#596565"
                screen.blit(shield_image.convert_alpha(), shield_rect)
            else:
                self.color = BAR_COLOR
            
    def is_immune(self):
        delay = 3000
        
        seconds = pygame.time.get_ticks()
        if seconds - self.last_collide_time - delay < PLAYER_IMMUNITY_DURATION and not seconds < 5000:
            return True
        self.immunity = False
        return False
    
    def rotate(self, dt: float) -> None:
        rotation = 0
        rotation += 300 * dt
        # to make left and right movement slower
        friction = 0.9
        rotation *= friction
        self.rotation += rotation
        
    def shoot(self, type):
        projectile = DoubleShot(self.position.x, self.position.y)
        self.cooldown = projectile.cooldown
        shot_vector = pygame.Vector2(0,1)
        rotated_shot = shot_vector.rotate(self.rotation + random.randint(-10,10))
        shot_speed = rotated_shot * PLAYER_SHOOT_SPEED
        projectile.velocity = shot_speed
        
    def update(self, dt: float) -> None:
        time = False if self.immunity else True
        boost = False
        friction = 0.966
        self.in_boundary(LEFT, RIGHT, TOP, BOTTOM)
        if self.alive and self.frame == 0:
            keys = pygame.key.get_pressed()
            
            # friction will multiply by percent e.g. 0.95 which decreases velocity(gradual speed)
            if keys:
                if self.useable_stamina >= 0 :
                    if keys[pygame.K_LSHIFT] and keys[pygame.K_w]:
                        boost = True
                        self.useable_stamina -= 25 * dt
                    if boost:
                        self.accel += 100 * dt 
                    if keys[pygame.K_w]:
                        self.accel += 200 * dt
                        self.useable_stamina -= 5 * dt
                    if keys[pygame.K_a]:
                        self.rotate(-dt)
                    if keys[pygame.K_s]:
                        self.accel -= 200 * dt
                        self.useable_stamina -= 5 * dt
                    if keys[pygame.K_d]:
                        self.rotate(dt)
                    if keys[pygame.K_SPACE] and self.cooldown < 0 and time:
                        self.shoot(self.skill)
                
                    
                    # This should be gone once skill orb is fully functional
                    if keys[pygame.K_g] and self.cooldown < 0:
                        self.shoot(Bomb)
                        
                    # create a faster acceleration sprint feature
                    # create an animation that players behind the ship to make a bigger blast

                    # when boost equals False increase the stamina bar
            if not boost:
                self.useable_stamina += 20 * dt
                    
                # limits stamina by player stat
                if self.useable_stamina >= self.__stamina:
                    self.useable_stamina = self.__stamina
            if boost:
                self.__max_speed = PLAYER_SPEED + 100
            else:
                self.__max_speed = PLAYER_SPEED
            
            # this limits the speed
            if self.accel >= self.__max_speed:
                self.accel = self.__max_speed
            elif self.accel <= -self.__max_speed:
                self.accel = -self.__max_speed

            # to prevent negative scientific notation 
            if abs(self.accel) <= 0.6:
                self.accel = 0
            if self.accel != 0:
                self.move(dt)
            if not keys[pygame.K_w]:
                self.accel *= friction 
        self.cooldown -= dt
        if self.cooldown < 0:
            self.cooldown = - 0.1
            
            
    def move(self, dt) -> None:
        unit_vector = pygame.Vector2(0,self.accel)
        rotated_vector = unit_vector.rotate(self.rotation) 
        self.position += rotated_vector * dt 
        