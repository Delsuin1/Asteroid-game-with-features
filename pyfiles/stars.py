import pygame
from pyfiles.circleshape import CircleShape
import random
from pyfiles.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Stars(CircleShape):
    def __init__(self, x, y, radius, player_position):
        super().__init__(x,y,radius)
        # might need to create a star class
        self.player = player_position
        self.stars: list[Star] = []
        self.colors = [

    "#B2B2B2",  # Pure White (Brightest)
    "#ADB1B2",  # White Star (Subtle Blue Glow)
    "#A7A7A2",  # Star White (Natural Starlight)
    "#AFB1A5",  # Diamond Star (Warm White)
    "#AEADB2",  # Type F Star (Slightly Blue-White)
    "#B2ABA4",  # Type G Star (Sun-like Yellow-White)
    "#A8AEB2",  # Alice Blue (Cool Starlight)
    "#AEAEB2",  # Ghost White (Ethereal Glow)
    "#A8B2B2",  # Azure (Hot Blue-White Star)
    "#B2AF8F",  # Lemon Chiffon (Warm Star)
    "#B2AFA8",  # Floral White (Soft Glow)
    "#ACACAC",  # White Smoke (Distant Star)
    "#AFAEAC",  # Off White (Natural White)
    "#B0B0B0",  # Swan White (Clean White)
    "#AEAEAB",  # Vivid White (High Contrast)
    "#ABACA8",  # Bright White (Crisp)
    "#AEACA7",  # Bone White (Aged Starlight)
    "#B2B192",  # Cream (Yellowish Star)
    "#A8A496",  # Eggshell (Warm Glow)
    "#B1ACA1",  # Old Lace (Antique Star)
    "#B2A09E",  # Misty Rose (Red Giant Hint)
    "#9DB2B2",  # Light Cyan (Blue Supergiant)
    "#A8B2A8",  # Honeydew (Greenish Tint)
    "#B2B2A8",  # Ivory (Classic Warm White)
    "#B2AFAF",  # Snow (Cool White)
    "#AEAFAF",  # Paper White (Matte Star)
    "#A9AAAA",  # Platinum (Metallic White)
    "#A3ABAE",  # Starlight Blue (Atmospheric)
    "#ACADB2",  # Sky White (Daylight Star)
    "#AFB0B0",   # Cloud White (Soft Diffusion)   
    "#7D7D7D",  # Pure White (Brightest)
    "#797C7D",  # White Star (Subtle Blue Glow)
    "#757571",  # Star White (Natural Starlight)
    "#7B7C74",  # Diamond Star (Warm White)
    "#7A797D",  # Type F Star (Slightly Blue-White)
    "#7D7873",  # Type G Star (Sun-like Yellow-White)
    "#767A7D",  # Alice Blue (Cool Starlight)
    "#7A7A7D",  # Ghost White (Ethereal Glow)
    "#767D7D",  # Azure (Hot Blue-White Star)
    "#7D7B64",  # Lemon Chiffon (Warm Star)
    "#7D7B76",  # Floral White (Soft Glow)
    "#787878",  # White Smoke (Distant Star)
    "#7B7A78",  # Off White (Natural White)
    "#7B7B7B",  # Swan White (Clean White)
    "#7A7A78",  # Vivid White (High Contrast)
    "#787876",  # Bright White (Crisp)
    "#7A7875",  # Bone White (Aged Starlight)
    "#7D7C66",  # Cream (Yellowish Star)
    "#767369",  # Eggshell (Warm Glow)
    "#7C7871",  # Old Lace (Antique Star)
    "#7D706F",  # Misty Rose (Red Giant Hint)
    "#6E7D7D",  # Light Cyan (Blue Supergiant)
    "#767D76",  # Honeydew (Greenish Tint)
    "#7D7D76",  # Ivory (Classic Warm White)
    "#7D7B7B",  # Snow (Cool White)
    "#7A7B7B",  # Paper White (Matte Star)
    "#767777",  # Platinum (Metallic White)
    "#72787A",  # Starlight Blue (Atmospheric)
    "#78797D",  # Sky White (Daylight Star)
    "#7B7B7B",   # Cloud White (Soft Diffusion)   
]   
 
        self.star_count = 4000
        self.radius = random.uniform(1,2)
        self.spawn_star()
       
        
        
        
        
    def draw(self, screen: pygame.Surface):
        
        for star in self.stars:
            pygame.draw.circle(screen, star.color, (star.position.x - self.player.position.x * .5 , star.position.y - self.player.position.y * .5), self.radius)


    def spawn_star(self):
        i = 0
        while i < self.star_count:
            self.stars.append(Star(random.randint(-640,SCREEN_WIDTH*2), random.randint(-640, SCREEN_HEIGHT*2), random.choice(self.colors), self.radius))
            i += 1
            
            
class Star(CircleShape):
    def __init__(self, x: float, y: float, colors: str, radius: int) -> None:
        super().__init__(x,y, radius)
        self.x = x
        self.y = y
        self.color = colors

       
