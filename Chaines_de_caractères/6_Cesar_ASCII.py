#chiffrement césar avec tous les caractères ascii

def cesar_cipher(msg="", key=0):
    msg_ch = ""
    for i in msg:
        a = ord(i)
        b = chr(a + key)
        msg_ch = msg_ch + b
    return msg_ch


def cesar_decipher(msg_ch,key=0):
    msg = ""
    for i in msg_ch:
        a = ord(i)
        b = chr(a - key)
        msg = msg + b
    return msg




msg = str(input("Entrez votre message: "))
key = input("Entrez votre clée: ")
msg_cipher = cesar_cipher(msg,int(key))
print(" ")
print("Chifrement en cours...")
print(f"{msg}---chifrement--->{msg_cipher}")
print("--------------------------------------------------------------------------------")



choice = input("Voulez-vous déchiffrer le message ?(y/n): ")
if choice == "y":
    msg_cl = cesar_decipher(msg_cipher,int(key))
    print(" ")
    print("déchiffrement en cours...")
    print(f"{msg_cipher}-----déchiffrement----->{msg_cl}")
else:
    print("Le programme prendra fin maintenant, merci pour votre visite !!")
