import pygame
import math
from pygame import sprite
from pygame import Vector2
from pygame import math


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
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, circleshape):
        
        if pygame.math.Vector2.distance_to(self.position, circleshape.position) < self.radius + circleshape.radius:
            return True
        
        else:
            return False