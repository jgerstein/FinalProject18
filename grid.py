import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
chessboard = pygame.image.load("chessboard.png")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(chessboard, (0,0))
    
    pygame.display.flip()
    clock.tick(60)