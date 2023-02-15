
def nombre_chiffres(nombre,chiffre):
    a = 0
    for i in nombre:
        if chiffre == i:
            a += 1
        else:
            a += 0
    print(f"Il y a {a} fois le chiffre {chiffre}")

nombre = input("Entrez votre nombre: ")
chiffre = input("Entrez le chiffre que vous voulez compter: ")

f = nombre_chiffres(nombre,chiffre)
print(f)