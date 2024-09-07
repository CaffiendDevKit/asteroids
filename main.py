import sys
import pygame
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)


    player = Player(x=(SCREEN_WIDTH / 2),y=(SCREEN_HEIGHT / 2))
    asteroidField = AsteroidField()
    

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for each in updatable:
            each.update(dt)
        for each in drawable:
            each.draw(screen)
        for each in asteroids:
            for shot in shots:
                if each.collision_check(shot):
                    each.kill()
                    shot.kill()
            if each.collision_check(player): #Player collided with an asteroid
                print("Game over!")
                sys.exit()
        
        pygame.display.flip()
        dt = clock.tick(TARGET_FPS) / 1000 # 60 FPS


if __name__ == "__main__":
    main()