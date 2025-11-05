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

# kylg_a = float(input( "sisesta külg a : " ))

# kylg_b = float(input( "sisesta külg b : " ))

# kylg_c = float(input( "sisesta külg c : " ))


# if kylg_c < 0 or kylg_b  < 0 or kylg_a  < 0:
#         print("kasutaja on sisestanud kolmnurga negatiivse külje pikkuse (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")
# elif kylg_c > kylg_a and kylg_c > kylg_b and kylg_a == kylg_b:
#         print("kasutaja on sisestanud võrdhaarse kolmnurga (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")
# elif kylg_c == kylg_a and kylg_c == kylg_b and kylg_a == kylg_b:
#         print("kasutaja on sisestanud võrdkülgse kolmnurga (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")
# else :
#         print("kasutaja on sisestanud kolmnurga (külgedega: ", kylg_a, ", ",  kylg_b, " & ", kylg_c, ") ")



#-----------------------------------------------------
# --- OPI ---
#-----------------------------------------------------

# """ https://www.w3schools.com/python/ref_string_isnumeric.asp  """
# a = "\u0030" #unicode for 0
# b = "\u00B2" #unicode for &sup2;
# c = "10km2"
# d = "-1"
# e = "1.5"
# f = "1"
# ff = "1,1"

# print(a.isnumeric())
# print(b.isnumeric())
# print(c.isnumeric())
# print(d.isnumeric())
# print(e.isnumeric())
# print(f.isnumeric())
# print(ff.isnumeric())

# """ https://stackoverflow.com/questions/36452105/python-user-input-data-type """

# answer = input("Enter an integer: ")
# while not answer.isdigit():
## while not answer.isdecimal(): # huvitav mis vahe on isdigit ja isdecimal 
#     print("That's not a whole number. Try again.")
#     answer = input("Enter an integer: ")
# answer = int(answer)


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))



#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------