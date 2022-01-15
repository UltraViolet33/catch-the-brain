"""
Catch the Brain
A Python Game made with Pygame
Main Python File
By Ulysse Valdenaire
"""
# importation des classes et modules
import pygame
import random
import math
from game import Game

# initialisation du module pygame
pygame.init()

# générer le fenêtre de jeu
pygame.display.set_caption("Catch the Circle")
screen = pygame.display.set_mode((1080, 600))

# importer le fond
background = pygame.image.load('Images/fond.jpg')
background = pygame.transform.scale(background, (1080, 600))

# importer l'image pour cacher le cercle
cache = pygame.image.load('Images/square.png')

# importer l'image pour cacher le cerveau
cache2 = pygame.image.load('Images/square.png')

# importer le cerveau
clue = pygame.image.load('Images/brain.png')

# importer le bouton level 1
level_1_button = pygame.image.load('Images/one.png')
level_1_button_rect = level_1_button.get_rect()
level_1_button_rect.x = math.ceil(screen.get_width() / 2.2)
level_1_button_rect.y = math.ceil(screen.get_height() / 2.8)

# importer le boutton level 2
level_2_button = pygame.image.load('Images/two.png')
level_2_button_rect = level_2_button.get_rect()
level_2_button_rect.x = math.ceil(screen.get_width() / 2.2)
level_2_button_rect.y = math.ceil(screen.get_height() / 2.0)

game = Game()

# boucle du jeu
running = True
while running:
    screen.blit(background, (0, 0))
    # Niveau 1
    if game.first_level:
        game.update(screen)
    # Niveau 2
    elif game.second_level:
        game.update2(screen)
    elif game.welcome:
        # ecran d'accueil avec boutton de niveau
        screen.blit(level_1_button, (level_1_button_rect))
        screen.blit(level_2_button, (level_2_button_rect))

    # mise à jour de l'écran
    pygame.display.flip()

    # evenements de pygame
    for event in pygame.event.get():
        # si le joueur ferme la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.first_level = False
                game.second_level = False
                game.welcome = True
                print("ok")

        # si le joueur appuie sur la souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score = 0
            if game.brain.rect.collidepoint(event.pos):
                # cache le cerveau
                screen.blit(cache, (game.brain.rect.x, game.brain.rect.y))
                # nouvelles coordonnées du cercle
                game.brain.rect.x = game.circle.rect.x
                game.brain.rect.y = game.circle.rect.y
                # nouvelles coordonnées du cerveaux
                game.circle.rect.x = random.randint(0, 1000)
                game.circle.rect.y = random.randint(0, 500)

            if level_1_button_rect.collidepoint(event.pos):
                game.level1()
                screen.blit(cache, (level_1_button_rect))
                screen.blit(cache, (level_2_button_rect))
            elif level_2_button_rect.collidepoint(event.pos):
                game.level2()
                screen.blit(cache, (level_1_button_rect))
                screen.blit(cache, (level_2_button_rect))
