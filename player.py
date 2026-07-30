import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS, 
    LINE_WIDTH, 
    BOARDER_WIDTH,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_IMMUNITY_DURATION,
    BAR_COLOR
)



class Player(CircleShape):
    def __init__(self, x: int, y: int, stamina, lives) -> None:
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.speed = 0
        self.useable_stamina = stamina
        self.color = BAR_COLOR
        self.__stamina = stamina
        self.lives = lives
        self.last_collide_time = 0
        self.immunity_duration = PLAYER_IMMUNITY_DURATION
        

        
        # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        player_shape = pygame.draw.polygon(screen, self.color, self.triangle(), LINE_WIDTH)
        if self.is_immune():
            self.color = "grey"
        else:
            self.color = BAR_COLOR

    def is_immune(self):
        seconds = pygame.time.get_ticks() 
        if seconds - self.last_collide_time < self.immunity_duration:
            return True
        return False
    
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
    
    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys:
            if keys[pygame.K_w]:
                self.move(dt)
            if keys[pygame.K_a]:
                self.rotate(-dt)
            if keys[pygame.K_s]:
                self.move(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_LSHIFT] and keys[pygame.K_w] and self.useable_stamina > 0:
                self.move(dt*1.2)
                self.useable_stamina -= 80 * dt

                
            elif not keys[pygame.K_LSHIFT]:
                self.useable_stamina += 20 * dt

            if self.useable_stamina > self.__stamina:
                self.useable_stamina = self.__stamina
            
 
    
    def move(self, dt) -> None:
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_speed_vector = rotated_vector * PLAYER_SPEED * dt 
        self.position += rotated_speed_vector