n = 0
a = 2

for _ in range(64):
    g = a**n
    n += 1
    print(f"{n} jour ---> {g} grains")
    #print("{} {:.2E}".format(n, g)) #écriture en notation scientifique
