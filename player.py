import pygame
import functions

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        done = True

    screen.blit(functions.get_image("chessboard.png"), (0,0))
        
    pygame.display.flip()
    clock.tick(60)

