import pygame
import constants
import random

pygame.init()
screen = pygame.display.set_mode((810, 810))
pygame.display.set_caption("Copycat Chess")
clock = pygame.time.Clock()
all_sprites_list = pygame.sprite.Group()
done = False

pos_x_list = constants.pos_x_list
pos_y_list = constants.pos_y_list

print(pos_x_list)
print(pos_y_list)

class Piece(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = constants.get_image("pieces/pd.png")
        self.rect = self.image.get_rect()

for i in range(20):
    print(i)
    piece = Piece()
    axis = random.choice(constants.axis_list)
    if axis == 'x':
        rect_x = random.choice(pos_x_list)
        piece.rect.x = rect_x
        piece.rect.y = random.choice(constants.far_close_list)
        pos_x_list.remove(rect_x)
    elif axis == 'y':
        rect_y = random.choice(pos_y_list)
        piece.rect.x = random.choice(constants.far_close_list)
        piece.rect.y = rect_y
        pos_y_list.remove(rect_y)

    all_sprites_list.add(piece)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        done = True

    screen.blit(constants.get_image("chessboard.png"), (0,0))
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

