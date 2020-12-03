import pygame
screenInfo = pygame.display.Info()
size = (width, height) = (screenInfo.current_w, screenInfo.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bgColor = (0, 255, 100)
ballImage = pygame.image.load("ball.png")
ballRect = ballImage.get_rect()
ballSpeed = pygame.math.Vector2(0.8, 0.8)
ballRect.center = (width//2, height//2)

def moveBall():
        ballRect.move_ip(ballSpeed)


def main():
    while True:
        clock.tick(1000)
        screen.fill(bgColor)
        pygame.display.flip()
        moveBall()
        screen.blit(ballImage)

if __name__ == "__main__":
    main()