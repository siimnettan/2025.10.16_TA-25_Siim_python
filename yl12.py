
#-----------------------------------------------------
# --- # yl10.py
#-----------------------------------------------------
""" 
Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
Väljasta listi esimene väärtus
Lisa listi lõppu uus puuvili
Väljasta listi viimane väärtus
Muuda ühe elemendi väärtust ja väljasta kogu list
Kontrolli kas väärtus (näiteks õun) eksisteerib listis
Väljasta listi pikkus
Eemalda listist element ja väljasta kogu list
Muuda listi järjekord vastupidiseks
Sorteeri list ja väljasta
(jada, list, listi element, listi meetodid)

"""
## TRIKID:
# ctrl + ä
# shift alt a
# alt shift nool_üles

#-----------------------------------------------------
# --- 
#-----------------------------------------------------

fruit_list = ["pear", "banana", "apple", "cherry"]

# Väljasta listi esimene väärtus
print(fruit_list[0])

# Lisa listi lõppu uus puuvili

fruit_list.append("orange")

print(len(fruit_list))

## Väljasta listi viimane väärtus
# print(fruit_list[len(fruit_list)-1])
print(fruit_list[-1])

# Muuda ühe elemendi väärtust ja väljasta kogu list
fruit_list[2] = "fig"
print(fruit_list)

# Kontrolli kas väärtus (näiteks õun) eksisteerib listis

# if "apple" in fruit_list:
#     print("jah on listis")
# else:
#     print("nope")


# Väljasta listi pikkus
print(len(fruit_list))

# Eemalda listist element ja väljasta kogu list

# fruit_list.remove("apple")

print(fruit_list)

# Muuda listi järjekord vastupidiseks   

print(sorted(fruit_list))

# fruit_list = fruit_list.sort() # see on fruit list sort
print(fruit_list)
# print(fruit_list.sort(reverse=True))

fruit_list.sort(reverse=True) 
print(fruit_list)



# # Sorteeri list ja väljasta
# print(fruit_list)
# print(fruit_list[1:3]) # kolmandat ei kaasata

# # slice 
# print(fruit_list[1:]) # 1st lõpuni
# print(fruit_list[:3]) # algusest 2-ni
# print(fruit_list[::2]) # üle ühe
# print(fruit_list[-1:-2:2]) # üle ühe


#### COPY eripära Pyhton
# list1 = [1, 3, 4, 5, 6]
# list2 = list1

# list2[2] = 10
# print(list1)
# print(list2)

# list3 = list2.copy()
# list3[3] = 1000

# print(list1)
# print(list2)
# print(list3)


#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------