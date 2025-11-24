
#-----------------------------------------------------
# --- # yl14.py
#-----------------------------------------------------
""" 
Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” 
(ext - extension - faili laiend) ja prindib välja laiendi (“ext”). (str.split)
"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles
# method puhul saab kasutada loogikat OBJEKT.METHOD() siis ei 
#   ei pea sulgudesse panna

#-----------------------------------------------------
# --- 
#-----------------------------------------------------

# aju.txt

def prog():
    name_fail = input("mis küsib kasutajalt failinimi koos faililaiendiga :")
    # name_fail = str.split(name_fail, ".")
    name_fail = name_fail.split( ".")
    ## name_fail.split( ".") # ei tööta tuleb ka omistamine
    print(name_fail[1])

prog()



#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------