

#-----------------------------------------------------
# --- # yl21.py
#-----------------------------------------------------
""" 
Arvuti mõtleb välja arvu nullist sajani. 
Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
Vale pakkumise korral annab arvuti vihje, kas pakkumine on 
õigest arvust suurem või väiksem. 
Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. 
(juhuarv - random)
"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles
# method puhul saab kasutada loogikat OBJEKT.METHOD()

#-----------------------------------------------------
# --- 
#-----------------------------------------------------
import random

###                                      
print( your_quess := int(input("anna üks arv vahemikus 1-100: ") ))
print(comp_quess := random.randint(1,100))

while your_quess != comp_quess:
    # if your_quess == comp_quess:
    #     print("Ohh sa arvasid ära.your_quess:",your_quess,"ja comp_quess :", comp_quess)
    # else:
        if your_quess > comp_quess:
            print("sa pakkusid liialt palju. paku natuke vähem")
            print( your_quess := int(input("anna üks arv vahemikus 1-100: ") ))
        else:
            print("paku suurem number")
            print( your_quess := int(input("anna üks arv vahemikus 1-100: ") ))








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

