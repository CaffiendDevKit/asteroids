import pygame
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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(x=(SCREEN_WIDTH / 2),y=(SCREEN_HEIGHT / 2))
    asteroidField = AsteroidField()
    

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for each in updatable:
            each.update(dt)
        for each in drawable:
            each.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(TARGET_FPS) / 1000 # 60 FPS


if __name__ == "__main__":
    main()