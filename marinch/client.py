#! /usr/bin/python
# -*- coding:utf-8 -*-
import socket, sys, os, threading
import pygame
import pygame.gfxdraw
from pygame.locals import *

HOST = os.environ.get('RDB_HOST') or '10.42.0.1'
PORT = 60000

def main(conn):
    image_arriere_plan = pygame.image.load("data/images/maps/mapessai.png")

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

    def select_perso():
        path_image_perso = ''
        perso = input('choisisez un perso :')
        if perso == 1:
            path_image_perso = 'characteres/carremaster.png'
        elif perso == 2:
         path_image_perso = 'characteres/cerclemasterok.png'
        elif perso == 3:
            path_image_perso = 'characteres/trianglemaster.png'
        elif perso == 4:
            path_image_perso = 'characteres/croixmaster.png'
        return path_image_perso

    class Player(object):
        def __init__(self):
            path_image_perso = select_perso()
            self.perso, self.rect = load_image(path_image_perso,-1)
            self.rect.x = 20
            self.rect.y = 10

        def move(self, dx, dy):
            # Move each axis separately. Note that this checks for collisions both times.
            if dx != 0:
                self.move_single_axis(dx, 0)
            if dy != 0:
                self.move_single_axis(0, dy)

        def move_single_axis(self, dx, dy):
            # Move the rect
            self.rect.x += dx
            self.rect.y += dy
            x = self.rect.x
            x = str(x)
            y = self.rect.y
            y = str(y)
            position = 'pos : ' + x + ' ' + y
            connexion.send(position)

            # If you collide with a wall, move out based on velocity
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                        self.rect.x = 20
                        self.rect.y = 10
                    if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                        self.rect.x = 20
                        self.rect.y = 10
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                        self.rect.x = 20
                        self.rect.y = 10
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
                        self.rect.x = 20
                        self.rect.y = 10

    # Nice class to hold a wall rect
    class Wall(object):
        def __init__(self, pos):
            walls.append(self)
            self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

    # Initialise pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()

    # Set up the display
    pygame.display.set_caption("MarInch")
    screen = pygame.display.set_mode((1024, 720))

    clock = pygame.time.Clock()
    walls = [] # List to hold the walls
    player = Player() # Create the player

    # Holds the level layout in a list of strings.
    level = [
    "                                                               W",
    "                                                               W",
    "                                                               W",
    "                                                               W",
    "                       CCC       CCC         CCC           CCC W",
    "                       CCC     CCCCC       CCCCC           CCCCW",
    "                       CCC     CCCCC       CCCCC           CCCCW",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                    CC    CC                                  W",
    "W                    CC    CC CC     CC             CC         W",
    "W                    CC    CC CC     CC             CC         W",
    "W                                                              W",
    "W                                                              W",
    "W                                      CC                      W",
    "W                                      CC                      W",
    "WWWWWWWWWWWWWWWWWWWW     C     wWWWWWWWWWWWWWWWWWWWWWWW        W",
    "W                                   CCC                        W",
    "W                                   CCC                        W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W       CCC             CCC                             CCC    W",
    "W     CCCCC       CC    CCC   CC                  CCC   CCC    W",
    "W     CCCCC       CC    CCC   CC                  CCC   CCC    W",
    "W                                                              W",
    "W                                                              W",
    "W          CC             CC                                   W",
    "W          CC             CC                                   W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW      WWWWWWWWWWWWWWWW     W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                   CC                                         W",
    "W                   CC                                         W",
    "W   CCC    CC    CCC         CCC    CC    CCC   CC   CCC   CC  W",
    "W   CCC    CC    CCC         CCC    CC    CCC   CC   CCC   CC  W",
    "W   CCC          CCC         CCC          CCC        CCC       W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "W                                                              W",
    "WWWWWWWWWWWWWWWWWWWW      E     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]



    # Parse the level string above. W = wall, E = exit
    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                Wall((x, y))
            if col == "E":
                end_rect = pygame.Rect(x, y, 16, 16)
            x += 16
        y += 16
        x = 0

    running = True
    while running:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                connexion.send('FIN')
                quit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                connexion.send('FIN')
                quit()

        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-4, 0)
        if key[pygame.K_RIGHT]:
            player.move(4, 0)
        if key[pygame.K_UP]:
            player.move(0, -4)
        if key[pygame.K_DOWN]:
            player.move(0, 4)

        # Just added this to make it slightly fun ;)
        if player.rect.colliderect(end_rect):
            connexion.send('FIN')
            quit()

        # Draw the scene
        screen.fill((0, 0, 0))
        screen.blit(image_arriere_plan, (0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        screen.blit(player.perso, player.rect)
        pygame.display.flip()

class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            print message_recu
            if message_recu =='' or message_recu.upper() == "FIN":
                break
            elif message_recu[:5] == 'pos :':

        th_E._Thread__stop()
        print "Client arrêté. Connexion interrompue."
        self.connexion.close()

class ThreadEmission(threading.Thread):
    """objet thread gérant l'émission des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while 1:
            message_emis = raw_input()
            self.connexion.send(message_emis)

class ThreadJeu(threading.Thread):
    """objet thread gérant l'émission des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while 1:
            main(self.connexion)
        self.connexion.close()

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((HOST, PORT))
except socket.error:
    print "La connexion a échoué."
    sys.exit()
print "Connexion établie avec le serveur."

th_E = ThreadEmission(connexion)
th_J = ThreadJeu(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_J.start()
th_R.start()
