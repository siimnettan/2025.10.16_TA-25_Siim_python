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

# mis on kõige pikem külg - pikim külg max-funks



## vers 1
# if  ( kylg_a + kylg_b < kylg_c or kylg_b + kylg_c < kylg_a or kylg_a + kylg_c < kylg_b):

## vers 2
if not ( kylg_a + kylg_b > kylg_c and kylg_b + kylg_c > kylg_a and kylg_a + kylg_c > kylg_b):

## vers 3
# kylg_suurim = max(kylg_a, kylg_b, kylg_c) 
# print(kylg_suurim)
# if (kylg_c < 0 or kylg_b  < 0 or kylg_a  < 0) or (kylg_suurim >= kylg_a + kylg_b + kylg_c - kylg_suurim):
        print("negatiivne või ei eksisteeri (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")
elif kylg_c > kylg_a and kylg_c > kylg_b and kylg_a == kylg_b:
        print("kasutaja on sisestanud võrdhaarse kolmnurga (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")
elif kylg_c == kylg_a and kylg_c == kylg_b and kylg_a == kylg_b:
        print("kasutaja on sisestanud võrdkülgse kolmnurga (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")
else :
        print("kasutaja on sisestanud kolmnurga (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")


# edaspidi ing.k. ja kasuta camel



#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------