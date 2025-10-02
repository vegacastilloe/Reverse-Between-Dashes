# 🔁 Reverse Between Dashes — pandas mini-script 

![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/Reverse-Between-Dashes)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 Every Other Day Excel and Power Query Challenges No304 🌟
- 🌟 **Author**: Omid Motamedisedeh

    - In the question table, reverse the characters of any substring that appears between two "-" symbols.

 🔰 Este script aplica una transformación específica sobre cadenas en un DataFrame: **invierte cualquier subcadena que esté entre dos guiones (`-`)**.

 🔗 Link to Excel file:
 👉 https://lnkd.in/gXAfG9yq

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/Reverse-Between-Dashes/blob/main/reverse_between_dashes.py

---
---

## Reverse Between Dashes — pandas mini-script

Este script aplica una transformación específica sobre cadenas en un DataFrame: **invierte cualquier subcadena que esté entre dos guiones (`-`)**. Ideal para limpieza de datos, validación de lógica y enseñanza de manipulación de strings en Python.

## 📦 Requisitos

- Python 3.9+
- Paquetes:
- pandas openpyxl (para leer .xlsx)
- tabulate (solo para impresión bonita)
- Archivo Excel con al menos:
    - La columna: `Question`.
    - En la columna 2: resultados esperados para comparación

---

## 🚀 Cómo funciona

1. Carga de archivo Excel con pandas.read_excel.
2. Limpieza de nombres de columnas (str.strip).
3. Selección de columna objetivo.
4. Aplicación de la función reverse_between_dashes.
5. Comparación contra columna de prueba.
6. Concatenación de resultados y comparación.
7. Visualización con tabulate en formato fancy_grid.

---

## 📤 Salida

El script imprime un DataFrame con:

- `Question`
- Columna esperadas desde el Excel
- `Result del df_final`
- Columna `Match` con valores `True` o `False`

---

## 🧹 Output:

|Question|Result|Esperado|Match|
|-|-|-|-|
|AB-XYZ-CD|AB-ZYX-CD|AB-ZYX-CD|True|
|12-345-67|12-543-67|12-543-67|True|
|HELLO-WORLD-2025-12|HELLO-DLROW-5202-12|HELLO-DLROW-5202-12|True|
|X-ABC-Y|X-CBA-Y|X-CBA-Y|True|
|DATA-1234-SCI|DATA-4321-SCI|DATA-4321-SCI|True|

---

## 🛠️ Personalización

Puedes adaptar el script para:

- Aplicar reglas más complejas
- Exportar el resultado a Excel o CSV

---

## 🚀 Ejecución

import pandas as pd
from tabulate import tabulate

###  🧩 Datos originales
```python
df_raw = pd.read_excel(xl, header=0)
df_raw.columns = df_raw.columns.str.strip()
df = df_raw.iloc[:, 1]
```
### 🧠 Función para la aplicación de reverse_between_dashes
```python
def reverse_between_dashes(s):
    parts = s.split('-')
    for i in range(1, len(parts) - 1):
        parts[i] = parts[i][::-1]
    return '-'.join(parts)
```
### 📊 Resultado y creación del DataFrame
```python
result = [reverse_between_dashes(item) for item in df]
df_final = pd.DataFrame(result)
df_final.columns = ['Result']
```

### 🧪 Comparación con columnas esperadas
```python
test = df_raw.iloc[:, 2:].rename(columns=lambda  x : x.replace('.1', ''))
comparison = df_final == test
df_final = pd.concat([df, df_final, test, comparison], axis=1)
print(tabulate(df_final, headers='keys', tablefmt='fancy_grid'))
```

### 💾 Exportación opcional
```python
# df_input.to_excel("reverse_between_dashes_output.xlsx", index=False)
```
---
### 📄 Licencia
---
Este proyecto está bajo ![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg). Puedes usarlo, modificarlo y distribuirlo libremente.

---
