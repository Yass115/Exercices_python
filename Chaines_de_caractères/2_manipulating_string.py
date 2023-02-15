word = input("Entrez votre mot: ")

st = "*"
lc = len(word)
new_word = word[0]

i = 1
while i < lc:
    new_word = new_word + st + word[i]
    i += 1

print(new_word)