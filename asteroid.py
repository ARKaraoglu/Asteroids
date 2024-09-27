import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius= radius

    def draw(self, screen):
       pygame.draw.circle(surface = screen, color = "white", center = (self.position.x, self.position.y), radius = self.radius, width = 2)

    def update(self, dt):
       self.position += (self.velocity * dt)

    def split(self):
      self.kill()
      if self.radius == ASTEROID_MIN_RADIUS: 
         return
      else:
         angle = random.uniform(20, 50)
         v1 = self.velocity.rotate(angle)
         v2 = self.velocity.rotate(-angle)
         newAsteroidsRadius = self.radius - ASTEROID_MIN_RADIUS
         
         smallerAst1 = Asteroid(self.position.x, self.position.y, newAsteroidsRadius)
         smallerAst2 = Asteroid(self.position.x, self.position.y, newAsteroidsRadius)
         
         smallerAst1.velocity = pygame.Vector2(v1.x, v1.y) * 1.2
         smallerAst2.velocity = pygame.Vector2(v2.x, v2.y) * 1.2

         return smallerAst1, smallerAst2





