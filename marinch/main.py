#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import pygame, os
import pygame.gfxdraw
from pygame.locals import *

width = 1024
height = 720

pygame.init()
image_arriere_plan = pygame.image.load("data/images/accueil/decormaster.png")

pygame.display.set_caption('MarInch')


def select_perso():
    perso = raw_input('choisisez un perso :')
    if perso == 1: perso = croix
    if perso == 2: perso = triangle
    if perso == 3: perso = carre
    if perso == 4: perso = rond
    return perso


def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'images')
    fullname = os.path.join(fullname, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()



class PyManMain:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=640,height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height), RESIZABLE)
                                                          
    def MainLoop(self):
        """This is the Main Loop of the Game"""
        
        """Load All of our Sprites"""
        self.LoadSprites();
        """tell pygame to keep sending up keystrokes when they are
        held down"""
        pygame.key.set_repeat(500, 30)
        
        """Create the fenetre"""
        self.fenetre = pygame.Surface(self.screen.get_size())
        self.fenetre = self.fenetre.convert()
        self.fenetre.fill((0,0,0))
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.perso.move(event.key)
            """Check for collision"""
            """Do the Drawging"""
            self.screen.blit(self.fenetre, (0, 0))
            self.perso_sprites.draw(self.screen)
            pygame.display.flip()
                    
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.perso = perso()
        self.perso_sprites = pygame.sprite.RenderPlain((self.perso))


class perso(pygame.sprite.Sprite):
    """This is our perso that will move around the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('characteres/trianglemaster.png',-1)
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

if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()


fonctionnement = True

while fonctionnement:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fonctionnement = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                fonctionnement = False