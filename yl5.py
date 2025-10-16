# yl5
""" 
Koosta tõeväärtustabel kahele avaldisele
A AND (B OR C)
(A  B) OR NOT(C AND A)

https://docs.google.com/spreadsheets/d/1sUFsE-bOm3isqKUGlIgjZWtdfqv7jDXp9lkch2pNCWc/edit?usp=sharing

https://beta.wikiversity.org/wiki/V%C3%B5rdlustehted_ja_loogikatehted


 """

# ctrl + ä
# shift alt a
# alt shift nool_üles

n = int(input( "kasutaja 1 sisesta nr : " ))

m = int(input( "kasutaja 2 sisesta nr : " ))


if n < m:
    print("kasutaja 1 sisestatud arv (", n, ") on väiksem")
else:
    print("kasutaja 2 sisestatud arv (", m, ") on väiksem")



