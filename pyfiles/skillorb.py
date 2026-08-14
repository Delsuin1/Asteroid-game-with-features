import pygame
from pyfiles.circleshape import CircleShape
from pyfiles.shot import Shot
from pyfiles.constants import LEFT, RIGHT, TOP, BOTTOM
class SkillOrb(CircleShape):
    def __init__(self, x, y, radius, skill=Shot):
        super().__init__(x,y,radius)
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, "gold", self.position, self.radius)
    
    def update(self, dt):
        self.move(dt)
        self.in_boundary(LEFT, RIGHT, TOP, BOTTOM)
    
    
    def rotate(self, dt: float) -> None:
        rotation = 0
    
        # to make left and right movement slower
        self.rotation += rotation
        
    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(140)
        speed_rotated_vector = rotated_vector * 30 * dt
        self.position += speed_rotated_vector