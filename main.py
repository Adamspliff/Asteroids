import pygame
import sys 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
   
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt=0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        
        updatable.update(dt)
        
        for a in asteroids:
            if player.collision(a):
                print("Game over!")
                sys.exit()                   
        
        for i in drawable:
            i.draw(screen)
        #drawable.draw(screen) should work (but does not) bc pygame draws everything with sprite.image and sprite.rect        

        pygame.display.flip()
        dt = clock.tick(60) / 1000

       
if __name__ == "__main__":
    main()

