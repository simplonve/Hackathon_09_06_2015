#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import pygame
import pygame.gfxdraw
from pygame.locals import *

largeur = 1280
hauteur = 720

pygame.init()

fenetre = pygame.display.set_mode((largeur, hauteur))

image_arriere_plan = pygame.image.load("images/accueil/decormaster.svg")

background = pygame.Surface(fenetre.get_size())
background = background.convert()
background.fill((255, 255, 255))

pygame.display.set_caption('MarInch')
pygame.display.flip()

def select_perso():
    perso = raw_input('choisisez un perso :')
    if perso == 1: perso = croix
    if perso == 2: perso = triangle
    if perso == 3: perso = carre
    if perso == 4: perso = rond
    return perso



fonctionnement = True

while fonctionnement:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fonctionnement = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                fonctionnement = False