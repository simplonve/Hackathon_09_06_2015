#! /usr/bin/python
# -*- coding:utf-8 -*-
import socket, sys, os, threading

HOST = os.environ.get('RDB_HOST') or '10.42.0.1'
PORT = 60000

class ThreadClient(threading.Thread):
    '''dérivation d'un objet thread pour gérer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        nom = self.getName()
        while 1:
            msgClient = self.connexion.recv(1024)
            if msgClient.upper() == "FIN" or msgClient =="":
                break
            message = "%s> %s" % (nom, msgClient[6:len(msgClient)-4]])
            print message
            for cle in conn_client:
                if cle != nom:
                    conn_client[cle].send(message)
        self.connexion.close()
        del conn_client[nom]
        print "Client %s déconnecté." % nom

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print "La liaison du socket à l'adresse choisie a échoué."
    sys.exit()
print "Serveur prêt, en attente de requêtes ..."
mySocket.listen(5)

conn_client = {}
while 1:
    connexion, adresse = mySocket.accept()
    th = ThreadClient(connexion)
    th.start()
    it = th.getName()
    conn_client[it] = connexion
    print "Client %s connecté, adresse IP %s, port %s." %\
          (it, adresse[0], adresse[1])
    connexion.send("Vous êtes connecté. Envoyez vos messages.")
