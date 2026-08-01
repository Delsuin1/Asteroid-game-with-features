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
        self.velocity = pygame.Vector2(0, 2)
        self.radius = radius
        self.frame = 0

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass
    
    
    def collides_with(self, other) -> bool:
        if self.position.distance_to(other.position) <= self.radius + other.radius:
            if not other.is_immune():
                return True
        
        # create a small 10% percent chance for coliding asteroids to break into small objects
        return False
        
        