
#-----------------------------------------------------
# --- # yl13.py
#-----------------------------------------------------
""" 
Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
Koosta list, mis koosneb kolmest loomast.
Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
Väljasta see lemmikloomade list.
Väljasta listi viimase elemendi viimane täht.
(sõne kui list, mitmemõõtmeline ilist - multi dimensional)

"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles

#-----------------------------------------------------
# --- 
#-----------------------------------------------------

# Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
pet = input("mis on sinu lemmik loom :")

print(pet[0])

# # Väljasta listi esimene väärtus
# print(fruit_list[0])

# Koosta list, mis koosneb kolmest loomast.

pets_list = [ "boa", "dog", "cat"]

# Lisa selle listi lõppu kasutaja sisestatud lemmikloom.

pets_list.append(pet) 

print(pets_list)

# Väljasta see lemmikloomade list.
# Väljasta listi viimase elemendi viimane täht.

print(pets_list[-1][-2])

# (sõne kui list, mitmemõõtmeline ilist - multi dimensional)



#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------