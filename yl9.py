#-----------------------------------------------------
# --- # yl9
#-----------------------------------------------------
""" 
Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)
"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles

#-----------------------------------------------------
# --- 
#-----------------------------------------------------


kylg_a = float(input( "sisesta külg a : " ))

kylg_b = float(input( "sisesta külg b : " ))

kylg_c = float(input( "sisesta külg c : " ))


if kylg_c < 0 or kylg_b  < 0 or kylg_a  < 0:
        print("kasutaja on sisestanud kolmnurga negatiivse külje pikkuse (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")
elif kylg_c > kylg_a and kylg_c > kylg_b and kylg_a == kylg_b:
        print("kasutaja on sisestanud võrdhaarse kolmnurga (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")
elif kylg_c == kylg_a and kylg_c == kylg_b and kylg_a == kylg_b:
        print("kasutaja on sisestanud võrdkülgse kolmnurga (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")
else :
        print("kasutaja on sisestanud kolmnurga (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")





#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------