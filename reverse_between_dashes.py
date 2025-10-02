import pandas as pd
from tabulate import tabulate

#  🧩 Datos originales
df_raw = pd.read_excel(xl, header=0)
df_raw.columns = df_raw.columns.str.strip()
df = df_raw.iloc[:, 1]

# 🧠 Función para la aplicación de reverse_between_dashes
def reverse_between_dashes(s):
    parts = s.split('-')
    for i in range(1, len(parts) - 1):
        parts[i] = parts[i][::-1]
    return '-'.join(parts)

# 📊 Resultado y creación del DataFrame
result = [reverse_between_dashes(item) for item in df]
df_final = pd.DataFrame(result)
df_final.columns = ['Result']

# 🧪 Comparación con columnas esperadas
test = df_raw.iloc[:, 2:].rename(columns=lambda  x : x.replace('.1', ''))
comparison = df_final == test
df_final = pd.concat([df, df_final, test, comparison], axis=1)
print(tabulate(df_final, headers='keys', tablefmt='fancy_grid'))

# 💾 Exportación opcional
# df_input.to_excel("reverse_between_dashes_output.xlsx", index=False)
