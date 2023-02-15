# Inversion d'une chaîne de caractères

# Chaîne fournie au départ
ch = input("Entrez votre mot: ")

lc = len(ch)  # nombre de caractères total
i = lc - 1  # le traitement commencera à partir du dernier caractère
nch = ""  # nouvelle chaîne à construire (vide au départ)
while i >= 0:
    # on concatène le caractère lu à la nouvelle chaine
    nch += ch[i]
    i -= 1

# Affichage du résultat
print(ch, "=>", nch)