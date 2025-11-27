# 2025.10.16_TA-25_Siim_python

# Table of Contents
1. [1. yl nr 7 - modulo tehted kuupäevadega](#1-yl-nr-7---modulo-tehted-kuup%C3%A4evadega)
2. [2.1 Imperatiivne vs Deklaratiivne — Andmefail energy.xml](#21-imperatiivne-vs-deklaratiivne--andmefail-xml)
3. [2.2 Imperatiivne vs Deklaratiivne — Pyhton](#22-imperatiivne-lahendus---python)
4. [2.3 Imperatiivne vs Deklaratiivne — R näitel](#23-imperatiivne-vs-deklaratiivne--r-näitel)
5. [2.4 Imperatiivne vs Deklaratiivne — SQL näitel](#24-imperatiivne-vs-deklaratiivne--sql-näitel)
6. [3-input-küsimine](#3-input-küsimine)
7. [4-stringi-meetod](#4-stringi-meetod)
8. [5-tsükli-näide](#5-tsükli-näide)
9. [6. Sokoban Mängu ehitamine](#6-sokoban-mangu-ehitamine)
10.[7. ICS-faili lugemine ja töötlemine Pythonis](#7-ICS---faili-lugemine-ja-tootlemine-pythonis)
11.[9. Bitwise operaatorid kasutamine bititasemel arvutuste tegemiseks
](#9-bitwise-operaatorid-kasutamine-bititasemel-arvutuste-tegemiseks) 

# 1. yl nr 7 - modulo tehted kuupäevadega

Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. 
(paarisarvu mõiste - odd/even)

```Python
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

```


# 2.1 Imperatiivne vs Deklaratiivne — Andmefail XML

energy.xml

```XML
<root>
  <record>
    <r:DateOfIssue>2024-10-01</r:DateOfIssue>
    <r:ProductionTechnology>Solar</r:ProductionTechnology>
    <r:EnergySource>PV</r:EnergySource>
  </record>
  <record>
    <r:DateOfIssue>2024-10-02</r:DateOfIssue>
    <r:ProductionTechnology>Wind</r:ProductionTechnology>
    <r:EnergySource>Turbine</r:EnergySource>
  </record>
</root>

```

Soovime saada CSV:
```
DateOfIssue,ProductionTechnology,EnergySource
2024-10-01,Solar,PV
2024-10-02,Wind,Turbine
```


## 2.2 Imperatiivne lahendus - Python

```Python
import xml.etree.ElementTree as ET
import csv

# samm 1: XML-faili parsimine
tree = ET.parse("energy.xml")
root = tree.getroot()

# samm 2: tühja listi loomine tulemustele
rows = []

# samm 3: käime läbi kõik <record> elemendid
for rec in root.findall("record"):
    date = rec.find("r:DateOfIssue").text
    tech = rec.find("r:ProductionTechnology").text
    src = rec.find("r:EnergySource").text
    rows.append([date, tech, src])

# samm 4: kirjutame CSV-faili
with open("energy.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["DateOfIssue", "ProductionTechnology", "EnergySource"])
    writer.writerows(rows)
```

🧠 Mis toimub:
- samm-sammuline juhend, kuidas tulemuseni jõuda
- iga samm muudab programmi olekut (rows muutub)
- kood on imperatiivne, sest kirjeldab kuidas teha

## 2.2.2 🧩 2️⃣ Deklaratiivne lahendus (Pythonic, funktsionaalne stiil)

```Python
import xml.etree.ElementTree as ET
import csv

# loeme ja parsimme XML-i
root = ET.parse("energy.xml").getroot()

# kirjeldame *mida* tahame (mitte, kuidas tsüklit käia)
records = [
    {
        "DateOfIssue": rec.find("r:DateOfIssue").text,
        "ProductionTechnology": rec.find("r:ProductionTechnology").text,
        "EnergySource": rec.find("r:EnergySource").text,
    }
    for rec in root.findall("record")
]

# kirjutame CSV ühe väljendiga
with open("energy.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)
```

🧠 Mis toimub:
- kasutame list comprehension (kirjelduslik, mitte sammuline)
- ei loo tühje muutujaid ega muuda olekut
- kogu töö on “kirjelduslik”: “siin on struktuur, mida tahan”

**⚖️ Võrdlus**
| Aspekt         | Imperatiivne                | Deklaratiivne                           |
| -------------- | --------------------------- | --------------------------------------- |
| Stiil          | Samm-sammuline käskude jada | Kirjeldus, *mida* teha                  |
| Kood           | Pikem, muutujatega          | Lühem, väljenduslik                     |
| Oleku muutmine | Jah (`rows.append`)         | Välditakse (kasutatakse väljendeid)     |
| Python-võte    | `for`-tsüklid               | List comprehension, `map`, `DictWriter` |
| Tulemus        | Sama CSV                    | Sama CSV                                |


## 2.3 Imperatiivne vs Deklaratiivne — R näitel



## 2.3.1 🧱 1️⃣ Imperatiivne R-versioon

👉 Samm-sammuline, käske täitev lähenemine.

``` R

library(XML)

# 1. Laeme XML-faili
doc <- xmlParse("energy.xml")
root <- xmlRoot(doc)

# 2. Loome tühjad vektorid
dates <- c()
techs <- c()
sources <- c()

# 3. Käime iga <record> elemendi läbi
records <- getNodeSet(root, "//record")
for (rec in records) {
  date <- xmlValue(rec[["r:DateOfIssue"]])
  tech <- xmlValue(rec[["r:ProductionTechnology"]])
  src  <- xmlValue(rec[["r:EnergySource"]])
  
  dates <- c(dates, date)
  techs <- c(techs, tech)
  sources <- c(sources, src)
}

# 4. Paneme tulemused data.frame’i
df <- data.frame(
  DateOfIssue = dates,
  ProductionTechnology = techs,
  EnergySource = sources,
  stringsAsFactors = FALSE
)

# 5. Kirjutame CSV
write.csv(df, "energy.csv", row.names = FALSE)

```

**🧠 Siin toimub:**
- igal sammul muutub olek (lisame vektoritesse);

- kood kirjeldab kuidas tulemus saadakse;

- tüüpiline imperatiivne mõtlemine: “tee see, siis see, siis see”.



## 2.3.2 Deklaratiivne R-versioon

👉 Kasutame funktsionaalset ja andmepõhist stiili (xml2 + dplyr).

``` R
 
library(xml2)
library(dplyr)

# loe XML ja leia kõik <record> elemendid
records <- read_xml("energy.xml") %>%
  xml_find_all("//record")

# kirjeldame, mida tahame: extrakti iga väli ja loo andmetabel
df <- tibble(
  DateOfIssue = records %>% xml_find_first("r:DateOfIssue") %>% xml_text(),
  ProductionTechnology = records %>% xml_find_first("r:ProductionTechnology") %>% xml_text(),
  EnergySource = records %>% xml_find_first("r:EnergySource") %>% xml_text()
)

# kirjeldame eesmärki: kirjuta CSV
write.csv(df, "energy.csv", row.names = FALSE)

```


**Siin toimub:**
- ei käida käsitsi tsüklit ega lisata elemente vektoritesse;
- kasutatakse andmevoogu (%>%), mis kirjeldab mida teha;
- vältitakse oleku muutmist;
- kood on lühem ja väljenduslikum.

**Võrdlus**
| Aspekt          | Imperatiivne R                         | Deklaratiivne R                     |
| --------------- | -------------------------------------- | ----------------------------------- |
| Fookus          | *Kuidas* samm-sammult tulemuseni jõuda | *Mida* andmetega teha               |
| Kood            | Pikem, tsüklid ja muutujad             | Lühem, voog (pipes) ja funktsioonid |
| Oleku muutmine  | Jah (`dates <- c(...)`)                | Välditakse                          |
| Tüüpiline stiil | Baas-R, `for`, `c()`                   | `dplyr`, `xml2`, `%>%`              |
| Tulemus         | Sama `energy.csv`                      | Sama `energy.csv`                   |


**Tulemus (energy.csv)**
DateOfIssue,ProductionTechnology,EnergySource
2024-10-01,Solar,PV
2024-10-02,Wind,Turbine

kolmas variant, kus deklaratiivne R-kood teeb sama töö üheainsa funktsioonikutsena (purrr ja map_df abil)

## 2.4 Imperatiivne vs Deklaratiivne — SQL näitel

Võtame sama andmenäite, kuid seekord kujutame ette, et andmed on salvestatud andmebaasi tabelisse.  

---
 1. [Sub paragraph](#subparagraph1)

 ### Sub paragraph <a name="subparagraph1"></a>
This is a sub paragraph, formatted in heading 3 style

## 2.4.1 🧩 Imperatiivne lähenemine - Andmed (`energy` tabel)  <a name="Andmed"></a>

| DateOfIssue | ProductionTechnology | EnergySource |
|--------------|----------------------|---------------|
| 2024-10-01   | Solar                | PV            |
| 2024-10-02   | Wind                 | Turbine       |

---

## 2.4.2 🧱 1️⃣ Imperatiivne lähenemine (Python + SQL-ühendus) <a name="Imperat - Python & SQL"></a>

Imperatiivses stiilis sa **kirjutad käsud**, kuidas tulemus saada:
- ühenda andmebaasiga,  
- vali read,  
- loo tsükkel, et need töödelda ja kirjutada CSV.

```python
import sqlite3
import csv

# samm 1: loo ühendus andmebaasiga
conn = sqlite3.connect("energy.db")
cur = conn.cursor()

# samm 2: saada SQL-päring (imperatiivne osa tuleb pärast)
cur.execute("SELECT DateOfIssue, ProductionTechnology, EnergySource FROM energy")

# samm 3: loo CSV-fail ja kirjuta read käsitsi
with open("energy.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["DateOfIssue", "ProductionTechnology", "EnergySource"])
    for row in cur:
        writer.writerow(row)

conn.close()

```

## 2.4.3 🧩 2️⃣ Deklaratiivne lähenemine (puhas SQL) <a name="Dekl - SQL"></a>

SQL ise on deklaratiivne:

Sa ei ütle kuidas andmeid ridade kaupa töödelda, vaid mida tahad saada.

```SQL
SELECT 
  DateOfIssue,
  ProductionTechnology,
  EnergySource
FROM energy
WHERE EnergySource = 'PV'
ORDER BY DateOfIssue;
```

**🧠 Deklaratiivne, sest:**
- sa ei määra, kuidas andmebaas täpselt ridasid läbi käib;
- ütled vaid, mida soovid näha;
- andmebaasi mootor otsustab ise, kuidas päring optimaalselt täita.

## 2.4.3 Deklaratiivne lähenemine - (Lisavariant) Kombineeritud lähenemine Pythonis <a name="Dekl - Python & SQL"></a>

Deklaratiivset SQL-i saab kasutada ka Pythonis nii, et Python ei kontrolli protsessi, vaid lihtsalt “vahendab” tulemust:

``` Python
import sqlite3
import pandas as pd

conn = sqlite3.connect("energy.db")

df = pd.read_sql_query("""
    SELECT DateOfIssue, ProductionTechnology, EnergySource
    FROM energy
    WHERE EnergySource = 'PV'
    ORDER BY DateOfIssue
""", conn)

df.to_csv("energy.csv", index=False)
conn.close()
```

**🧠 Siin:**
- SQL on endiselt deklaratiivne (kirjeldab, mida tahad näha);
- Python lihtsalt käivitab päringu ja salvestab tulemuse;
- tulemuseks on puhtalt deklaratiivse SQL-i väljund CSV-failina.

**⚖️ Võrdlus**

| Aspekt         | Imperatiivne (nt Python + SQL)             | Deklaratiivne (puhas SQL)          |
| -------------- | ------------------------------------------ | ---------------------------------- |
| Fookus         | *Kuidas* andmeid lugeda ja töödelda        | *Mida* tulemus peaks sisaldama     |
| Oleku muutmine | Jah (muutujad, tsüklid)                    | Ei (kirjelduslik, ei muuda olekut) |
| Kontroll       | Täielik kontroll koodi üle                 | Juhtimine antakse andmebaasile     |
| Tüüpiline keel | Python, Java, C, R (imperatiivses stiilis) | SQL                                |
| Tulemus        | CSV fail                                   | Tabel/päringu väljund              |


**🧠 Lühidalt**

- Imperatiivne → “Tee need sammud, et CSV saada.”
- Deklaratiivne (SQL) → “Siin on, mida ma tahan, sina (andmebaas) otsi viis, kuidas seda kõige paremini teha.”


# 3. Input küsimine 

```Python
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

answer = input("Enter an integer: ")
while not answer.isdigit():
# while not answer.isdecimal(): # huvitav mis vahe on isdigit ja isdecimal 
    print("That's not a whole number. Try again.")
    answer = input("Enter an integer: ")
answer = int(answer)




```

# 4. Stringi meetod

```Python
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```

See, mida sa näitasid, on **kaks erinevat viisi stringide vormindamiseks** Pythonis. Mõlemad kuuluvad **imperatiivse programmeerimise** stiili alla, mitte otseselt objektorienteeritud programmeerimise (OOP) alla, kuigi Python ise toetab OOP-d.

---

### 🧩 1. **Lihtne komadega ühendamine (`print` koos `,`)**
```python
price = 49
print("For only", price, "dollars!")
```
- See on **lihtne ja otsekohene** viis stringide ja muutujate ühendamiseks.
- Ei kasuta vormindust, seega ei saa kontrollida nt komakohtade arvu.
- Ei ole objektorienteeritud – lihtsalt käsurea väljund.

---

### 🧩 2. **`str.format()` meetod**
```python
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```
- Kasutab **stringi meetodit**, mis on **objektipõhine** (sest `txt` on `str` objekt ja `.format()` on selle meetod).
- Võimaldab **täpsemat kontrolli**, nt komakohtade arv (`.2f` tähendab 2 kohta pärast koma).
- Seda võib pidada **objektorienteeritud lähenemiseks**, kuna kasutad objekti (`str`) meetodit.

---

### Kokkuvõte:

| Meetod | Vormindus | OOP-seos |
|--------|-----------|----------|
| `print("...", var, "...")` | Vähe kontrolli | Ei ole OOP |
| `"tekst {var}".format(var=...)` | Täpne kontroll | OOP-meetod |

---

Kui soovid, võin näidata ka kolmandat, uuemat viisi: **f-stringid**, mis on veelgi mugavamad:

```python
price = 49
print(f"For only {price:.2f} dollars!")
```




# 5. tsükli näide

```Python
numbers = [1, 2, 3, 4, 5]
squared = []

for n in numbers:
    squared.append(n * n)

print(squared)
```

## 5.2 while tsükkel ja Walrus operaator
vt ka https://www.w3schools.com/python/python_operators_assign.asp

Walrus operaator on omistamisavaldis, et sa saaksid omistada väärtuse ja
seda kasutada samaaegselt ühes avaldises

```Python

print(x := 3) # see on sama mis
# x = 3
# print(x)


## või AI näide 1:

while (n := len(my_list)) > 0:
    print(f"Listis on {n} elementi") # kasutusel str meetod
    my_list.pop()
# # mis on sama nagu:
# n = len(my_list)
# while n > 0:
#     print(f"Listis on {n} elementi")
#     my_list.pop() # NB! txt.pop() on list meetod ehk remove
#     # pop()	Removes the element at the specified position
#     # remove()	Removes the first item with the specified value



## või AI näide 2:
## ilma Walrus operaatorita - kas see peaks töötama?
# while True:
#     user_input = input("Sisesta midagi (või Enter lõpetamiseks): ")
#     if user_input = "":
#         break
#     print(f"Sisestatud: {user_input}")

while (user_input := input ("sisesta")) != "":
    print(f"Sisestatud: {user_input}")


```



# 6. Sokoban mangu ehitamine


Siin on **täielik õppetunni plaan**, mis sobib põhikooli tasemele ja õpetab samm-sammult Sokoban-mängu loomist Pythonis:

***

## **Õppetunni pealkiri:**

**"Ehita oma Sokoban-mäng Pythonis"**

### **Eesmärgid:**

*   Õpilane mõistab, mis on Sokoban ja kuidas mäng töötab.
*   Õpilane õpib:
    *   kasutama **list of lists** struktuuri mänguvälja jaoks,
    *   kirjutama funktsioone (`print_grid`, `move`, `is_win`),
    *   töötama **tingimuslausete** ja **koordinaatidega**,
    *   looma lihtsat mänguloogikat.

***

## **Tunni kestus:**

2 × 45 minutit (võib jagada ka 3 osaks).

***

## **Tunni struktuur:**

### **1. Sissejuhatus (10 min)**

*   Näita valmis Sokoban-mängu terminalis.
*   Selgita reegleid:
    *   Mängija (`Y`) liigub WASD-ga.
    *   Kastid (`B`) tuleb lükata eesmärkidele (`F`).
    *   Seinad (`#`) ei lase liikuda.
*   Küsi: *Mis juhtub, kui kast on seina ees?* (ei saa lükata).

***

### **2. Planeerimine (10 min)**

*   Joonista paberile mänguväli (grid).
*   Selgita, et Pythonis teeme selle **list of lists** kujul.
*   Sümbolid: `#`, `.`, `F`, `B`, `Y`.

***

### **3. Samm-sammuline ehitamine**

#### **Samm 1: Mänguvälja printimine (15 min)**

*   Näita koodi:
    ```python
    grid = [
        list("#######"),
        list("#F.####"),
        list("#FB...#"),
        list("#YB.B.#"),
        list("###F..#"),
        list("#######")
    ]

    def print_grid():
        for row in grid:
            print(" ".join(row))
        print()

    print_grid()
    ```
*   Harjutus: Muuda sümboleid ja prindi uuesti.

***

#### **Samm 2: Leia mängija ja eesmärgid (10 min)**

*   Näita, kuidas leida `Y` ja `F`:
    ```python
    player_pos = (3, 1)
    goals = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "F"]
    print(goals)
    ```
*   Selgita, mis on **koordinaadid**.

***

#### **Samm 3: Liikumine ilma kastideta (15 min)**

*   Lisa WASD sisend ja liikumine:
    ```python
    def move(dx, dy):
        global player_pos
        x, y = player_pos
        nx, ny = x + dx, y + dy
        if grid[nx][ny] in [".", "F"]:
            grid[nx][ny] = "Y"
            grid[x][y] = "." if (x, y) not in goals else "F"
            player_pos = (nx, ny)
    ```
*   Harjutus: Mis juhtub, kui liigud seina sisse? (Lisa kontroll `if grid[nx][ny] == "#": return`).

***

#### **Samm 4: Kastide lükkamine (15 min)**

*   Näita loogikat:
    ```python
    if grid[nx][ny] == "B":
        bx, by = nx + dx, ny + dy
        if grid[bx][by] in [".", "F"]:
            grid[bx][by] = "B"
            grid[nx][ny] = "Y"
            grid[x][y] = "." if (x, y) not in goals else "F"
            player_pos = (nx, ny)
    ```
*   Harjutus: Mis juhtub, kui kast on seina ees?

***

#### **Samm 5: Võidutingimus (10 min)**

*   Funktsioon:
    ```python
    def is_win():
        return all(grid[x][y] == "B" for (x, y) in goals)
    ```
*   Kui `is_win()` on `True`, prindi: **"Tubli! Kõik kastid on kohal!"**

***

### **4. Lõpetus ja laiendused (10 min)**

*   Lisa:
    *   Värvid (`colorama`).
    *   Mitme leveli tugi.
    *   Undo funktsioon.
*   Kodune töö: Tee oma level ja jaga klassiga.

***

## **Harjutused tunni jooksul**

*   Muuda mänguvälja ja testi.
*   Lisa kontroll, et mängija ei lähe seina sisse.
*   Tee funktsioon, mis loeb kastide arvu.

***

## **Lisategevused (edukatele)**

*   Lisa **levelite fail** ja loe see sisse.
*   Tee **punktisüsteem** (liikumiste arv).
*   Lisa **menüü**: “Uus mäng”, “Välju”.

***

Kas soovid, et ma **koostan valmis töövihiku** (PDF või Word), kus on:

*   **koodi osad**,
*   **selgitused**,
*   **harjutused ja küsimused**,
*   **laienduste ideed**?  
    Või pigem **PowerPoint slaidid**, et saaksid tunnis näidata?



# 7. ICS-faili lugemine ja töötlemine Pythonis

ICS (iCalendar) failid on tekstipõhised ja sisaldavad kalendri sündmuste infot. Pythonis saab neid töödelda mitme teegi abil, näiteks **`icalendar`** või **`ics`**.

---

## ✅ 1. Lugemine `icalendar` teegiga

See variant ei tööta

```python
from icalendar import Calendar

# Loe ICS-fail
with open("sündmus.ics", "rb") as f:
    cal = Calendar.from_ical(f.read())

# Itereeri sündmuste üle
for component in cal.walk():
    if component.name == "VEVENT":
        summary = component.get("SUMMARY")
        start = component.get("DTSTART").dt
        end = component.get("DTEND").dt
        location = component.get("LOCATION")
        print(f"Sündmus: {summary}")
        print(f"Algus: {start}, Lõpp: {end}")
        print(f"Asukoht: {location}")
```

Selgitus:

Calendar.from_ical() loeb ICS-faili sisu.
component.name == "VEVENT" filtreerib sündmused.
.dt teisendab kuupäeva Python datetime objektiks.


**2. Lugemine ics teegiga (lihtsam)**

```python
from ics import Calendar

with open("sündmus.ics", "r", encoding="utf-8") as f:
    c = Calendar(f.read())

for event in c.events:
    print(f"Sündmus: {event.name}")
    print(f"Algus: {event.begin}, Lõpp: {event.end}")
    print(f"Asukoht: {event.location}")
```
**Selgitus:**

ics teek on lihtsam ja otsekohesem.
event.begin ja event.end on Arrow objektid (mugav kuupäevade käsitlemiseks).


## 7.2.1 TÖÖTAV ilma teegita

```Python
events = []
event = {}

with open("2025-11-17-15-15-04.ics", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "BEGIN:VEVENT":
            event = {}
        elif line.startswith("SUMMARY:"):
            event["summary"] = line.replace("SUMMARY:", "")
        elif line.startswith("DTSTART:"):
            event["start"] = line.replace("DTSTART:", "")
        elif line.startswith("DTEND:"):
            event["end"] = line.replace("DTEND:", "")
        elif line.startswith("LOCATION:"):
            event["location"] = line.replace("LOCATION:", "")
        elif line == "END:VEVENT":
            events.append(event)

# Näita tulemusi
for e in events:
    print(f"Sündmus: {e.get('summary')}")
    print(f"Algus: {e.get('start')}, Lõpp: {e.get('end')}")
    print(f"Asukoht: {e.get('location')}")
    print("-" * 30)

```


## 7.2.2 puhasta
```Python
# Puhastatud sisu salvestamiseks
isPuhastatudFail = []


# Faili puhastamine
allowed_keys = {"BEGIN:VEVENT", "END:VEVENT", "UID", "DTSTAMP", "DTSTART", "DTEND", "SUMMARY", "DESCRIPTION", "LOCATION"}
cleaned_lines = []

with open("2025-11-17-15-15-04.ics", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue  # Jäta tühjad read vahele
        # Kontrolli, kas rida algab mõne lubatud võtmega
        for key in allowed_keys:
            if line.startswith(key):
                isPuhastatudFail.append(line)
                break

# # Salvesta puhastatud fail
# with open("puhastatud.ics", "w", encoding="utf-8") as f:
#     for l in cleaned_lines:
#         f.write(l + "\n")

# print("Fail puhastatud ja salvestatud nimega puhastatud.ics")


# Kontrollime tulemust
print("Puhastatud objekt:")
for l in isPuhastatudFail:
    print(l)


```

## 7.2.3 väljade järjekord


```Python

# Väljade järjekord
order = ["BEGIN:VEVENT", "UID", "DTSTAMP", "DTSTART", "DTEND", "SUMMARY", "DESCRIPTION", "LOCATION", "END:VEVENT"]

isRidaFail = []
current_event = []

for line in isPuhastatudFail:
    if line == "BEGIN:VEVENT":
        current_event = [line]  # Alusta uut sündmust
    elif line == "END:VEVENT":
        current_event.append(line)
        # Liida kõik väljad ühte stringi, komadega eraldatult
        isRidaFail.append(", ".join(current_event))
        current_event = []
    else:
        current_event.append(line)

# Kontrollime tulemust
print("isRidaFail:")
for rida in isRidaFail:
    print(rida)

```


## 7.2.4 filtreerimine

mingi filtreerimine

```Python

### filtreerimine 
filtered_lines = []

for line in isPuhastatudFail:
# with open("2025-11-17-15-15-04.ics", "r", encoding="utf-8") as f:
    # for line in f:
        line = line.strip()
        if line.startswith("DTSTAMP:202511"):
            # Eralda võtme ja väärtuse
            # key, value = line.split(":", 1)
            # year = value[0:4]
            # month = value[4:6]

            # # Kontrolli tingimust
            # if year == "2025" and month == "11":
                filtered_lines.append(line)

# Näita tulemusi
for l in filtered_lines:
    print(l)

```


# 8. COPY eripära Python



---


See näitab, et lihtne omistamine loob viite, mitte koopiat, ja .copy() teeb pindmise koopia.

```python

### COPY eripära Pyhton
list1 = [1, 3, 4, 5, 6]
list2 = list1

list2[2] = 10
print(list1)
print(list2)

list3 = list2.copy()
list3[3] = 1000

print(list1)
print(list2)
print(list3)


```



# 9. Bitwise operaatorid kasutamine bititasemel arvutuste tegemiseks

Bitwise operaatorid töötavad otse binaarsete bittidega (0 ja 1). Need on kasulikud madala taseme operatsioonides, optimeerimisel ja olukordades, kus on vaja kiiresti kontrollida või muuta arvude bitte.

---

## 1. Kontrollimine, kas arv on paaris või mitte

```python
x = 10
if x & 1 == 0:
    print("Paaris")
else:
    print("Mittepaaris")
```

**Selgitus:**  
`x & 1` kontrollib viimast bitti. Kui see on 0 → arv on paaris, kui 1 → arv on paaritu.

---

## 2. Lippude (flags) haldamine

```python
READ = 0b0001
WRITE = 0b0010

permissions = READ | WRITE  # lubame mõlemad
print(permissions)  # 3

# Kontrollime, kas WRITE on lubatud
if permissions & WRITE:
    print("Kirjutamine lubatud")
```

**Selgitus:**  
Bitwise operaatorid on kiired ja mälusäästlikud, kui hoiad mitut olekut ühes arvus.

---

## 3. Kiire korrutamine/jagamine kahekordsete arvudega

```python
x = 5
print(x << 1)  # 10 (nihutus vasakule = korrutamine 2-ga)
print(x >> 1)  # 2  (nihutus paremale = jagamine 2-ga)
```

**Selgitus:**  
`<<` nihutab bitte vasakule (korrutab 2-ga), `>>` nihutab paremale (jagab 2-ga).

---

## 4. Maskimine

```python
x = 29  # binaarselt: 11101
mask = 0b1111
print(x & mask)  # 13 (1101)
```

**Selgitus:**  
Maskimine võimaldab võtta ainult teatud bitid (näiteks viimased 4 bitti).

---

## Kokkuvõte

- `&` → AND (kontrollib bitte)
- `|` → OR (ühendab bitte)
- `^` → XOR (erinevad bitid)
- `<<` → nihuta vasakule (korruta 2-ga)
- `>>` → nihuta paremale (jaga 2-ga)

Bitwise operaatorid on kasulikud:
- Paaris/mitterpaaris kontroll
- Lippude haldus
- Kiire korrutamine/jagamine
- Maskimine ja bititaseme manipulatsioon




# 10. Copilot prompt
Palun anna vastus ühesainsas koodiplokis. Kasuta Markdown-formaati. Lisa Python-koodi näited Markdowni sees (kasuta ```python``` blokke). Ära lisa väljaspool koodiplokki mitte ühtegi teksti ega kommentaari. 

Näide, kui sul on konkreetne struktuur:
Palun anna vastus ühesainsas koodiplokis. Kasuta Markdown-formaati ja loo hierarhia:
h1 - [Pealkiri]
h2 - [Alapealkiri 1]
h2 - [Alapealkiri 2]
...
Lisa iga alapealkirja alla Python-koodi näide (kasuta ```python``` blokke). Ära lisa väljaspool koodiplokki mitte ühtegi teksti ega kommentaari.


# 11. Regex - cheatsheet


Regex Basics
Symbol	Meaning
.	any character except newline
*	Match 0 or more characters
+	Match 1 or more characters
?	Match 0 or 1 characters
[abc]	Any of a,b or c
[^abc]	not a,b or c
[a-z]	Any of a to z
^$	Start and end of string
\w\d\s	word, digit, whitespace
\W\D\S	not word, digit, whitespace
a{5}a{2,}	exactly five, two or more
a{1,3}	between one & three


# Vahe enne lõppu


# LOPP



