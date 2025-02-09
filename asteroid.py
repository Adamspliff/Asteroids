from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y , radius):

        position = pygame.Vector2(x,y)

        super().__init__(position.x, position.y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_velo_1 = self.velocity.rotate(random_angle)
            new_velo_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_velo_1*1.2
            new_asteroid_2.velocity = new_velo_2*1.2

    def draw(self, screen):

        pygame.draw.circle(screen, (random.choices(range(256), k=3)), self.position, self.radius, 2)


    def update(self, dt):

        self.position += (self.velocity * dt)

