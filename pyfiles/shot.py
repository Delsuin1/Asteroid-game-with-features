import pygame
from pyfiles.circleshape import CircleShape
from pyfiles.constants import SHOT_RADIUS, LINE_WIDTH, BOMB_RADIUS
from pyfiles.images import teleport_sprite1, teleport_rect1


class Shot(CircleShape):
    def __init__(self, x: float, y: float, shot_radius=SHOT_RADIUS) -> None:
        super().__init__(x, y, shot_radius)
        
        
        
    def draw(self, screen):
        # frame 7 for regular bullet
        # frame 10-11 for bomb
        # change white for the shot animation using the teleport animation
        screen.blit(teleport_sprite1[6], teleport_sprite1[10].get_rect(center = (self.position)))
        pygame.draw.circle(screen, "#3C8263", self.position, self.radius, LINE_WIDTH)
        
        
    def update(self, dt):
        self.position += self.velocity * dt
        
class Bomb(Shot):
    def __init__(self, x, y):
        super().__init__(x,y, BOMB_RADIUS) 
        self.bomb = True
    def draw(self, screen):
        # frame 6 for regular bullet
        # frame 10 for bomb
        screen.blit(teleport_sprite1[10], teleport_sprite1[10].get_rect(center = (self.position)))
        pygame.draw.circle(screen, "#3C8263", self.position, self.radius, LINE_WIDTH)
        
    def split(self):
        self.kill()
        for i in range(1, 8+1):
            angle = 40*i
            rotation = self.velocity.rotate(angle)
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = rotation / 2