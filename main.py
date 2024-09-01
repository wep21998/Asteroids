import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Game initialization
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #conainer initialization
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    # Game start info
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # Set game window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    # initialize main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) /1000
        screen.fill((0,0,0))
        for obj in updatable:
            obj.update(dt)
        for astroid in asteroids:
            for shot in shots:
                if shot.collision(astroid):
                    astroid.split()
                    shot.kill()
            if astroid.collision(player):
                print("Game over!")
                sys.exit()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()