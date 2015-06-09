#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import pygame
import pygame.gfxdraw
from pygame.locals import *

largeur = 180
hauteur = 150

pygame.init()

fenetre = pygame.display.set_mode((taille_pixel*largeur, taille_pixel*hauteur))

image_arriere_plan = pygame.image.load("images/fond_accueil.svg")

background = pygame.Surface(fenetre.get_size())
background = background.convert()
background.fill((255, 255, 255))

pygame.display.set_caption('MarInch')


pygame.display.flip()

fonctionnement = True

while fonctionnement:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fonctionnement = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                fonctionnement = False