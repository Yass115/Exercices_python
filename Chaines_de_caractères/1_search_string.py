word = input("Entrez votre mot: ")

a = 0
for i in word:
    if i == "e":
        a += 1


print(f"Il y a {a} lettres e dans cettte chaine de caractère")


# solution:

# Recherche d'un caractère particulier dans une chaîne
# Chaîne fournie au départ
ch = "Monty python flying circus"

# Caractère à rechercher
cr = "e"

# Recherche proprement dite
'''lc = len(ch)  # nombre de caractères à tester 
i = 0  # indice du caractère en cours d'examen 
t = False  # "drapeau" à lever si le caractère recherché est présent 
while i < lc:
    if ch[i] == cr:
        t = True
    i = i + 1

# Affichage final 
print("Le caractère", cr, end=' ')
if t:
    print("est présent", end=' ')
else:
    print("est introuvable", end=' ')
print("dans la chaîne", ch)'''