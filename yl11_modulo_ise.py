
#-----------------------------------------------------
# --- # yl11.py
#-----------------------------------------------------
""" 
Kirjuta programm, mis küsib kasutajalt sisendina stringi.
Eemalda selle sisendi algusest ja lõpust tühikud.
String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
Väljasta selle stringi kolm keskmist sümbolit.
(stringi meetodid, list)
"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles
# method puhul saab kasutada loogikat OBJEKT.METHOD()

#-----------------------------------------------------
# --- 
#-----------------------------------------------------

###  modulo 
# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# 3 % 2 = 1
# 4 % 2 = 0
# 5 % 2 = 1
# 6 % 2 = 0

##########################

# give_me_str = ""

# def prog():
# mis küsib kasutajalt sisendina stringi.
give_me_str = input("anna üks string: ")
# Eemalda selle sisendi algusest ja lõpust tühikud.
give_me_str = give_me_str.strip()

# if 1 == int(len(give_me_str)) % 2 and int(len(give_me_str)) >= 7:
#     # # String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja 
#     # # et sümbolite arv on paarituarvuline.
#     print("selles on üle 7 sümboli ja see on paaritu", len(give_me_str))
#     # Väljasta selle stringi kolm keskmist sümbolit.
#     is_middle_no = int(len(give_me_str)/2)
#     is_middle_min = is_middle_no - 1 
#     is_middle_max = is_middle_no + 1 
#     # print("stringi kolm keskmist sümbolit", is_middle_min, is_middle_no, is_middle_max )
#     # print("stringi kolm keskmist sümbolit", 
#     #       give_me_str[is_middle_min], 
#     #       give_me_str[is_middle_no], 
#     #       give_me_str[is_middle_max]
#     #     )
#     print("stringi kolm keskmist sümbolit", give_me_str[is_middle_no-1:is_middle_no+1])
    
# else:
#     print("on paaris arv ja/või vähem sümbole")

is_middle_no = int(len(give_me_str)/2)
is_middle_min = is_middle_no - 1 
is_middle_max = is_middle_no + 1     
# print("stringi kolm keskmist sümbolit", 
#       give_me_str[
#           range(is_middle_no-1, is_middle_no+1)
#           ]
#       )

x = range(is_middle_min, is_middle_max+1)

for n in x:
  print(n, x, give_me_str[n])

# name_fail = str.split(name_fail, ".")
# name_fail = name_fail.split( ".")
# # name_fail.split( ".") # ei tööta tuleb ka omistamine
# print(name_fail[1])

# prog()

###########################################
### ctrl kas funktsionaalsused töötavad 
# give_me_str = input("anna üks string: ")
# give_me_str = give_me_str.strip()

### ctrl kas modulo töötab
# if 0 == int(len(give_me_str)) % 2:    
#     print("see on paaris")
# else:
#     print("ei ole paaris arv. Jäägi väärtus", int(len(give_me_str)) % 2)

# if int(len(give_me_str)) >= 7:
#     print("selles on sümbolit", len(give_me_str))
# else:
#     print("not enough symbols", len(give_me_str))


#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------