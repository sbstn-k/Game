from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, LINE_WIDTH, SHOT_RADIUS
from math import pi


import pygame


class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        


    def draw(self, surface):
        
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        # must override
        self.position = self.position + (self.velocity * dt)