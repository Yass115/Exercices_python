import math as m

def rad_deg_min(rad):
    deg = int(rad*(180/m.pi))
    min = int(deg * 60)
    sec = int(min * 60)
    return print(f"{rad} correspond à {deg} degrès et ça correspond aussi à  {min} minutes et {sec} secondes")

radians = int(input("Ecrivez votre angle en radians: "))
f = rad_deg_min(radians)
print(f)
