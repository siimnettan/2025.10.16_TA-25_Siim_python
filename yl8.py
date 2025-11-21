#-----------------------------------------------------
# --- # yl8
#-----------------------------------------------------
""" 
Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number.
Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.
"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles

#-----------------------------------------------------
# --- 
#-----------------------------------------------------

n = int(input( "kasutaja sisesta aasta : "  ))

# if n % 1 == 0:

# def liigAasta(aasta):
#     # jagub neljasajaga või jagub neljaga ja ei jagu sajaga.
#     if aasta % 400 == 0 or (aasta % 4 == 0 and  aasta % 100 == 0):
#         print(" liigaasta (", aasta  ,  ")")
#     else:
#         print("ei ole  (", aasta  ,  ")")


def liigAasta(aasta):
    # if type(aasta) == int: ma ei oska kontrollida positiivset TÄISARVU, sest 
    # ma muutsin arvu ise juba täisarvuks input juures
    if aasta > 0 and type(aasta) == int:
        
        # jagub neljasajaga või jagub neljaga ja ei jagu sajaga.
        if aasta % 400 == 0 or (aasta % 4 == 0 and  aasta % 100 != 0):
            print(" liigaasta (", aasta  ,  ")")
        else:
            print("ei ole  (", aasta  ,  ")")
    else:
        print(" ei ole korrektne number (", aasta  ,  ")")

#  
liigAasta(n)


#-----------------------------------------------------
# --- OPI ---
#-----------------------------------------------------
#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------