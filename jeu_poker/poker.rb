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
  paquet.delete_at(carte_tiree)
  puts paquet.length
end
