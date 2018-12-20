import pygame
import os
import sys

pygame.init()

pos_x_list = [45,90,135,180,225,270,315,360,405,450,495,540,585,630,675,720]
pos_y_list = [45,90,135,180,225,270,315,360,405,450,495,540,585,630,675,720]
axis_list = ['x', 'y']
far_close_list = [45, 720]

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
