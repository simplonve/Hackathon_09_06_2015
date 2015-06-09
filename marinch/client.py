#! /usr/bin/python
# -*- coding:utf-8 -*-
import socket, sys, os, threading

host = os.environ.get('RDB_HOST') or '192.168.1.34'
port = 40000

class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            print "*" + message_recu + "*"
            if message_recu =='' or message_recu.upper() == "FIN":
                break
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

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((host, port))
except socket.error:
    print "La connexion a échoué."
    sys.exit()
print "Connexion établie avec le serveur."

th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()
