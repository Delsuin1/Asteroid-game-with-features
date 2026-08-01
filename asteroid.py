import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH
from images import get_sprite_sheet, asteroid_sprite_sheet


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.frame = 0
        self.asteroid_sprite, self.asteroid_rect = get_sprite_sheet(asteroid_sprite_sheet, 8,8, self.radius*0.033, self.position)
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
        
        
        