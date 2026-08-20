import pygame
from pyfiles.circleshape import CircleShape
from pyfiles.constants import SHOT_RADIUS, LINE_WIDTH, BOMB_RADIUS
from pyfiles.images import teleport_sprite1, teleport_rect1
from math import sqrt
from pyfiles.constants import LEFT, RIGHT, TOP, BOTTOM, BOMB_COOLDOWN_SECONDS, SHOT_COOLDOWN_SECONDS, DOUBLESHOT_COOLDOWN_SECONDS

class Shot(CircleShape):
    def __init__(self, x: float, y: float, shot_radius=SHOT_RADIUS) -> None:
        super().__init__(x, y, shot_radius)
        # the position variables are where the shot began
        self.position_x = x
        self.position_y = y
        self.limit_range = False
        self.timer = 0
        self.cooldown = SHOT_COOLDOWN_SECONDS
        
        
    def draw(self, screen):
        # frame 6 for regular bullet

        screen.blit(teleport_sprite1[6], teleport_sprite1[10].get_rect(center = (self.position)))
        pygame.draw.circle(screen, "#3C8263", self.position, self.radius, LINE_WIDTH)

    
    def distance(self, position: tuple[list[int,int]], dt, range=2):
        # position is the current variable distance
        #this finds the radius of a circle 
        distance = sqrt((position.x - self.position_x) ** 2 + (position.y - self.position_y) ** 2) * dt
        if distance > range:
            self.kill()
        
    def in_boundary(self, left, right, top, bottom):
        
        # Add padding so the player model completely leaves frame
        if self.position.x > right:
            self.kill()
        elif self.position.x < left:
            self.kill()
        elif self.position.y > bottom:
            self.kill()
        elif self.position.y < top:
            self.kill()
            
    def update(self, dt):
        self.position += self.velocity * dt
        if self.limit_range:
            self.distance(self.position, dt)
        self.in_boundary(LEFT, RIGHT, TOP, BOTTOM)

# Rename wave shot
# work in progress
class WaveShot(Shot):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.cooldown = DOUBLESHOT_COOLDOWN_SECONDS
        self.limit_range = True
        self.immunity = True
        self.num = 0
        
    def draw(self, screen):
            # indicator
            pygame.draw.circle(screen, "#F12020", self.position, 20)
    def second_shot(self, dt):
        rotation = self.velocity.rotate(90) 
        shot = Shot(self.position.x - 50 , self.position.y)
        shot.limit_range = True
        shot.velocity = rotation * 100 * dt
        
        
    def update(self, dt):
        self.position += 0.4 * self.velocity.rotate(0) * dt
        if self.limit_range and self.timer < 3 and self.num < 500:
            self.num += 1
            self.second_shot(dt)
            self.timer += 1.5 * dt
        else:
            self.kill()










class BarrierShot(Shot):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.cooldown = DOUBLESHOT_COOLDOWN_SECONDS
        self.limit_range = True
        self.immunity = True
        self.num = 0
        
        
    def second_shot(self, dt, gap=2):
        # implement for loop to create a gap
        shot = Shot(self.position.x, self.position.y)
        shot.limit_range = True
        shot.distance(self.position, dt, 3)
        # this is the movement
        shot.velocity = self.velocity * 10 * dt
        
    def draw(self, screen):
        # indicator
        pygame.draw.circle(screen, "#F12020", self.position, 20)
        
        
    def update(self, dt):
        self.position += self.velocity * 1.5 * dt
        if self.limit_range and self.num < 10:
            self.distance(self.position, dt, 2.5)
            self.second_shot(dt)
            self.num+=1
            self.timer += 1 * dt
        if self.timer >= 5:
            self.kill()
  

    
class Bomb(Shot):
    def __init__(self, x, y):
        super().__init__(x,y, BOMB_RADIUS) 
        self.bomb = True
        self.cooldown = BOMB_COOLDOWN_SECONDS
        
        
    def update(self, dt):
        self.in_boundary(LEFT, RIGHT, TOP, BOTTOM)
        # .3 modifier to make it slower
        self.position += 0.3 * self.velocity * dt

    def draw(self, screen):
        # frame 10 for bomb
        screen.blit(teleport_sprite1[10], teleport_sprite1[10].get_rect(center = (self.position)))
        pygame.draw.circle(screen, "#3C8263", self.position, self.radius, LINE_WIDTH)
        
    def split(self):
        self.kill()
        for i in range(8):
            angle = 40*i
            rotation = self.velocity.rotate(angle) 
            shot = Shot(self.position.x, self.position.y)
            shot.limit_range = True
            shot.velocity = rotation / 8