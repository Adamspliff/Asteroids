from circleshape import CircleShape
from constants import *
import pygame


class Shot(CircleShape):
    def __init__(self, x, y , radius):

        position = pygame.Vector2(x,y)

        super().__init__(position.x, position.y, radius)
        

    def draw(self, screen):

        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += (self.velocity * dt)

