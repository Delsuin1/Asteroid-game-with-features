import pygame
from pyfiles.circleshape import CircleShape
from pyfiles.constants import SHOT_RADIUS, LINE_WIDTH, BOMB_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float, shot_radius=SHOT_RADIUS) -> None:
        super().__init__(x, y, shot_radius)
        
        
        
    def draw(self, screen):
        # change white for the shot animation using the teleport animation
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
        
    def update(self, dt):
        self.position += self.velocity * dt
        
class Bomb(Shot):
    def __init__(self, x, y):
        super().__init__(x,y, BOMB_RADIUS) 
        self.bomb = True

    def split(self):
        self.kill()
        for i in range(8):
            angle = 40*i
            rotation = self.velocity.rotate(angle)
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = rotation / 2