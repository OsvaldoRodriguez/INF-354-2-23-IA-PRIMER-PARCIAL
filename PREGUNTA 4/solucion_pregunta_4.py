import pandas as pd
import numpy as np


url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/master/DATASET/dataSetCodechefUsers.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute']
# Utilizando Etiquetado simple con LabelEncoder

# laberl encoder
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
print(datos)
data_set_mapeado = []
for i in range(len(dataset[0])):
  aux = []
  for j in range(len(dataset)):
    aux.append(dataset[j][i])
  
  if type(aux[0]) != str:
    aux_2 = aux
  else:
    aux_2 = encoder.fit_transform(aux)
  data_set_mapeado.append(aux_2)

# ahora lo convertirmos a un array de numpy para hacer operaciones

dataset_nuevo = np.array(data_set_mapeado)
dataset_nuevo = dataset_nuevo.transpose() # transponiendo los datos porque estaban en filas
#ahora convirtiendo a dataFrame
datitos = pd.DataFrame(dataset_nuevo, columns = titles)
print("\n\nETIQUETADO SIMPLE CON LABELENCODER\n\n", datitos)

# onehotencoder

from sklearn.preprocessing import OneHotEncoder
print(datos)
# Crear una instancia de OneHotEncoder
encoder = OneHotEncoder(sparse=False)
# Ajustar el codificador a los datos y transformar las columnas seleccionadas
one_hot_encoded = encoder.fit_transform(datos[titles])
# Utiliza get_feature_names_out en lugar de get_feature_names
one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(titles))
# Mostrar el DataFrame con las variables categóricas codificadas
print(one_hot_df)

