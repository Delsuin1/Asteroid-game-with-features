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
        not self.in_boundary(LEFT-100, RIGHT+100, TOP-100, BOTTOM+100)
        
    def in_boundary(self, left, right, top, bottom):
        # Example: If player x coor is more than the screens width(1280),
        # reduce the player's x coordinate by the screens width returning the player to the opposite side of the screen(left side).
        
        # If the player goes in the opposite direction, check if the player is at x coor 0 if it is add the screen's width.
        # This places the player on the opposite side(right side).
        
        # Add padding so the player model completely leaves frame
        if self.position.x > right or self.position.x < left:
            self.kill()

        elif self.position.y > bottom or self.position.y < top:
            self.kill()

           
        
        


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
        asteroid_2 = Asteroid(self.position.x, self.position.y, asteroid_radius2)
    
        asteroid_1.velocity = asteroid_rotated_vector1 * 1.2
        asteroid_2.velocity = asteroid_rotated_vector2 * 1.2