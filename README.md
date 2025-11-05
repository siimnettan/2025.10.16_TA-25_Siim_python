# 2025.10.16_TA-25_Siim_python

# Table of Contents
2.1 Imperatiivne vs Deklaratiivne — Andmefail energy.xml
2.2 [](Imperatiivne vs Deklaratiivne — Pyhton)
2.3 [](Imperatiivne vs Deklaratiivne — R näitel)
2.4 [2.3 Imperatiivne vs Deklaratiivne](# Imperatiivne vs Deklaratiivne — SQL näitel)
2. [Example2](##Andmed - energy tabel)
3. [Third Example](# Imperatiivne lähenemine - Python + SQL-ühendus)
4. [Fourth Example](# Deklaratiivne lähenemine - puhas SQL)
5. [Viies Example]( Deklaratiivne lähenemine - Kombineeritud lähenemine Pythonis)

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


# 2.2 Imperatiivne lahendus - Python

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


# 2.3 Imperatiivne vs Deklaratiivne — R näitel



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

# 2.4 Imperatiivne vs Deklaratiivne — SQL näitel

Võtame sama andmenäite, kuid seekord kujutame ette, et andmed on salvestatud andmebaasi tabelisse.  

---

## 2.4.1 🧩 Imperatiivne lähenemine - Andmed (`energy` tabel)

| DateOfIssue | ProductionTechnology | EnergySource |
|--------------|----------------------|---------------|
| 2024-10-01   | Solar                | PV            |
| 2024-10-02   | Wind                 | Turbine       |

---

## 2.4.2 🧱 1️⃣ Imperatiivne lähenemine (Python + SQL-ühendus)

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

## 2.4.3 🧩 2️⃣ Deklaratiivne lähenemine (puhas SQL)

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

### 2.4.3 Deklaratiivne lähenemine - (Lisavariant) Kombineeritud lähenemine Pythonis

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