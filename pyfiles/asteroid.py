import pygame
from pyfiles.circleshape import CircleShape
from pyfiles.constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, LEFT, RIGHT, TOP, BOTTOM
from pyfiles.images import asteroid_sprite_sheet
from pyfiles.animate import animate
from pyfiles.logger import log_event
import random



class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.frame = 0
        # keep sprite in asteroid as radius is variable
        self.asteroid_sprite, self.asteroid_rect = animate(asteroid_sprite_sheet, 8,8, self.radius*0.033, 5,5)
        self.asteroid_frame = 0
        
        
    def draw(self, screen):
        screen.blit(self.asteroid_sprite[int(self.frame)], self.asteroid_rect.get_rect(center = self.position))
        # pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)
    
    
    def get_frame(self, images, dt):
        self.frame += 12 * dt
        if self.frame >= len(images):
            self.frame = 0
         
        
    def update(self, dt) -> None:
        self.asteroid_frame = self.get_frame(self.asteroid_sprite, dt)     
        self.position += self.velocity * dt
        self.in_boundary(LEFT, RIGHT, TOP, BOTTOM)
        
        
        
        


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20,50)
        asteroid_rotated_vector1 = self.velocity.rotate(rand_angle)
        asteroid_rotated_vector2 = self.velocity.rotate(-rand_angle)
        asteroid_radius1 = self.radius - ASTEROID_MIN_RADIUS
        asteroid_radius2 = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, asteroid_radius1)
        asteroid_2 = Asteroid(self.position.x, self.position.y,                 asteroid_radius2)

        asteroid_1.velocity = asteroid_rotated_vector1 * 1.2
        asteroid_2.velocity = asteroid_rotated_vector2 * 1.2