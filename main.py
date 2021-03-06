import pygame, sys
pygame.init()
screenInfo = pygame.display.Info()
size = (width, height) = (screenInfo.current_w, screenInfo.current_h)
#screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()
bgColor = (0, 250, 100)
ballImage = pygame.image.load("beachBall.png")
ballRect = ballImage.get_rect()
ballSpeed = pygame.math.Vector2(0.8, 0.8)
ballRect.center = (width//2, height//2)
pygame.display.set_caption('BouncingBall Test')

def moveBall():
        ballRect.move_ip(ballSpeed)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(1000)
        screen.fill(bgColor)
        pygame.display.flip()
        moveBall()
        screen.blit(ballImage, ballSpeed)

if __name__ == "__main__":
    main()