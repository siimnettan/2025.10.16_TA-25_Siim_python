
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
    nimi = input("Tere! Mis sinu nimi on? ")
    print("Tere,", nimi +"! Kust sa pärit oled?")
    txt = input().lower().strip() #chain
    # txt.lower()
    
    if txt in ["Saaremaalt", "Saarest","Kuressaarest","Orissaarest","Sõrvest"]:
        print("kui elukoht on Saaremaa, siis väljastab mingi kommentaari ")
    else: 
        print("aaaaa")
    
    
    txt = int(input("aga kui vana sa oled? "))
    if txt < 18:
        print("ahsoo, sa oled liiga noor, et autot juhtida")
    elif txt == 18: 
        print("õnnitleb täisealiseks saamise puhul")
    else: 
        print("kasutaja võib autot juhtida")

    print("Head teed,", nimi+ "!")

soiduAlgus()




#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------