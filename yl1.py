# yl1
# Kirjuta programm, mis teisendab kasutaja poolt 
# kroonides sisestatud summa eurodesse ja väljastab 
# ümardatud tulemuse. (round)

n = int(input( "Sisesta kroonid: " ))

eurod = n / 15.6

print("See teeb eurodes", str(round(eurod)))

