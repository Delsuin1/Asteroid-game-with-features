import pygame
from pyfiles.circleshape import CircleShape
from pyfiles.shot import Shot, Bomb, BarrierShot, WaveShot
from pyfiles.constants import LEFT, RIGHT, TOP, BOTTOM, SCREEN_WIDTH, SCREEN_HEIGHT
import random

class SkillOrb(CircleShape):
    def __init__(self, x, y, radius, skill=Shot):
        super().__init__(x,y,radius)
        self.rotation = 0
        self.timer = False  
        self.time = 0
        self.skill = skill
        self.types = Shot, Bomb, BarrierShot
        
    def draw(self, screen):
        if self.skill == Shot:
            pygame.draw.circle(screen, "green", self.position, self.radius)
        elif self.skill == Bomb:
            pygame.draw.circle(screen, "gold", self.position, self.radius)
        elif self.skill == BarrierShot:
            pygame.draw.circle(screen, "blue", self.position, self.radius)
        elif self.skill == WaveShot:
            pygame.draw.circle(screen, "brown", self.position, self.radius)
            
    def update(self, dt):
        
        self.time += 1 * dt if self.timer == True else 0
        self.move(dt)
        self.in_boundary(LEFT, RIGHT, TOP, BOTTOM)
        self.rotate(dt)
        if self.time >= 2:
            self.kill()
            self.time = 0
            SkillOrb(random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), 40, random.choice(self.types))
            
    
    def rotate(self, dt: float) -> None:
    
        # to make left and right movement slower
        if self.rotation >= 360:
            self.rotation = 0
        self.rotation += 200 * dt
        
    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        speed_rotated_vector = rotated_vector * 30 * dt
        self.position += speed_rotated_vector