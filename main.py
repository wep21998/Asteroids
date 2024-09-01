import pygame
from constants import *
from player import Player

def main():
    # Game inizialization
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    # Game start info
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # Set game window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Initialize main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) /1000
        screen.fill((0,0,0))
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()