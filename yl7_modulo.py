# yl7_modulo
""" 
Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. 
(paarisarvu mõiste - odd/even)
"""

## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles

n = int(input( "kasutaja 1 sisesta nr : " ))


if n % 2:
        print("kasutaja 1 sisestatud arv (", n, ") on paaritu")
else:
        print("paaris arv")


#-----------------------------------------------------
# --- OPI ---
#-----------------------------------------------------
# ### modulo operaatorit % saab kasutada kellaaegade ümberarvutustes:

# # 1. 24-tunnise kellaaja normaliseerimine
# Kui sul on tundide arv, mis ületab 24 (näiteks 27 tundi), siis modulo abil saad selle tagasi tavapärasesse 24-tunnisesse formaati:

# tunnid = 27
# kellaaeg = tunnid % 24  # Tulemus: 3

# Selgitus: 27 tundi tähendab 1 ööpäev + 3 tundi → kellaaeg on 03:00.

# #2. Kellaaeg pärast kindlat ajavahemikku
# Kui soovid teada, mis kell on näiteks 50 tunni pärast, ja praegune kellaaeg on 10:00:

# praegune_kell = 10
# hiljem = (praegune_kell + 50) % 24  # Tulemus: 12

# Selgitus: 10 + 50 = 60 → 60 % 24 = 12 → kell on 12:00.

# #3. Minutite ümberarvutus tundideks ja minutiteks
# Kui sul on näiteks 130 minutit ja tahad selle jagada tundideks ja minutiteks:

# minutid = 130
# tunnid = minutid // 60         # Tulemus: 2
# alles_jäänud_minutid = minutid % 60  # Tulemus: 10

# Selgitus: 130 minutit = 2 tundi ja 10 minutit.


# ### Modulo operaatorit saab väga hästi kasutada nädalapäevade arvutamisel, kuna nädalas on 7 päeva ja % 7 aitab tsükliliselt liikuda läbi nädalapäevade.
# Näide: Mis päev on X päeva pärast?
# Oletame, et täna on teisipäev (päev nr 2, kui loeme:
# 0 = pühapäev,
# 1 = esmaspäev,
# 2 = teisipäev,
# ...
# 6 = laupäev).
# Kui tahame teada, mis päev on 10 päeva pärast, siis:
# Pythontänane_päev = 2  # teisipäevpäeva_nr = (tänane_päev + 10) % 7  # Tulemus: 5Show more lines
# Tulemus: päev nr 5 = reede

# Teine näide: Mis päev oli X päeva tagasi?
# Kui tahame teada, mis päev oli 9 päeva tagasi, ja täna on neljapäev (päev nr 4):
# Pythontänane_päev = 4  # neljapäevpäeva_nr = (tänane_päev - 9) % 7  # Tulemus: 2Show more lines
# Tulemus: päev nr 2 = teisipäev
# NB! Kui tulemus on negatiivne, siis % operaator tagastab positiivse jäägi (sõltuvalt keelest – Pythonis see töötab hästi).

# Kolmas näide: Päevade loend tsüklis
# Kui sul on loend päevadest ja tahad liikuda edasi tsükliliselt:
# Pythonpäevad = ["P", "E", "T", "K", "N", "R", "L"]algus = 6  # Laupäevfor i in range(10):    print(päevad[(algus + i) % 7])Show more lines
# Tulemus: Laupäev, Pühapäev, Esmaspäev, ..., Tsükliliselt edasi.

#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------