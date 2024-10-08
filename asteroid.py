import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #print("new asteroid!")
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        #print("draw")
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        #print("update")
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector_a = self.velocity.rotate(-angle)
            vector_b = self.velocity.rotate(angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = vector_a * 1.2
            asteroid_b.velocity = vector_b * 1.2