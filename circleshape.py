import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # Checks if this circle has collided with another
    # Returns true if there is a collison
    def collision_check (self, other_circle: 'CircleShape'):
        distance = self.position.distance_to(other_circle.position)
        total_radius = self.radius + other_circle.radius
        if distance > total_radius:
            return False
        else:
            return True