import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH
from images import get_sprite_sheet


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float, sprite_sheet, rows, col) -> None:
        super().__init__(x, y, radius)
        self.sprite_sheet = sprite_sheet
        self.frame = 0
        self.sprite, self.frame_rect = get_sprite_sheet(self.sprite_sheet, rows, col, self.radius*0.033, self.position)
        
        
    def draw(self, screen):
        
        screen.blit(self.sprite[int(self.frame)], self.frame_rect.get_rect(center = self.position))
        # pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)
    
    
    def get_frame(self, images, dt):
        self.frame += 12 * dt
        if self.frame >= len(images):
            self.frame = 0
        
        
    def update(self, dt) -> None:
        self.position += self.velocity * dt
        self.get_frame(self.sprite, dt)