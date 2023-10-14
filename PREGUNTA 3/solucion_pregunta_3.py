import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/master/DATASET/dataSetCodechefUsersWithoutData.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute']

imputar = SimpleImputer(missing_values = np.nan, strategy = 'mean')

# fit -> entrenar
# fit_transform -> probar

print("DATOS INICIALES\n", datos)

# para recorrer por columnas
# para este caso se va a considerar el promedio
for i in range(len(dataset[0])):
  if type(dataset[0][i]) == str:
    continue
  suma = 0
  for j in range(len(dataset)):
    if not np.isnan(dataset[j][i]):
      suma += dataset[j][i]
  
  suma /= len(dataset)

  for j in range(len(dataset)):
    if np.isnan(dataset[j][i]):
      dataset[j][i] = suma

#convirtiendo a dataFrame
dataFrame = pd.DataFrame(dataset, columns = titles)
print("\n\nDatos despues de hacer SimpleImputer manualmente\n\n")
print(dataFrame)





