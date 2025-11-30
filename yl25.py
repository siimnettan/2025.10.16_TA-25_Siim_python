

#-----------------------------------------------------
# --- # yl25.py
#-----------------------------------------------------
""" 
yl25

Koosta dictionary vähemalt viie endale iseloomuliku tunnusega 
(näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).

Väljasta elukoht kahel erineval viisil (kasutades get() meetodit ja mitte kasutades seda).
Muuda magustoidu väärtust.

Tee kordus üle dictionary ja väljasta kõik võtmed.
Tee kordus üle dictionary ja väljasta kõik väärtused (pööra tähelepanu sellele, et saab mitmel viisil, proovi erinevaid võimalusi).
Kontrolli, kas isikukood on dictionary's olemas.
Leia dictionary suurus (elementide arv).
Lisa element enda pikkuse jaoks.
Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
Tutvu kõigi dictionary meetoditega.
Läbi ülesanne juhendi lõpus.
https://www.w3schools.com/python/python_dictionaries.asp

"""
## TRIKID:
# File → Preferences → Keyboard Shortcuts.
# Toggle line comment:  ctrl shift 7 # eelmisel arvutil:ctrl + ä
# Toggle block comment: shift alt a

# Add cursor Above: ctrl shift uparrow
# copy line down: alt shift nool_alla
# method puhul saab kasutada loogikat OBJEKT.METHOD()

#-----------------------------------------------------
# --- 
#-----------------------------------------------------
#(näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).
# list listis


isel_tunnus =	{
  "eesnimi": "Ford",
  "perenimi": "Mustang",
  "sünniaasta": 1964,
  "elukoht": "Mustoja",
  "magustoit": "puder"
}
print(isel_tunnus)

# kasutades get() meetodit ja mitte kasutades seda).
# Muuda magustoidu väärtust.
print(isel_tunnus["perenimi"])
print(isel_tunnus.get("elukoht"))

isel_tunnus["perenimi"] = "Sepp"
print(isel_tunnus["perenimi"])


# Tee kordus üle dictionary ja väljasta kõik võtmed.
# Tee kordus üle dictionary ja väljasta kõik väärtused 
# (pööra tähelepanu sellele, et saab mitmel viisil, proovi erinevaid võimalusi).


# print(isel_tunnus.keys())
print("asdjölj", x := isel_tunnus.keys(), "lkjsalkj")

# for k in isel_tunnus.keys():
#     print(isel_tunnus[k])
# newlist = [isel_tunnus[k] for k in isel_tunnus.keys() ]

### TÖÖTAS
# newlist = [k for k in isel_tunnus.keys() ]
# print(newlist)

### TÖÖTAS - väärtuste saamiseks - comprehension
newlist = [v for v in isel_tunnus.values() ]
print(newlist)


# Kontrolli, kas isikukood on dictionary's olemas.
# Leia dictionary suurus (elementide arv).
print(isel_tunnus.keys())
print(isel_tunnus.values())

print("isikukood" in isel_tunnus.keys() )
# if "model" in thisdict:
#  print("Yes, 'model' is one of the keys in the thisdict dictionary") 


# Lisa element enda pikkuse jaoks.

# isel_tunnus["pikkus"] = 148
isel_tunnus.update({"pikkus":148})

print(isel_tunnus.items())

# Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
# Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
# Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
# Tutvu kõigi dictionary meetoditega.
# Läbi ülesanne juhendi lõpus.

isel_tunnus.pop("sünniaasta")

print(isel_tunnus.items())



isel_tunnus.clear()

print(isel_tunnus.items())
# ###                                      
# print( your_quess := int(input("anna üks arv vahemikus 1-100: ") ))
# print(comp_quess := random.randint(1,100))

# while your_quess != comp_quess:
#     # if your_quess == comp_quess:
#     #     print("Ohh sa arvasid ära.your_quess:",your_quess,"ja comp_quess :", comp_quess)
#     # else:
#         if your_quess > comp_quess:
#             print("sa pakkusid liialt palju. paku natuke vähem")
#             print( your_quess := int(input("anna üks arv vahemikus 1-100: ") ))
#         else:
#             print("paku suurem number")
#             print( your_quess := int(input("anna üks arv vahemikus 1-100: ") ))








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

