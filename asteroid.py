import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.containers = ()

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vec1 = self.velocity.rotate(angle) * 1.2
            vec2 = self.velocity.rotate(-angle) * 1.2
            new_size = self.radius - ASTEROID_MIN_RADIUS
            astroid1 = Asteroid(self.position.x, self.position.y, new_size)
            astroid2 = Asteroid(self.position.x, self.position.y, new_size)
            astroid1.velocity = vec1
            astroid2.velocity = vec2
        self.kill()
        
    def draw(self, screen):
       pygame.draw.circle(screen, "brown", self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)