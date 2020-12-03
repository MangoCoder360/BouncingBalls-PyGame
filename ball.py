import pygame

ballImage = pygame.image.load("ball.png")
ballRect = ballImage.get_rect()
ballSpeed = pygame.math.Vector2(0.8, 0.8)
ballRect.center = (width//2, height//2)

class Ball():
    def moveBall():
        ballRect.move_ip(ballSpeed)