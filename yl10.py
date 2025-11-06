
#-----------------------------------------------------
# --- # yl10.py
#-----------------------------------------------------
""" 
Kirjuta programm, mis 
küsib kasutajalt nime, tervitab teda nimepidi, 
küsib kasutajalt elukoha, 
kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse, 
kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, 
kui vanus on 18, siis õnnitleb täisealiseks saamise puhul, 
kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. (sõne - string)
"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles

#-----------------------------------------------------
# --- 
#-----------------------------------------------------

def soiduAlgus():
    # küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, 
    nimi = input("Mis sinu nimi on? ")
    txt = input("Tere,  {nimi} ! Kust sa pärit oled?")

    print("Head teed!")

soiduAlgus()

#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------