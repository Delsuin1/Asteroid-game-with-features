import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.alive = True
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.frame = 0
        self.immunity = False
        
        
    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass


    def in_boundary(self, left, right, top, bottom):
        # Example: If player x coor is more than the screens width(1280),
        # reduce the player's x coordinate by the screens width returning the player to the opposite side of the screen(left side).
        
        # If the player goes in the opposite direction, check if the player is at x coor 0 if it is add the screen's width.
        # This places the player on the opposite side(right side).
        
        # Add padding so the player model completely leaves frame
        if self.position.x > right:
            self.position.x -= right
        elif self.position.x < left:
            self.position.x += right
        elif self.position.y > bottom:
            self.position.y -= bottom
        elif self.position.y < top:
            self.position.y += bottom
    
    
    def collides_with(self, other) -> bool:
        if self.position.distance_to(other.position) <= self.radius + other.radius:
            if not other.immunity:
                return True
        
        # create a small 10% percent chance for coliding asteroids to break into small objects
        return False
        
        