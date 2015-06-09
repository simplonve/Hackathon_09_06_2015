def poker()
  paquet = []
	couleur_hash = {0 => "coeur", 1 => "carreau", 2 => "pique", 3 => "trefle"}
	(0..3).each {|couleur| (2..14).each {|carte|
	  paquet << [carte, couleur_hash[couleur]]}
	}
  puts paquet.length
	cartes_restantes = 53
  puts carte_tiree = rand(cartes_restantes)
  puts paquet[carte_tiree]
  flop_carte_1 = paquet[carte_tiree]
  paquet.delete_at(carte_tiree)
  cartes_restantes -= 1
  puts carte_tiree = rand(cartes_restantes)
  flop_carte_2 = paquet[carte_tiree]
  paquet.delete_at(carte_tiree)
  cartes_restantes -= 1
  puts carte_tiree = rand(cartes_restantes)
  flop_carte_3 = paquet[carte_tiree]
  paquet.delete_at(carte_tiree)
  cartes_restantes -= 1
  puts paquet.length
end
