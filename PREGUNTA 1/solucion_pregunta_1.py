# Enlace colabs
# https://colab.research.google.com/drive/1cXcnYpJiWPmOWjbJvUr2BREDt0tLREaQ?usp=sharing

import pandas as pd
import numpy as np

# para graficar
import seaborn as sns
import matplotlib.pyplot as plt
import random

####################################################################################################
# guardando en un array el dataset
url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/master/DATASET/dataSetCodechefUsers.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute']

####################################################################################################


#################################################
# FUNCIONES
def promedio():
  print("CALCULANDO EL PROMEDIO POR COLUMNAS DEL DATASET")
  promedios = []
  for i in range(len(dataset[0])):
    sum = 0;

    if(type(dataset[0][i]) != str):
      for j in range(len(dataset)):
        sum += dataset[j][i];
      sum /= len(dataset)
    
    promedios.append(sum)
    print(titles[i], sum)
  print()
  graficar(titles, promedios, "Promedio")


def moda():
  print("CALCULANDO LA MODA POR COLUMNAS DEL DATASET")
  total_modas = []
  for i in range(len(dataset[0])):
    mapa = {}
    for j in range(len(dataset)):
      if(dataset[j][i] in mapa):
        mapa[dataset[j][i]] += 1;
      else:
        mapa[dataset[j][i]] = 1;
    
    lista = []
    for key, value in mapa.items():
      lista.append([value, key])
    lista.sort(reverse=True)
    print(titles[i], lista[0][1])
    if(type(lista[0][1]) == str):
      total_modas.append(0)
    else:
      total_modas.append(lista[0][1])
  print()
  graficar(titles, total_modas, "Moda")

def cuartil(k):
  print("QUARTIL ", k)
  quartiles = []
  for i in range(len(dataset[0])):
    sum = 0;
    if( type(dataset[0][i]) != str):
      vector = []
      for j in range(len(dataset)):
        vector.append(dataset[j][i])

      vector.sort()
      cur = k * (len(vector) + 1) / 4
      pos = int(cur)
      print(titles[i], end=  ' ')

      if(cur == pos):
        # quartil es exacto
        print(vector[pos - 1])
        quartiles.append(vector[pos - 1])
      else:
        x1 = vector[pos - 1]
        x2 = vector[pos]
        total = abs(x2 + x1) / 2
        print(total)
        quartiles.append(vector[pos - 1])
    else:
      quartiles.append(0)
  print()
  string_tipo = "Quartil " + str(k)
  graficar(titles, quartiles, string_tipo)



def percentil(k):
  print("PERCENTIL ", k)
  percentiles = []
  for i in range(len(dataset[0])):
    sum = 0;
    if( type(dataset[0][i]) != str):
      vector = []
      for j in range(len(dataset)):
        vector.append(dataset[j][i])

      vector.sort()
      cur = k * (len(vector) + 1) / 100
      pos = int(cur)
      print(titles[i], end=  ' ')

      if(cur == pos):
        # quartil es exacto
        print(vector[pos - 1])
        percentiles.append(vector[pos - 1])
      else:
        x1 = vector[pos - 1]
        x2 = vector[pos]
        total = abs(x2 + x1) / 2
        print(total)
        percentiles.append(total)
    else:
      percentiles.append(0)
  print()
  
  string_tipo = "Percentil " + str(k)
  graficar(titles, percentiles, string_tipo)


def graficar(indices, valores, titulo):
  colores_aleatorios = [random.choice(['red', 'blue', 'green', 'purple', 'orange', 'pink', 'gray', 'brown']) for _ in indices]
  plt.figure(figsize=(15, 4))
  plt.bar(indices, valores, color=colores_aleatorios)


  # Establecer etiquetas y título
  plt.xlabel('Columnas')
  plt.ylabel(titulo)
  plt.title('{} por Columna en el Conjunto de Datos'.format(titulo))

  # Mostrar el gráfico
  plt.show()
  print()
  print()


####################################################



############################### MENU PRINCIPAL #####################################################
promedio()
moda()
cuartil(1)
cuartil(2)
cuartil(3)

percentil(50)
percentil(80)




"""
suponiendo la columna de "rating", aplica para el resto
el promedio es 2022.4267933180479 eso quiere decir que de todos los usuarios registrados
tenemos ese rendimiento promedio en cada concurso

para la moda es 1876 , quiere decir que de todo el rating ese valor es el mas comun
muchos usuarios estan con ese ranking

para el quartil (1) para global rank es 2508 (el quartil 1 es el 25 % de los datos ordenados crecientemente)
significa que el 25% de los datos son <= 2508 

para los percentiles (80) (parte los datos en 100 partes iguales, parecido a los quartiles)
se tiene 2111

eso nos quiere decir que el 80 % de los usuarios tiene ese ranking, lo que significa que muchos usuarios tienen rendimiento
promedio, no son muy pros (considerando a los pros de ranking 3000 para arriba)
"""


