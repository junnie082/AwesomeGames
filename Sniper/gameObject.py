import pygame
import random

class GameObject:
    def __init__(self, image_path, size, speed_range, score):
        self.image = pygame.image.load(image_path)
        self.size = size
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.speed_x = random.randint(speed_range[0], speed_range[1])
        self.speed_y = random.randint(speed_range[0], speed_range[1])
        self.score = score
