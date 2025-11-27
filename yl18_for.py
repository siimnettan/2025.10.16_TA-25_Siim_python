

#-----------------------------------------------------
# --- # yl18.py
#-----------------------------------------------------
""" 
Väljasta korduslause abil numbrid 5..1 (for in, range)
"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles
# method puhul saab kasutada loogikat OBJEKT.METHOD()

#-----------------------------------------------------
# --- 
#-----------------------------------------------------

# # Väljasta korduslause abil numbrid 5..1 (for in, range)
# random_range = range(0,5)
# print("kas tyyp range? ", type(random_range))
# print("range pikkus ", len(random_range))
# random_range = list(random_range)
# print("kas tyyp list? ",type(random_range))
# random_range.reverse()      # kust tuleb see et vahepeal tuleb objektiks teha?
# print("kas listi saab reverse-da? ", random_range)
# i = 1                         # i-d ei ole vaja eel defineerida

# for i in random_range:
#     print(i)
#     i += 1

for i in range(5):
# for i in range(-5, 0, 1):       # selline asi ka võimalik
# for i in reverse(list(range(5))):       # EI TÖÖTA selline asi ka võimalik
    print("korduslause nr :", i)
    i = i + 1



## OPI objekti nimi

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

