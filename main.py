import pygame
from constants import *
def main():
    # Game inizialization
    pygame.init()
    # Game start info
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # Set game window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    # Initialize main game loop
    while True:
        screen.fill((0,0,0))
        pygame.display.flip()



if __name__ == "__main__":
    main()