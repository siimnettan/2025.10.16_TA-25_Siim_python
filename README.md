# 2025.10.16_TA-25_Siim_python

# Table of Contents
1. [Example](# Imperatiivne vs Deklaratiivne — SQL näitel)
2. [Example2](## Andmed - energy tabel)
3. [Third Example](# Imperatiivne lähenemine - Python + SQL-ühendus)
4. [Fourth Example](# Deklaratiivne lähenemine - puhas SQL)
5. [Viies Example](## Võrdlus)

# Imperatiivne vs Deklaratiivne — SQL näitel

Võtame sama andmenäite, kuid seekord kujutame ette, et andmed on salvestatud andmebaasi tabelisse.  

---

## 🧩 Andmed (`energy` tabel)

| DateOfIssue | ProductionTechnology | EnergySource |
|--------------|----------------------|---------------|
| 2024-10-01   | Solar                | PV            |
| 2024-10-02   | Wind                 | Turbine       |

---

# 🧱 1️⃣ Imperatiivne lähenemine (Python + SQL-ühendus)

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

# 🧩 2️⃣ Deklaratiivne lähenemine (puhas SQL)

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

### 🧠 Deklaratiivne, sest:

sa ei määra, kuidas andmebaas täpselt ridasid läbi käib;

ütled vaid, mida soovid näha;

andmebaasi mootor otsustab ise, kuidas päring optimaalselt täita.

## ⚖️ Võrdlus
| Aspekt         | Imperatiivne (nt Python + SQL)             | Deklaratiivne (puhas SQL)          |
| -------------- | ------------------------------------------ | ---------------------------------- |
| Fookus         | *Kuidas* andmeid lugeda ja töödelda        | *Mida* tulemus peaks sisaldama     |
| Oleku muutmine | Jah (muutujad, tsüklid)                    | Ei (kirjelduslik, ei muuda olekut) |
| Kontroll       | Täielik kontroll koodi üle                 | Juhtimine antakse andmebaasile     |
| Tüüpiline keel | Python, Java, C, R (imperatiivses stiilis) | SQL                                |
| Tulemus        | CSV fail                                   | Tabel/päringu väljund              |


### 🧠 Lühidalt

Imperatiivne → “Tee need sammud, et CSV saada.”

Deklaratiivne (SQL) → “Siin on, mida ma tahan, sina (andmebaas) otsi viis, kuidas seda kõige paremini teha.”