import pygame
from pygame.time import Clock
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatableGroup = pygame.sprite.Group()
    drawableGroup = pygame.sprite.Group()
    Player.containers = (updatableGroup, drawableGroup) #type: ignore 
  
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatableGroup, drawableGroup) #type: ignore
    AsteroidField.containers = (updatableGroup) #type: ignore

    asteroidfield = AsteroidField()
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        for obj in updatableGroup:
            obj.update(dt) 
        screen.fill((0,0,0))
        for sprite in drawableGroup:
            sprite.draw(screen)
        
   
        dt = clock.tick(60) / 1000 
        
        pygame.display.flip()
            
if __name__ == "__main__":
    main()
