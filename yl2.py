# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja 
# arvutab ringi pindala ja ümbermõõdu. (math.pi)

import math

n = int(input( "palun anna raadius: " ))

ringi_pind = math.sqrt(n) * math.pi

print("See ringi pindala", str(round(ringi_pind, 1)))


