def poker()
  #creation paquet
  paquet = []
  couleur_hash = {0 => "coeur", 1 => "carreau", 2 => "pique", 3 => "trefle"}
  (0..3).each {|couleur| (2..14).each {|carte|
    paquet << [carte, couleur_hash[couleur]]}}
  #tirage du flop
  cartes_restantes = 53
  carte_tiree = rand(cartes_restantes)
  flop = []
  (1..3).each {|carte|
  flop << paquet[carte_tiree]
  paquet.delete_at(carte_tiree)
  cartes_restantes -= 1
  carte_tiree = rand(cartes_restantes)
  }
  #tirage joueurs
  cartes_joueurs = []
  (0..7).each {|carte| 
  cartes_joueurs << paquet[carte_tiree]
  paquet.delete_at(carte_tiree)
  cartes_restantes -= 1
  carte_tiree = rand(cartes_restantes)
  }
  print flop
  print cartes_joueurs
  print paquet.length
    
end