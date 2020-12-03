import pygame
from pygame.locals import *
pygame.init()
screenInfo = pygame.display.Info()
size = (width, height) = (screenInfo.current_w, screenInfo.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bgColor = (0, 255, 100)

def main():
    while True:
        clock.tick(1000)
        screen.fill(bgColor)
        pygame.display.flip()

if __name__ == "__main__":
    main()