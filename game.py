"""
Catch the Brain
A Python Game made with Pygame
Game Python File
By Ulysse Valdenaire
"""
import pygame
from circle import Circle
from brain import Brain


class Game:

    def __init__(self):
        self.welcome = True
        self.first_level = False
        self.second_level = False
        self.circle = Circle()
        self.all_circles = pygame.sprite.Group()
        self.brain = Brain()
        self.all_brains = pygame.sprite.Group()

    def level1(self):
        self.first_level = True
        self.second_level = False
        self.welcome = False
        self.spawn_circle()
        self.spawn_white()

    def level2(self):
        self.second_level = True
        self.first_level = False
        self.welcome = False
        self.spawn_circle()

    def update2(self, screen):
        screen.blit(self.brain.image, self.brain.rect)

    def update(self, screen):
        screen.blit(self.circle.image, self.circle.rect)
        screen.blit(self.brain.image, self.brain.rect)

    def spawn_circle(self):
        circle = Circle()
        self.all_circles.add(circle)

    def spawn_white(self):
        brain = Brain()
        self.all_brains.add(brain)
