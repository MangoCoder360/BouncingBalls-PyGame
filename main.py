import pygame
from pygame.locals import *
pygame.init()
screenInfo = pygame.display.Info()
size = (width, height) = (screenInfo.current_w, screenInfo.current_h)
screen = pygame.display.set_mode(size)