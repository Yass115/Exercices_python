j = 0
l = int(input("Entrez le nombre de chiffres: "))
n = l
k =[]
s = 0


for i in range(l):
    k.append(i)

while j < n:
    s += k[j]
    j += 1

print(f"La somme des {l} premiers chiffres est égale à {s}")
