# Codage Chuck Norris (binaire vers unaire)
def binaire2unaire(binaire, table):
    # On prépare le résultat unaire
    unaire = ""

    # Mémorisation du caractère précédent pour détecter le changement
    prev = ""

    # Il faut un compteur de répétitions
    rep = 0  # Facultatif car la première occurrence le crée. Mais pour la forme...

    # Traitement de tous les caractères du binaire
    # Comme il faudra faire un traitement après le dernier caractère
    # On lui rajoute "artificiellement" une valeur pour gérer le dernier caractère utile
    for b in binaire + ".":
        # Si le caractère a changé
        if b != prev:
            # Si on n'est pas sur le premier cas (déjà un caractère mémorisé)
            if prev:
                # On complète le unaire
                unaire += " %s %s" % (table[prev], "0" * rep)

            # Le compteur de répétitions est remis à 0 (création à la première itération si pas créé avant la boucle)
            rep = 0

            # On mémorise ce nouveau caractère
            prev = b
        # if

        # Cas général, quel que soit le caractère on incrémente la répétition
        rep += 1
    # for

    # Travail terminé (mais la chaine commence par un espace inutile)
    return unaire[1:]


# binaire2unaire()

# Décodage Chuck Norris (unaire vers binaire)
def unaire2binaire(unaire, table):
    # On crée la table de décodage en inversant clefs et valeurs de la table de codage
    decode = dict()
    for (k, v) in table.items(): decode[v] = k

    # On prépare le résultat binaire
    binaire = ""

    # On commence par découper le unaire sur l'espace
    mesg = unaire.split(" ")

    # On récupère le message découpé de 2 en 2
    for i in range(0, len(mesg), 2):
        # Le premier élément est le code, le second le nombre de répétitions
        binaire += decode[mesg[i]] * len(mesg[i + 1])

    # Travail terminé
    return binaire


# unaire2binaire()

# Test
# La table de traduction binaire/unaire
table = {
    "1": "0",
    "0": "00",
}

# Le message de base
mesg = "10000111"

# Le codage
unaire = binaire2unaire(mesg, table)

# Le décodage
binaire = unaire2binaire(unaire, table)

# Résultat
print("message originel: [{}]".format(mesg))
print("codage: [{}]".format(unaire))
print("décodage: [{}]".format(binaire))
print("vérification: {}".format("ok" if binaire == mesg else "bad"))