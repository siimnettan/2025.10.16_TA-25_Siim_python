#-----------------------------------------------------
# --- # yl26.py
#-----------------------------------------------------
""" 
https://www.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/

Lisatasu arvutamise ülesanne. Alusta algoritmi koostamisest. 
Kommentaarides on kah lahendused, aga proovi ise lahendada. 
Defineeri lisatasu arvutamise funktsioon. 
Sisendina defineeri dictionary.

"""
## TRIKID:
# File → Preferences → Keyboard Shortcuts.
# Toggle line comment:  ctrl shift 7 # eelmisel arvutil:ctrl + ä
# Toggle block comment: shift alt a

# Add cursor Above: ctrl shift uparrow
# copy line down: alt shift nool_alla
# method puhul saab kasutada loogikat OBJEKT.METHOD()

#-----------------------------------------------------
# --- 
#-----------------------------------------------------

# Sales people get paid using the following formula for the total commission: 
# commission is 6.2% of profit, 
# with no commission for any product to total less than zero.
# Input Description

# You'll be given two matrices showing the sales figure per salesperson for each product they sold, 
# and the expenses by product per salesperson. Example:

# Revenue 

#         Frank   Jane
# Tea       120    145
# Coffee    243    265

# Expenses

#         Frank   Jane
# Tea       130     59
# Coffee    143    198

# #Your program should calculate the commission for each salesperson for the month. Example:
#                 Frank   Jane
# Commission       6.20   9.49

# Revenue

#             Johnver Vanston Danbree Vansey  Mundyke
# Tea             190     140    1926     14      143
# Coffee          325      19     293   1491      162
# Water           682      14     852     56      659
# Milk            829     140     609    120       87

# Expenses

#             Johnver Vanston Danbree Vansey  Mundyke
# Tea             120      65     890     54      430
# Coffee          300      10      23    802      235
# Water            50     299    1290     12      145
# Milk             67     254      89    129       76


# Revenue				
# 	Tea	Coffee	Water	Milk
data_big = {
"Johnver": {  	
  "revenue": {   "Tea": 190, "Coffee":	325, "Water":	682, "Milk":	829},
  "expenses":	{"Tea":120,	"Coffee":300,	"Water":50, 	"Milk":67}
  },
"Vanston": {  	
  "revenue": {   "Tea": 140, "Coffee":	19, "Water":	14, "Milk":	140},
  "expenses":	{"Tea":65,	"Coffee":10,	"Water":299, 	"Milk":254}
  },
"Danbree": {  	
  "revenue": {   "Tea": 1926, "Coffee":	293, "Water":	852, "Milk":	609},
  "expenses":	{"Tea":890,	"Coffee":23,	"Water":1290, 	"Milk":89}
  },
"Vansey" : {    
  "revenue": {   "Tea": 14, "Coffee":	1491, "Water":	56, "Milk":	120},
  "expenses":	{"Tea":54,	"Coffee":802,	"Water":12, 	"Milk":129}
  },
"Mundyke": {  	
  "revenue": {   "Tea": 143, "Coffee":	162, "Water":	659, "Milk":	87},
  "expenses":	{"Tea":430,	"Coffee":235,	"Water":145, 	"Milk":76}
  }
				
}
				
commission_rate = 6.2/100
results = {}
profit = {}
commission = {}

def calc_profit():
    profit = revenue - expenses
    if profit <= 0:
        profit = 0
    else:
        profit = profit
    commission = profit * commission_rate 

for person, values in data_big.items():
    revenue = values["revenue"]
    expenses = values["expenses"]

    print(revenue)
    print(expenses)

    
    profit = {}

    for product in revenue:
        p = revenue[product] - expenses[product]
        profit[product] = p
    
    results[person] = {
        "profit": profit
    }

print(results)

# # ###     versioon 3
# data = {
# "Frank":{"revenue" : {"Tea":120, "Coffee":243},
#     "expenses" : {"Tea":130, "Coffee":143}
#     },
# "Jane": {  
#     "revenue" : {"Tea":145, "Coffee":265},
#     "expenses" : {"Tea":59, "Coffee":198}
#     }
# } 
# print(data)

# results = {} # tühi dictionary
# commission_rate = 6.2/100

# for person, values in data.items():
#     # teeb 
#     # {'Tea': 120, 'Coffee': 243} <class 'dict'>
#     # {'Tea': 130, 'Coffee': 143}
#     # {'Tea': 145, 'Coffee': 265} <class 'dict'>
#     # {'Tea': 59, 'Coffee': 198}
#     print(revenue:= values["revenue"])
#     print(expenses:= values["expenses"])

#     profit = {}
#     commission = {}

#     for product in revenue:
#         p = revenue[product] - expenses[product]
#         profit[product] = p
#         commission[product] = max(p * commission_rate, 0)

#     results[person] = { 
#         "profit" : profit,
#         "commission" : commission
#     }

# print(results)



# # ###     versioon 2
 
# revenue = {"Tea":120, "Coffee":243}
# expenses = {"Tea":130, "Coffee":143}
# profit = {} # tühi dictionary
# commission = {}

# for r in revenue:
#     profit[r] = revenue[r] - expenses[r]
#     if profit[r] <= 0:
#         profit[r] = 0
#     else:
#         profit[r] = profit[r]
#     commission[r] = profit[r] * 6.2 /100

# print(profit, commission)

                                 
# ###     versioon 1                                 
##  Frank   Jane # Commission       6.20   9.49
# revenue = {"Tea":120, "Coffee":243}
# expenses = {"Tea":130, "Coffee":143}
# profit = {"Tea":130, "Coffee":143}
# profit.clear()
# profit["Tea"] = revenue["Tea"]- expenses["Tea"]
# if profit["Tea"] <= 0:
#     profit["Tea"] = 0
# else:
#     profit["Tea"] = profit["Tea"]
# profit["Coffee"] = revenue["Coffee"]- expenses["Coffee"]
# if profit["Coffee"] <= 0:
#     profit["Coffee"] = 0
# else:
#     profit["Coffee"] = profit["Coffee"]

# #
# commission = {"Tea":130, "Coffee":143} 
# commission.clear()
# commission["Tea"] = profit["Tea"] * 6.2 /100
# commission["Coffee"] = profit["Coffee"] * 6.2 /100
# # 

# print(revenue, expenses, profit, commission)







#### OPI objekti nimi


# **Reegel:**  
# `[Täpsustav osa]_[Põhisõna]`


### Miks number_value ja mitte value_number?
# Inglise keeles põhisõna tuleb tavaliselt lõppu, täpsustav osa ette.
# Siin põhisõna on value (väärtus), täpsustav osa on number (mis tüüpi väärtus).
# number_value = väärtus, mis on number.
# value_number kõlaks nagu "väärtuse järjekorranumber" (teine tähendus).

### Miks input_number ja mitte number_input?
# Põhisõna on number, täpsustav osa on input (kust see tuleb).
# input_number = number, mis on sisestatud.
# number_input kõlaks nagu "sisestus, mis on number" (võib segadust tekitada, sest input on tegevus).

#####
### Kui tahad lihtsalt hoida vahemikku:
# number_range
# range_values
# sequence_range

# Kui see on mõeldud iteratsiooniks:
# iteration_range
# loop_range

# Kui plaanid hiljem muuta selle juhuslikuks (nt shuffle):
# range_list (ja hiljem random.shuffle(range_list))




#-----------------------------------------------------
# --- LOPP ---
#-----------------------------------------------------

