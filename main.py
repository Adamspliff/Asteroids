import pygame
import sys 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots,updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        
        updatable.update(dt)
        

        new_shot = player.update(dt)
        if new_shot is not None: #debuggin statement no really necessairy
            pass
        
        for a in asteroids:
            if player.collision(a):
                print("Game over!")
                sys.exit()
        for a in asteroids:
            for s in shots:
                if s.collision(a):
                    a.split()
                    s.kill()

        
        for i in drawable:
            i.draw(screen)
                

        pygame.display.flip()
        dt = clock.tick(60) / 1000

       
if __name__ == "__main__":
    main()

