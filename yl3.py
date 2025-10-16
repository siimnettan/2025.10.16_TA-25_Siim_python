# yl3
# Kirjuta programm, mis küsib kasutajalt 
# täisarvu n vahemikus 1-9. 
# Arvuta n + nn + nnn väärtus ja väljasta see. 
# (Näiteks kui kasutaja sisestab 2, siis on vaja 
# väljastada tulemus 2 + 	22 + 222 = 246). 
# Ära kasuta korrutamistehet. 
# Ülesanne on lahendatav ainult liitmise operaatorit kasuades

# ctrl + ä
# shift alt a


import math

n = int(input( "palun anna raadius: " ))

b = str(n) + str(n)

c = str(n) + str(n) + str(n)

summa = n + int(b) + int(c)

print(summa)

#print(summa)


