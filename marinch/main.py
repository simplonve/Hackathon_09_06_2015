#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import pygame
import pygame.gfxdraw
from pygame.locals import *

largeur = 1024
hauteur = 720

pygame.init()

fenetre = pygame.display.set_mode((largeur, hauteur))

image_arriere_plan = pygame.image.load("images/accueil/decormaster.png")
perso = pygame.image.load("images/characteres/trianglemaster.png")

background = pygame.Surface(fenetre.get_size())
background = background.convert()
fenetre.blit(image_arriere_plan, (0, 0))

pygame.display.set_caption('MarInch')
pygame.display.flip()

def select_perso():
    perso = raw_input('choisisez un perso :')
    if perso == 1: perso = croix
    if perso == 2: perso = triangle
    if perso == 3: perso = carre
    if perso == 4: perso = rond
    return perso


class Perso(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = perso
        """Set the number of Pixels to move each time"""
        #saut de pixel
        self.x_dist = 10
        self.y_dist = 10

    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        xMove = 0;
        yMove = 0;
        if (key == K_RIGHT):
            xMove = self.x_dist
        elif (key == K_LEFT):
            xMove = -self.x_dist
        elif (key == K_UP):
            yMove = -self.y_dist
        elif (key == K_DOWN):
            yMove = self.y_dist
        #self.rect = self.rect.move(xMove,yMove);
        self.rect.move_ip(xMove,yMove);




fonctionnement = True

while fonctionnement:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fonctionnement = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                fonctionnement = False