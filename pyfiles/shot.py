import pygame
from pyfiles.circleshape import CircleShape
from pyfiles.constants import SHOT_RADIUS, LINE_WIDTH, BOMB_RADIUS
from pyfiles.images import teleport_sprite1, teleport_rect1
from math import sqrt

class Shot(CircleShape):
    def __init__(self, x: float, y: float, shot_radius=SHOT_RADIUS) -> None:
        super().__init__(x, y, shot_radius)
        # the position variables are where the shot began
        self.position_x = x
        self.position_y = y
        self.limit_range = False
        
        
    def draw(self, screen):
        # frame 6 for regular bullet

        screen.blit(teleport_sprite1[6], teleport_sprite1[10].get_rect(center = (self.position)))
        pygame.draw.circle(screen, "#3C8263", self.position, self.radius, LINE_WIDTH)

    
    def distance(self, position: tuple[list[int,int]], dt):
        # position is the current variable distance
        distance = sqrt((position.x - self.position_x) ** 2 + (position.y - self.position_y) ** 2) * dt
        if distance > 5:
            self.kill()

    def update(self, dt):
        self.position += self.velocity * dt
        if self.limit_range:
            self.distance(self.position, dt)
        
class Bomb(Shot):
    def __init__(self, x, y):
        super().__init__(x,y, BOMB_RADIUS) 
        self.bomb = True
        
    def update(self, dt):
        self.position += 0.3 * self.velocity * dt
        
    def draw(self, screen):
        # frame 10 for bomb
        screen.blit(teleport_sprite1[10], teleport_sprite1[10].get_rect(center = (self.position)))
        pygame.draw.circle(screen, "#3C8263", self.position, self.radius, LINE_WIDTH)
        
    def split(self):
        self.kill()
        for i in range(1, 8+1):
            angle = 40*i
            rotation = self.velocity.rotate(angle) 
            shot = Shot(self.position.x, self.position.y)
            shot.limit_range = True
            shot.velocity = rotation / 8