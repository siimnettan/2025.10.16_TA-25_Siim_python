# yl6
""" 
Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). (loogikatehted - logic operators)


 """

# ctrl + ä
# shift alt a
# alt shift nool_üles

n = int(input( "kasutaja 1 sisesta nr : " ))

m = int(input( "kasutaja 2 sisesta nr : " ))

k = int(input( "kasutaja 3 sisesta nr : " ))



# if n > m:
#     if n > k:
#         print("kasutaja 1 sisestatud arv (", n, ") on suurem kui teiste sisestatud arvud")
#     else:
#         print("kasutaja 3 sisestatud arv (", k, ") on suurem kui teiste sisestatud arvud")
# else:
#     if m > k:
#         print("kasutaja 2 sisestatud arv (", m, ") on suurem kui teiste sisestatud arvud")
#     else:
#         print("kasutaja 3 sisestatud arv (", k, ") on suurem kui teiste sisestatud arvud")
#         

# if n > m and n > k:
#         print("kasutaja 1 sisestatud arv (", n, ") on suurem kui teiste sisestatud arvud")
# elif m > n and m > k: 
#         print("kasutaja 2 sisestatud arv (", m, ") on suurem kui teiste sisestatud arvud")
# elif k > n and k > m:
#         print("kasutaja 3 sisestatud arv (", k, ") on suurem kui teiste sisestatud arvud")

### see variant ei tööta
# if n > (m or k):

# if n > (m and k):
#         print("kasutaja 1 sisestatud arv (", n, ") on suurem kui teiste sisestatud arvud")
# elif m > (n and k):
#         print("kasutaja 2 sisestatud arv (", m, ") on suurem kui teiste sisestatud arvud")
# elif k > (n and m):
#         print("kasutaja 3 sisestatud arv (", k, ") on suurem kui teiste sisestatud arvud")


if n > m > k or n > k > m:
        print("kasutaja 1 sisestatud arv (", n, ") on suurem kui teiste sisestatud arvud")
elif m > n > k or m > k > n:
        print("kasutaja 2 sisestatud arv (", m, ") on suurem kui teiste sisestatud arvud")
elif k > n > m or k > m > n:
        print("kasutaja 3 sisestatud arv (", k, ") on suurem kui teiste sisestatud arvud")



