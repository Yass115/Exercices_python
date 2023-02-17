
val = float(input("Entrez le prix de votre article: "))

choice = input("Entrez votre choix,(0)-->quitter ////(1)--> 6%///// (2)--> 12% ///(3)--> 21%: ")
tva = 0
while tva == 0:
    if choice == "0":
        quit()
    elif choice == "1":
        tva = 0.06
    elif choice == "2":
        tva = 0.12
    elif choice == "3":
        tva = 0.21

taxe = val*tva
prix = val + taxe
print(f"la taxe est de {taxe} eur, le prix TTC est de {prix}")