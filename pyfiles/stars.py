import pygame
from pyfiles.circleshape import CircleShape
import random
from pyfiles.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Stars(CircleShape):
    def __init__(self, x, y, radius, player_position):
        super().__init__(x,y,radius)
        # might need to create a star class
        self.player_position = player_position.position
        self.stars: list[Star] = []
        self.colors = [

    "#FFFFFF",  # Pure White (Brightest)
    "#F7FDFF",  # White Star (Subtle Blue Glow)
    "#EFEFE8",  # Star White (Natural Starlight)
    "#FAFDEC",  # Diamond Star (Warm White)
    "#F8F7FF",  # Type F Star (Slightly Blue-White)
    "#FFF4EA",  # Type G Star (Sun-like Yellow-White)
    "#F0F8FF",  # Alice Blue (Cool Starlight)
    "#F8F8FF",  # Ghost White (Ethereal Glow)
    "#F0FFFF",  # Azure (Hot Blue-White Star)
    "#FFFACD",  # Lemon Chiffon (Warm Star)
    "#FFFAF0",  # Floral White (Soft Glow)
    "#F5F5F5",  # White Smoke (Distant Star)
    "#FAF9F6",  # Off White (Natural White)
    "#FCFCFC",  # Swan White (Clean White)
    "#F8F8F4",  # Vivid White (High Contrast)
    "#F4F5F0",  # Bright White (Crisp)
    "#F9F6EE",  # Bone White (Aged Starlight)
    "#FFFDD0",  # Cream (Yellowish Star)
    "#F0EAD6",  # Eggshell (Warm Glow)
    "#FDF5E6",  # Old Lace (Antique Star)
    "#FFE4E1",  # Misty Rose (Red Giant Hint)
    "#E0FFFF",  # Light Cyan (Blue Supergiant)
    "#F0FFF0",  # Honeydew (Greenish Tint)
    "#FFFFF0",  # Ivory (Classic Warm White)
    "#FFFAFA",  # Snow (Cool White)
    "#F8F9FA",  # Paper White (Matte Star)
    "#F1F2F3",  # Platinum (Metallic White)
    "#E8F4F8",  # Starlight Blue (Atmospheric)
    "#F5F9FF",  # Sky White (Daylight Star)
    "#FAFBFC"   # Cloud White (Soft Diffusion)
]   
 
        self.star_count = 4000
        self.radius = random.uniform(1,2)
        self.spawn_star()
       
        
        
        
        
    def draw(self, screen: pygame.Surface):
        
        for star in self.stars:
            pygame.draw.circle(screen, star.color, (star.position.x - self.player_position.x * 0.5, star.position.y - self.player_position.y * 0.5,), self.radius)
        

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

       
