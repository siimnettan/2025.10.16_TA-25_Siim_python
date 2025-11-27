

#-----------------------------------------------------
# --- # yl20.py
#-----------------------------------------------------
""" 
Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
8 x 0 = 0
	8 x 1 = 8
	8 x 2 = 16
	…
	8 x 12 = 96
Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse

"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles
# method puhul saab kasutada loogikat OBJEKT.METHOD()

#-----------------------------------------------------
# --- 
#-----------------------------------------------------

# ### versioon üks 
# for i in range(12):
#     # print(f"arvuta  {8 *= i}")  # EI TÖÖTA
#     # print("arvuta  ", 8 *= i , " smth")  # EI TÖÖTA vist ei saa omistada print käsu
#     print("arvuta 8 x", i, "=", 8 * i , " smth")  # TÖÖTAB
#     i += 1
#     if i == 12:
#         print("arvuta 8 x", i , "=", 8 * i  , " lopp")  # TÖÖTAB


# ### versioon kaks
# print( number_value := int(input("anna palun üks nr: ") ))
# for i in range(number_value):
#     print("arvuta 8 x", i, "=", 8 * i )  # TÖÖTAB
#     print(f"i on tüüpi {type(i)} väärtusega :", i)
#     i += 1
#     # if i >= number_value:                           # TÖÖTAB
#     if i == number_value:                           # TÖÖTAB
#         print("arvuta 8 x", i , "=", 8 * i  , " lopp")  # TÖÖTAB
#         break


# ### versioon kolm                                       # EI TÖÖTA
# def formula_template():
#     if i < number_value:
#         print(i * 8)
#     else:
#         print(i+1 *8 )

# print( number_value := int(input("anna palun üks nr: ") ))

# for i in range(number_value):
#     # print("arvuta 8 x", i, "=", formula_template(i) )  # EI TÖÖTA
#     print("arvuta 8 x", i, "=", formula_template() )  # EI TÖÖTA
    # i += 1




# ### versioon kolm                                       # EI TÖÖTA
# # print("sisestasid ", number_value := int(input("anna palun üks nr: ") ))
# number_value = 2
# for i in range(number_value):
#     if i < number_value:
#         print("print 8 x", i,"vastus", i * 8)
#         i += 1
#     else:
#         print("print 8 x", i,"vastus", i+1 *8 , "lkjasd")


# ### versioon neli                                       # TÖÖTAB
# print("sisestasid ", number_value := int(input("anna palun üks nr: ") ))

# for i in range(number_value + 1):
#     if i < number_value:
#         print("print 8 x", i,"vastus", i * 8)
#         i += 1
#     else:
#         print("print 8 x", number_value,"vastus", number_value *8 , "lkjasd")


# ### versioon viis                                       # TÖÖTAB
print("anna korrutatav ", multiplicand := int(input("anna palun üks korrutatav (8): ") ))
print("korrutaja ", multiplier := int(input("anna palun üks korrutaja: ") ))

for i in range(multiplier + 1):
    if i < multiplier:
        print("print ",multiplicand," x", i,"vastus", i * 8)
        i += 1
    else:
        print("print ",multiplicand," x", multiplier,"vastus", multiplier *  i, "lkjasd")



#### OPI objekti nimi


# **Reegel:**  
# `[Täpsustav osa]_[Põhisõna]`


### Miks number_value ja mitte value_number?
# Inglise keeles põhisõna tuleb tavaliselt lõppu, täpsustav osa ette.
# Siin põhisõna on value (väärtus), täpsustav osa on number (mis tüüpi väärtus).
# number_value = väärtus, mis on number.
# value_number kõlaks nagu "väärtuse järjekorranumber" (teine tähendus).

### Miks input_number ja mitte number_input?
# Põhisõna on number, täpsustav osa on input (kust see tuleb).
# input_number = number, mis on sisestatud.
# number_input kõlaks nagu "sisestus, mis on number" (võib segadust tekitada, sest input on tegevus).

#####
### Kui tahad lihtsalt hoida vahemikku:
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

