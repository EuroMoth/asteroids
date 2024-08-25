import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        print("new asteroid!")
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        print("draw")
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        print("update")