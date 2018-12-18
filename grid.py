import pygame

pygame.init()
screen = pygame.display.set_mode((900,900))
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (161, 66, 38), pygame.Rect(0, 0, 900, 900))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 50, 800, 800))
    pygame.draw.rect(screen, (255,250,240), pygame.Rect(50, 50, 50, 50))
    pygame.draw.rect(screen, (255,250,240), pygame.Rect(150, 50, 50, 50))
    pygame.draw.rect(screen, (255,250,240), pygame.Rect(250, 50, 50, 50))
    pygame.draw.rect(screen, (255,250,240), pygame.Rect(350, 50, 50, 50))
    pygame.draw.rect(screen, (255,250,240), pygame.Rect(450, 50, 50, 50))
    pygame.draw.rect(screen, (255,250,240), pygame.Rect(550, 50, 50, 50))
    pygame.draw.rect(screen, (255,250,240), pygame.Rect(650, 50, 50, 50))
    pygame.draw.rect(screen, (255,250,240), pygame.Rect(750, 50, 50, 50))

    pygame.display.flip()
    clock.tick(60)