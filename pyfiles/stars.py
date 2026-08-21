import pygame
from pyfiles.circleshape import CircleShape
import random
from pyfiles.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Stars(CircleShape):
    def __init__(self, x, y, radius, player_position):
        super().__init__(x,y,radius)
        # might need to create a star class
        self.player_position = player_position
        self.stars: list[Star] = []
        self.colors = ["blue4", "darkslateblue", "gray48", "gray40", "orangered4", "black", "white"]
        self.star_count = 1000
        self.radius = 2
        self.spawn_star()
       
        
        
        
        
    def draw(self, screen: pygame.Surface):
        for star in self.stars:
            pygame.draw.circle(screen, star.color, (star.position.x - self.player_position.x , star.position.y - self.player_position.y,), self.radius)
                

    def spawn_star(self):
        i = 0
        while i < self.star_count:
            self.stars.append(Star(random.randint(0,SCREEN_WIDTH*2), random.randint(0, SCREEN_HEIGHT*2), random.choice(self.colors), self.radius))
            i += 1
            
            
class Star(CircleShape):
    def __init__(self, x: float, y: float, colors: str, radius: int) -> None:
        super().__init__(x,y, radius)
        self.x = x
        self.y = y
        self.color = colors

       
