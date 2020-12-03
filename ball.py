import pygame

ballImage = pygame.image.load() # FIX ME LATER!
ballRect = ballImage.get_rect()
ballSpeed = pygame.math.Vector2(0.8, 0.8)

class Ball():
    def moveBall():
        ballRect.move_ip(ballSpeed)