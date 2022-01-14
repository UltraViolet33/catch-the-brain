"""
Catch the Brain
A Python Game made with Pygame
Game Python File
By Ulysse Valdenaire
"""
import pygame
import random


class Brain(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Images/brain.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000)
        self.rect.y = random.randint(0, 470)
        self.velocity = 1
        self.score = 0
