"""
Catch the Brain
A Python Game made with Pygame
Circle Python File
By Ulysse Valdenaire
"""
import pygame
import random


class Circle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Images/circle.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000)
        self.rect.y = random.randint(0, 470)
