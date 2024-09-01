import pygame
from constants import *
from player import *
def main():
    # Game inizialization
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    # Game start info
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # Set game window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    # Initialize main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        dt = clock.tick(60) /1000
        pygame.display.flip()



if __name__ == "__main__":
    main()