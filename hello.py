# ctrl + ä
# shift alt a

print("tere kuressaare")


a= "tere kuressaare"
b= " "
c= "mf"

print(a+b+c)

n = int(input( "Sisesta isikukood: " ))


import re
if re.search("^[1-6][0-9]{10}$", n):
#if re.search("[1]{5}", n):
    print("on Eesti isikukood")

else:
    print("ei ole eesti isikukood")


