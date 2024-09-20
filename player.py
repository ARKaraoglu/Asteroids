import pygame
from constants import PLAYER_RADIUS
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def draw(self, screen):
       pygame.draw.polygon(surface = screen, color = "white", points = self.triangle(), width = 2) 

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius #type: ignore
        b = self.position - forward * self.radius - right   #type: ignore
        c = self.position - forward * self.radius + right   #type: ignore
        return [a, b, c]

