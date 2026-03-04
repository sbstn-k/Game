from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, LINE_WIDTH, ASTEROID_MIN_RADIUS
from math import pi
from logger import log_event
import random
import pygame



class Asteroid(CircleShape):

    def __init__(self, x, y, radius):

        super().__init__(x, y, radius)


    def draw(self, surface):
        
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        # must override
        self.position = self.position + (self.velocity * dt)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        num = random.uniform(20, 50)

        first = self.velocity.rotate(num)
        second = self.velocity.rotate(-num)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_ast = Asteroid(self.position[0], self.position[1], new_radius)

        second_ast = Asteroid(self.position[0], self.position[1], new_radius)


        first_ast.velocity = first * 1.2
        second_ast.velocity = second * 1.2
