

#-----------------------------------------------------
# --- # yl19.py
#-----------------------------------------------------
""" 
Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv
"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles
# method puhul saab kasutada loogikat OBJEKT.METHOD()

#-----------------------------------------------------
# --- 
#-----------------------------------------------------

# # Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv
vowel_set = ("a", "e", "i", "o", "u", "õ", "ä", "ö", "ü")
# vowel_set = ("a", "a") # tüüp TUPLE
# vowel_set = ("a")     # tüüp STRING
print("kas tyyp list? ",type(vowel_set))

print("1. vokaale on Tuple-s ", len(vowel_set))
print(f"2. vokaale on {type(vowel_set)} set-s :", len(vowel_set))

k = 0

### versioon kaks 
for i in range(len(vowel_set)):
    print("käsitsi kokku arvutades ", i)
    i += 1
    k += 1
# print("range pikkus ", len(random_range))
print(f"kokku on {k} vokaali")



#### OPI objekti nimi

# Kui tahad lihtsalt hoida vahemikku:
# number_range
# range_values
# sequence_range

# Kui see on mõeldud iteratsiooniks:
# iteration_range
# loop_range

# Kui plaanid hiljem muuta selle juhuslikuks (nt shuffle):
# range_list (ja hiljem random.shuffle(range_list))




#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------

