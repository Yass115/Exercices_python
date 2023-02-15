import math as m

rayon = int(input("Entrez votre rayon: "))
hauteur = int(input("Entrez votre hauteur: "))
if isinstance(rayon,int):
    if isinstance(hauteur,int):
        volume = int((m.pi*(rayon**2)*hauteur)/3)
        print(f"Le volume du cone droit est de {volume}")
    else:
        raise ValueError("Attention au type de la hauteur")
else:
    raise ValueError("Attention au type du rayon")
