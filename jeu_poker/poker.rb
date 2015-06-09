def poker()
  paquet = []
  couleur_hash = {0 => "coeur", 1 => "carreau", 2 => "pique", 3 => "trefle"}
  (0..3).each {|couleur| (2..14).each {|carte|
    paquet << [carte, couleur_hash[couleur]]}
  }
  cartes_restantes = 53
  carte_tiree = rand(cartes_restantes)
  flop = []
  (0..2).each {|flop_carte|
  flop << paquet[carte_tiree]
  paquet.delete_at(carte_tiree)
  cartes_restantes -= 1
  carte_tiree = rand(cartes_restantes)
  }
  print flop
end