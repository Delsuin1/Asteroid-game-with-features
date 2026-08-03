import pygame
from pyfiles.circleshape import CircleShape
from pyfiles.constants import SHOT_RADIUS
class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        
        
    def draw(self, screen):
        # change white for the shot animation using the teleport animation
        pygame.draw.circle(screen, "white", self.position, self.radius) #LineWidth)
        
        
    def update(self, dt):
        self.position += self.velocity * dt